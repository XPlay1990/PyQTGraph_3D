# -*- coding: utf-8 -*-
"""
Jan Adamczyk - 2018
"""
import sys
import pyqtgraph as pg
import numpy as np


class Line2DGraph(pg.GraphicsLayoutWidget):
    pg.setConfigOption('background', 'w')
    pg.setConfigOption('foreground', 'k')
    ptr1 = 0

    targetMapping = {"dist","db","phi","speed"}
    mode = "dist"

    def __init__(self, defaultNumberOfData, parent=None, **kargs):
        # super().__init__()
        pg.GraphicsWindow.__init__(self, **kargs)
        self.numberOfData = defaultNumberOfData
        self.widthOfData = 500
        self.graphrange = np.arange(0, self.widthOfData, 1)
        self.setParent(parent)
        self.setWindowTitle('Radar-Plot')
        self.setAntialiasing(True)
        self.p1 = self.addPlot(labels={'left': 'Voltage', 'bottom': 'Time'})
        self.p1.showGrid(x=True, y=True)
        # Use automatic downsampling and clipping to reduce the drawing load
        self.p1.setDownsampling(mode='peak')
        self.p1.setClipToView(True)
        # self.p1.setRange(xRange=[0, self.widthOfData], yRange=[-180, 100])

        self.dataArray = []
        for i in range(self.numberOfData):
            self.dataArray.append(np.zeros(self.widthOfData))
        self.activeChannels = []
        self.linesList = {"lineIndex": "plot"}
        # self.p1.enableAutoRange()
        self.initLines()

        self.timer = pg.QtCore.QTimer()
        self.timer.timeout.connect(self.updateDataSelf)
        self.timer.start(20)

    def updateDataSelf(self):  # test with timer and random data-generation
        try:
            for activeChannel in self.activeChannels:  # drawing the graph
                self.linesList[activeChannel].setData(self.graphrange, self.dataArray[activeChannel])
        except:
            print("2D UpdateGraph:", sys.exc_info()[1])

    def updateData(self, framesList):
        try:
            for frame in framesList:  # Data Handling
                for activeChannel in self.activeChannels:
                    self.dataArray[activeChannel][:-1] = self.dataArray[activeChannel][
                                                         1:]  # shift data in the array one sample left
                    # (see also: np.roll)
                    self.dataArray[activeChannel][-1] = frame[activeChannel]

            for activeChannel in self.activeChannels:  # drawing the graph
                self.linesList[activeChannel].setData(self.graphrange, self.dataArray[activeChannel])
        except:
            print("2D Update:", sys.exc_info()[1])

    # changes sample-quantity of the shown data
    def updateWidthOfData(self, quantity):
        # ToDo: insert Code
        try:
            self.widthOfData = quantity
        except:
            print("Unexpected error:", sys.exc_info()[1])

    # change numberOfData and update dataArray
    def updateNumberOfData(self, quantity):
        self.numberOfData = quantity
        self.refreshDataArray()

    # Change size of dataArray corresponding to numberOfData
    def refreshDataArray(self):
        activeNumberOfData = len(self.dataArray)
        sizeDiff = abs(self.numberOfData - activeNumberOfData)
        if (activeNumberOfData < self.numberOfData):
            for _ in range(sizeDiff):
                self.dataArray.append(np.zeros(self.widthOfData))
        else:
            for _ in range(sizeDiff):
                self.dataArray.pop(len(self.dataArray) - 1)

    # add and remove 2D Lines
    def addLines(self, lines):
        self.removeAllLines()
        for lineIndex in lines:
            self.activeChannels.append(int(lineIndex))
        self.initLines()

    def removeLines(self, lines):
        self.removeAllLines()
        for lineIndex in lines:
            self.activeChannels.remove(int(lineIndex))
        self.initLines()

    def removeAllLines(self):
        self.p1.clear()

    def enableAutoScale(self):
        self.p1.enableAutoScale()

    def initLines(self):
        for index in self.activeChannels:
            self.linesList[index] = self.p1.plot(self.dataArray[index], pen=(index, 3))

    def setCompleteFrames(self, completeFrames):
        self.completeFrames = completeFrames
        try:
            for frame in self.completeFrames:
                for activeChannel in self.activeChannels:
                    self.dataArray[activeChannel][:-1] = self.dataArray[activeChannel][
                                                         1:]  # shift data in the array one sample left
                    # (see also: np.roll)
                    self.dataArray[activeChannel][-1] = frame[activeChannel]
        except:
            print("2D UpdateData:", sys.exc_info()[1])

    def getCompleteFrames(self):
        return self.completeFrames

    def setMode(self, mode):
        self.removeAllLines()
        self.initLines()
        self.mode = mode