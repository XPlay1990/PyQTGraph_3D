# -*- coding: utf-8 -*-
"""
Jan Adamczyk - 2018
"""
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.opengl as gl
import numpy as np
import datetime


class Surface3D_Graph(gl.GLViewWidget):
    def __init__(self, parent=None, **kargs):
        # pg.GraphicsWindow.__init__(self, **kargs)
        gl.GLViewWidget.__init__(self, **kargs)
        self.setParent(parent)
        self.setWindowTitle('Radar-Plot')

        self.numberOfData = 1000
        self.widthOfData = 500
        self.x = np.linspace(-self.widthOfData / 2, self.widthOfData / 2, self.widthOfData)
        self.y = np.linspace(-self.numberOfData / 2, self.numberOfData / 2, self.numberOfData)
        # colormap = cm.get_cmap('jet')  # cm.get_cmap("CMRmap") 'viridis'
        # colormap._init()
        # lut = (colormap._lut * 255).view(np.ndarray)  # Convert matplotlib colormap from 0-1 to 0 -255 for Qt

        self.surfacePlot = gl.GLSurfacePlotItem(self.x, self.y, shader='heightColor', computeNormals=False,
                                                smooth=False)  # smooth true = faster; dont turn on computenormals
        self.surfacePlot.shader()['colorMap'] = np.array([0.01, 40, 0.5, 0.01, 40, 1, 0.01, 40, 2])  # lut
        # p4.setDepthValue(1000)
        # p4.setGLOptions('opaque')
        self.surfaceData = np.zeros((self.widthOfData, self.numberOfData), dtype=int)

        self.show()
        self.setWindowTitle('PAS Surfaceplot')
        self.setGeometry(100, 100, 1500, 800)  # distance && resolution
        self.setCameraPosition(distance=1000)

        ## Create axis
        # axis = pg.AxisItem('left', pen=None, linkView=None, parent=None, maxTickLength=-5, showValues=True)
        # axis.show()
        # axis = pg.AxisItem('left', pen = None)
        # xAxis.paint()
        # Axis.setSize(self.valueNumber, self.valueNumber, self.valueNumber)
        # axis.setStyle(showValues = True)
        # axis.show()
        # --------------------
        axis = gl.GLAxisItem()
        axis.setSize(x=1000, y=1000, z=1000, size=None)
        # xAxis.paint()
        # axis.setSize(self.valueNumber, self.valueNumber, self.valueNumber)
        self.addItem(axis)

        ## Add a grid to the view
        g = gl.GLGridItem()
        g.setSize(x=self.widthOfData * 2, y=self.numberOfData * 2)
        # g.scale(2,2,1000)
        g.setDepthValue(10)  # draw grid after surfaces since they may be translucent
        self.addItem(g)

        ## create a surface plot, tell it to use the 'heightColor' shader
        ## since this does not require normal vectors to render (thus we
        ## can set computeNormals=False to save time when the mesh updates)
        # p4.translate(100, 100, 0)
        self.addItem(self.surfacePlot)

    def startGUI(self):
        print("Init 3D-Surface GUI")
        ## Create a GL View widget to display data
        app = QtGui.QApplication([])
        w = gl.GLViewWidget()
        w.show()
        w.setWindowTitle('PAS Surfaceplot')
        w.setGeometry(100, 100, 1500, 800)  # distance && resolution
        w.setCameraPosition(distance=1000)

        ## Create axis
        # axis = pg.AxisItem('left', pen=None, linkView=None, parent=None, maxTickLength=-5, showValues=True)
        # axis.show()
        # axis = pg.AxisItem('left', pen = None)
        # xAxis.paint()
        # Axis.setSize(self.valueNumber, self.valueNumber, self.valueNumber)
        # axis.setStyle(showValues = True)
        # axis.show()
        # --------------------
        axis = gl.GLAxisItem()
        axis.setSize(x=1000, y=1000, z=1000, size=None)
        # xAxis.paint()
        # axis.setSize(self.valueNumber, self.valueNumber, self.valueNumber)
        w.addItem(axis)

        ## Add a grid to the view
        g = gl.GLGridItem()
        g.setSize(x=self.widthOfData * 2, y=self.numberOfData * 2)
        # g.scale(2,2,1000)
        g.setDepthValue(10)  # draw grid after surfaces since they may be translucent
        w.addItem(g)

        ## create a surface plot, tell it to use the 'heightColor' shader
        ## since this does not require normal vectors to render (thus we
        ## can set computeNormals=False to save time when the mesh updates)
        # p4.translate(100, 100, 0)
        w.addItem(self.surfacePlot)

        ## Start Qt event loop unless running in interactive mode.
        import sys
        if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
            QtGui.QApplication.instance().exec_()
        print("Init 3D-Surface GUI finished")

    # update via timer
    def updateSelf(self):
        timeBeforeUpdate = datetime.datetime.now()
        self.surfaceData = np.delete(self.surfaceData, 0, 0)
        newValues = np.random.randint(5, size=(1, self.numberOfData))
        # print('newval ', newValues)
        self.surfaceData = np.concatenate((self.surfaceData, newValues))
        self.surfacePlot.setData(z=self.surfaceData)
        timeAfterUpdate = datetime.datetime.now()
        timeDiff = timeAfterUpdate - timeBeforeUpdate
        elapsed_ms = (timeDiff.days * 86400000) + (timeDiff.seconds * 1000) + (timeDiff.microseconds / 1000)
        print(elapsed_ms, ' ms')

    # update via tcp
    def updateData(self, framesList):
        timeBeforeUpdate = datetime.datetime.now()
        for frame in framesList:
            self.surfaceData = np.delete(self.surfaceData, 0, 0)
            frame = np.array(frame, ndmin=2)
            # print('data: ', data)
            # print('frame: ', frame)
            self.surfaceData = np.concatenate((self.surfaceData, frame))
            self.surfacePlot.setData(z=self.surfaceData)
        timeAfterUpdate = datetime.datetime.now()
        timeDiff = timeAfterUpdate - timeBeforeUpdate
        elapsed_ms = (timeDiff.days * 86400000) + (timeDiff.seconds * 1000) + (timeDiff.microseconds / 1000)
        # print(elapsed_ms, ' ms')

    # init()
    # timer = QtCore.QTimer()
    # timer.timeout.connect(updateSelf)
    # timer.start(20)
