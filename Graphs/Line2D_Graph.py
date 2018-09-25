import datetime
from odbc import dataError

from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg


class Line2D_Graph:
    def __init__(self):
        self.activeIndex = 1;
        self.data = np.random.normal(size=(1, 1000))

    def startGUI(self):
        # QtGui.QApplication.setGraphicsSystem('raster')
        app = QtGui.QApplication([])
        # mw = QtGui.QMainWindow()
        # mw.resize(800,800)


        win = pg.GraphicsWindow(title="Basic plotting examples")
        win.resize(1000, 600)
        win.setWindowTitle('pyqtgraph example: Plotting')

        # Enable antialiasing for prettier plots
        pg.setConfigOptions(antialias=True)

        line = win.addPlot(title="Updating plot")
        self.curve = line.plot(pen='y')

        #import sys
        #sys.exit(app.exec_())

        ## Start Qt event loop unless running in interactive mode or using pyside.
        #if __name__ == '__main__':
            #import sys

            #if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
               # QtGui.QApplication.instance().exec_()

    def selfUpdate(self):
        global curve, data, ptr, curve
        self.curve.setData(data[ptr % 1])
        if ptr == 0:
            self.line.enableAutoRange('xy', False)  ## stop auto-scaling after the first data set is plotted
        ptr += 1

    def update(self, framesList):
        timeBeforeUpdate = datetime.datetime.now()
        for frame in framesList:
            # data = np.delete(data, 0, 0)
            frame = np.array(frame, ndmin=2)
            # print('data: ', data)
            # print('frame: ', frame)
            t = frame.item(self.activeIndex)
            # data = np.concatenate((data, [t]))
            self.data = np.append(self.data, t)
            self.data = np.delete(self.data, 0, 0)
            self.curve.setData(self.data)
        timeAfterUpdate = datetime.datetime.now()
        timeDiff = timeAfterUpdate - timeBeforeUpdate
        elapsed_ms = (timeDiff.days * 86400000) + (timeDiff.seconds * 1000) + (timeDiff.microseconds / 1000)
        # print(elapsed_ms, ' ms')
