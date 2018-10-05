import datetime
import sys
import time

import numpy as np

from matplotlib.backends.qt_compat import QtCore, QtWidgets, is_pyqt5

if is_pyqt5():
    from matplotlib.backends.backend_qt5agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
else:
    from matplotlib.backends.backend_qt4agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self, defaultNumberOfData, splitter, parent=None):
        super().__init__()
        splitter.addWidget(self)
        self.numberOfData = defaultNumberOfData
        self.widthOfData = 500
        self._main = QtWidgets.QWidget()
        self.setCentralWidget(self._main)
        layout = QtWidgets.QVBoxLayout(self._main)

        dynamic_canvas = FigureCanvas(Figure(figsize=(5, 3)))
        layout.addWidget(dynamic_canvas)
        self.graphrange = np.arange(0, self.widthOfData, 1)
        self._dynamic_ax = dynamic_canvas.figure.subplots()

        self.dataArray = []
        for i in range(self.numberOfData):
            self.dataArray.append(np.zeros(self.widthOfData))
        self.activeChannels = []

    def updateData(self, framesList):
        self.timeBeforeUpdate = datetime.datetime.now()
        self._dynamic_ax.clear()
        # Shift the sinusoid as a function of time.
        try:
            for frame in framesList:
                for activeChannel in self.activeChannels:
                    self.dataArray[activeChannel][:-1] = self.dataArray[activeChannel][
                                                         1:]  # shift data in the array one sample left
                    # (see also: np.roll)
                    self.dataArray[activeChannel][-1] = frame[activeChannel]
                    self.dataArray[activeChannel][
                        np.isinf(self.dataArray[activeChannel])] = np.nan  # should prevent problems with autoscaling
            for activeChannel in self.activeChannels:
                self._dynamic_ax.plot(self.graphrange, self.dataArray[activeChannel])
            if self.activeChannels:  # If list is not empty
                self._dynamic_ax.figure.canvas.draw_idle()
        except:
            print("2D Update:", sys.exc_info()[1])
        timeAfterUpdate = datetime.datetime.now()
        timeDiff = timeAfterUpdate - self.timeBeforeUpdate
        elapsed_ms = (timeDiff.days * 86400000) + (timeDiff.seconds * 1000) + (timeDiff.microseconds / 1000)
        print("Matplot 2D Time: ", elapsed_ms, ' ms')

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
        # self.initLines()

    def removeLines(self, lines):
        self.removeAllLines()
        for lineIndex in lines:
            self.activeChannels.remove(int(lineIndex))
        self.initLines()

    def removeAllLines(self):
        self._dynamic_ax.clear()

    def enableAutoScale(self):
        self.p1.enableAutoScale()

    def initLines(self):
        for index in self.activeChannels:
            self.linesList[index] = self.p1.plot(self.dataArray[index], pen=(index, 3))
