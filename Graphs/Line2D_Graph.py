# -*- coding: utf-8 -*-
"""
Jan Adamczyk - 2018
"""
import os
import sys

import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np


class Line2DGraph(pg.GraphicsLayoutWidget):
    pg.setConfigOption('background', 'w')
    pg.setConfigOption('foreground', 'k')
    ptr1 = 0

    def __init__(self, parent=None, **kargs):
        self.widthOfData = 500
        self.graphrange = np.arange(0, self.widthOfData, 1)
        pg.GraphicsWindow.__init__(self, **kargs)
        self.setParent(parent)
        self.setWindowTitle('Radar-Plot')
        self.setAntialiasing(True)
        self.p1 = self.addPlot(labels={'left': 'Voltage', 'bottom': 'Time'})
        self.p1.showGrid(x=True, y=True)
        self.data1 = np.zeros(self.widthOfData)
        self.data2 = np.zeros(self.widthOfData)
        self.curve1 = self.p1.plot(self.data1, pen=(3, 3))
        self.curve2 = self.p1.plot(self.data2, pen=(2, 3))
        self.activeChannels = []

    def updateData(self, framesList):
        try:
            for frame in framesList:
                self.data1[:-1] = self.data1[1:]  # shift data in the array one sample left
                # (see also: np.roll)
                self.data1[-1] = frame[0]
                self.data1[np.isinf(self.data1)] = np.nan
                self.curve1.setData(self.graphrange, self.data1)

                self.data2[:-1] = self.data2[1:]  # shift data in the array one sample left
                # (see also: np.roll)
                self.data2[-1] = frame[1]
                self.data2[np.isinf(self.data2)] = np.nan
                self.curve2.setData(self.graphrange, self.data2)
        except:
            print("2D Update:", sys.exc_info()[1])

    # changes sample-quantity of the shown data
    def updateWidthOfData(self, quantity):
        try:
            self.widthOfData = quantity
            self.data1 = np.zeros(self.widthOfData)
        except:
            print("Unexpected error:", sys.exc_info()[1])

    # add and remove 2D Lines
    def addLines(self, lines):
        # ToDo insert working code
        for line in lines:
            self.curves.append(self.p1.plot(self.data1, pen=(3, 3)))
            self.activeChannels.append(lines.line)

    def removeLines(self, lines):
        # ToDo insert working code
        for line in lines:
            self.curves.append(self.p1.plot(self.data1, pen=(3, 3)))
            self.activeChannels.append(lines.line)
