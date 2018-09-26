"""
Jan Adamczyk - 2018
"""

import socket
from threading import Thread


class TCP_Handler:
    """demonstration class only
      - coded for clarity, not efficiency
    """
    completeFrames = []
    incompleteFrames = []
    replace_list = ['[', ']', '\r', ' ']
    updateThread = Thread();

    def __init__(self, surface3d_Graph, line2D_Graph, sock=None):
        self.surface3d_Graph = surface3d_Graph
        self.line2D_Graph = line2D_Graph
        if sock is None:
            self.sock = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock
        self.connect('127.0.0.1', 1337)
        socketReadThread = Thread(target=self.read)
        socketReadThread.start()

    def connect(self, host, port):
        self.sock.connect((host, port))

    def read(self):
        while True:
            chunk = self.sock.recv(50)  # if datapackets are smaller than this or splitting-method has to change!
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
                for i in range(0, len(self.incompleteFrames)):
                    completeFrame += self.incompleteFrames[i]
                completeFrame += split[0]
                # completeFrame.replace('\r', '')
                completeFrame = self.remove_multiple_strings(completeFrame, self.replace_list)
                # print(completeFrame)
                completeFrame = completeFrame.split(',')
                completeFrame = list(map(int, completeFrame))

                # fill up completeFrames-Array
                self.incompleteFrames = []
                self.incompleteFrames.append(split[1])
                self.completeFrames.append(completeFrame)
                # print(self.completeFrames)

                # Draw Graph if library is ready, otherwise buffer in completeFrames
                if not self.updateThread.is_alive():
                    # starting independent Graph-Thread
                    # GLSurfacePlot.updateSelf()
                    update3D = Thread(target=self.surface3d_Graph.updateData,
                                      args=([self.completeFrames]))
                    update2D = Thread(target=self.line2D_Graph.updateData, args=([self.completeFrames]))
                    update2D.start()
                    update3D.start()
                    update3D.join()
                    update2D.join()
                    # self.updateThread = Thread(target=GLSurfacePlot.update, args=(self.completeFrames))
                    # self.updateThread.start()

                    self.completeFrames = []
                    # self.completeFramesIndex = 0
            else:  # and chunk != '['and chunk != ']'
                self.incompleteFrames.append(chunk)

    @staticmethod
    def remove_multiple_strings(cur_string, replace_list):
        for cur_word in replace_list:
            cur_string = cur_string.replace(cur_word, '')
        return cur_string
