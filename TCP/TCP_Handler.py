"""
Jan Adamczyk - 2018
"""
import datetime
import socket
from concurrent import futures
from threading import Thread


class TCP_Handler:
    """demonstration class only
      - coded for clarity, not efficiency
    """
    completeFrames = []
    incompleteFrames = []
    replace_list = ['[', ']', '\r', ' ']
    timeBeforeUpdate = datetime.datetime.now()

    def __init__(self, surface3d_Graph, line2D_Graph, sock=None):
        self.surface3d_Graph = surface3d_Graph
        self.line2D_Graph = line2D_Graph
        self.stopUpdate = False
        self.graphfutures = []
        if sock is None:
            self.sock = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock
        self.connect('127.0.0.1', 15688)
        self.executor = futures.ThreadPoolExecutor(2)
        socketReadThread = Thread(target=self.read)
        socketReadThread.daemon = True
        socketReadThread.start()

    def connect(self, host, port):
        self.sock.connect((host, port))

    def read(self):
        while True:
            chunk = self.sock.recv(50)  # if datapackets are smaller, then this or splitting-method has to change!
            chunk = chunk.decode("utf-8")
            if chunk == '':
                print('Socket closed!')
                raise RuntimeError("socket connection broken")
            elif '\n' in chunk:
                # print('MSG Complete!')

                # split at newline
                split = chunk.split('\n')

                # reset and fill Frame
                completeFrame = ""
                for char in self.incompleteFrames:
                    completeFrame += char
                completeFrame += split[0]
                # completeFrame.replace('\r', '')
                completeFrame = self.remove_multiple_strings(completeFrame, self.replace_list)
                # print(completeFrame)
                completeFrame = completeFrame.split(';')
                #                completeFrame = list(map(int, completeFrame))

                # fill up completeFrames-Array
                self.incompleteFrames = []
                self.incompleteFrames.append(split[1])
                self.completeFrames.append(completeFrame)
                # print(self.completeFrames)

                # print("Buffersize: ", len(self.completeFrames))
                # Draw Graph if library is ready, otherwise buffer in completeFrames
                if self.updateFinished() and not self.stopUpdate:
                    # App-Timer
                    timeAfterUpdate = datetime.datetime.now()
                    timeDiff = timeAfterUpdate - self.timeBeforeUpdate
                    elapsed_ms = (timeDiff.days * 86400000) + (timeDiff.seconds * 1000) + (timeDiff.microseconds / 1000)
                    # print("Redraw Time: ", elapsed_ms, ' ms')
                    self.timeBeforeUpdate = datetime.datetime.now()

                    # updating graphs
                    self.updateGraphs()

                    # clear completeFrames
                    self.completeFrames.clear()
                # else:
                # print("Waiting")
            else:  # no "\n" found
                self.incompleteFrames.append(chunk)

    def updateGraphs(self):
        rangeData = []
        targets = []
        completeTargetFrames = []
        intTargets = []
        for frame in self.completeFrames:
            # print(frame)
            if (frame[0] == "R"):
                del frame[0]  # "R"
                del frame[1]  # "0"
                frame = list(map(int, frame))
                rangeData.append(frame)
            elif (frame[0] == "T"):
                del frame[0]  # "T"
                target = []
                targets = []
                index = 0
                for i in frame:
                    if i == '':
                        targets.append(target)
                        target = []
                    else:
                        target.append(i)
                targets.append(target)
                for t in targets:
                    t = list(map(int, t))
                    intTargets.append(t)
                completeTargetFrames.append(intTargets)

        # starting independent Graph-Threads
        self.graphfutures = []
        future = self.executor.submit(self.surface3d_Graph.updateData, rangeData)
        self.graphfutures.append(future)
        # future = self.executor.submit(self.line2D_Graph.updateData, self.completeFrames.copy())
        # self.graphfutures.append(future)
        self.line2D_Graph.setCompleteFrames(completeTargetFrames)
        # self.waitForUpdatesToFinish()

    def updateFinished(self):
        isFinished = True
        for future in self.graphfutures:
            isFinished = isFinished and future.done()
        return isFinished

    def stopUpdating(self):
        try:
            self.stopUpdate = True
            self.waitForUpdatesToFinish()
        except ValueError:
            pass

    def startUpdating(self):
        self.stopUpdate = False

    def waitForUpdatesToFinish(self):
        for future in self.graphfutures:
            try:
                future.result()
            except AttributeError:
                pass  # why does this occur after setting incoming data very low and wait for a while?

    @staticmethod
    def remove_multiple_strings(cur_string, replace_list):
        for cur_word in replace_list:
            cur_string = cur_string.replace(cur_word, '')
        return cur_string
