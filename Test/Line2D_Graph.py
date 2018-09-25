# -*- coding: utf-8 -*-
"""
Jan Adamczyk - 2018
"""
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np


class Line2DGraph(pg.GraphicsWindow):
    pg.setConfigOption('background', 'w')
    pg.setConfigOption('foreground', 'k')
    ptr1 = 0

    def __init__(self, parent=None, **kargs):
        self.widthOfData = 1000
        pg.GraphicsWindow.__init__(self, **kargs)
        self.setParent(parent)
        self.setWindowTitle('Radar-Plot')
        p1 = self.addPlot(labels={'left': 'Voltage', 'bottom': 'Time'})
        self.data1 = np.zeros(self.widthOfData)
        self.data2 = np.zeros(self.widthOfData)
        self.curve1 = p1.plot(self.data1, pen=(3, 3))
        self.curve2 = p1.plot(self.data2, pen=(2, 3))

        # timer = pg.QtCore.QTimer(self)
        # timer.timeout.connect(self.update)
        # timer.start(2000)  # number of seconds (every 1000) for next update

    def update(self):
        self.data1[:-1] = self.data1[1:]  # shift data in the array one sample left
        # (see also: np.roll)
        self.data1[-1] = np.random.normal()
        self.ptr1 += 1
        self.curve1.setData(self.data1)
        self.curve1.setPos(self.ptr1, 0)

        self.data2[:-1] = self.data2[1:]  # shift data in the array one sample left
        # (see also: np.roll)
        self.data2[-1] = np.random.normal()
        self.curve2.setData(self.data2)
        self.curve2.setPos(self.ptr1, 0)

    def updateData(self, framesList):
        for frame in framesList:
            self.data1[:-1] = self.data1[1:]  # shift data in the array one sample left
            # (see also: np.roll)
            self.data1[-1] = frame[0]
            self.ptr1 += 1
            self.curve1.setData(self.data1)
            self.curve1.setPos(self.ptr1, 0)

            self.data2[:-1] = self.data2[1:]  # shift data in the array one sample left
            # (see also: np.roll)
            self.data2[-1] = frame[1]
            self.curve2.setData(self.data2)
            self.curve2.setPos(self.ptr1, 0)


if __name__ == '__main__':
    w = Line2DGraph()
    w.show()
    QtGui.QApplication.instance().exec_()
