# -*- coding: utf-8 -*-
"""
Jan Adamczyk - 2018
"""
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.opengl as gl
import numpy as np
import datetime

numberOfData = 1000
widthOfData = 100
x = np.linspace(-widthOfData / 2, widthOfData / 2, widthOfData)
y = np.linspace(-numberOfData / 2, numberOfData / 2, numberOfData)
#colormap = cm.get_cmap('jet')  # cm.get_cmap("CMRmap") 'viridis'
#colormap._init()
#lut = (colormap._lut * 255).view(np.ndarray)  # Convert matplotlib colormap from 0-1 to 0 -255 for Qt
p4 = gl.GLSurfacePlotItem(x, y, shader='heightColor', computeNormals=False,
                          smooth=False)  # smooth true = faster; dont turn on computenormals
p4.shader()['colorMap'] = np.array([0.01, 40, 0.5, 0.01, 40, 1, 0.01, 40, 2]) #lut
#p4.setDepthValue(1000)
# p4.setGLOptions('opaque')
data = np.zeros((widthOfData, numberOfData), dtype=int)

index = 0


def init():
    global p4, data, index

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
    # xAxis.paint()
    # axis.setSize(self.valueNumber, self.valueNumber, self.valueNumber)
    w.addItem(axis)

    ## Add a grid to the view
    g = gl.GLGridItem()
    g.setSize(x=widthOfData * 2, y=numberOfData * 2)
    # g.scale(2,2,1000)
    g.setDepthValue(10)  # draw grid after surfaces since they may be translucent
    w.addItem(g)

    ## create a surface plot, tell it to use the 'heightColor' shader
    ## since this does not require normal vectors to render (thus we
    ## can set computeNormals=False to save time when the mesh updates)
    # p4.translate(100, 100, 0)
    w.addItem(p4)

    # timer = QtCore.QTimer()
    # timer.timeout.connect(updateSelf)
    # timer.start(20)

    ## Start Qt event loop unless running in interactive mode.
    import sys

    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()

#update via timer
def updateSelf():
    global p4, data, index
    timeBeforeUpdate = datetime.datetime.now()
    data = np.delete(data, 0, 0)
    newValues = np.random.randint(5, size=(1, numberOfData))
    # print('newval ', newValues)
    data = np.concatenate((data, newValues))
    p4.setData(z=data)
    timeAfterUpdate = datetime.datetime.now()
    timeDiff = timeAfterUpdate - timeBeforeUpdate
    elapsed_ms = (timeDiff.days * 86400000) + (timeDiff.seconds * 1000) + (timeDiff.microseconds / 1000)
    print(elapsed_ms, ' ms')

#update via tcp
def update(framesList):
    global p4, data, index
    timeBeforeUpdate = datetime.datetime.now()
    for frame in framesList:
        data = np.delete(data, 0, 0)
        frame = np.array(frame, ndmin=2)
        # print('data: ', data)
        # print('frame: ', frame)
        data = np.concatenate((data, frame))
        p4.setData(z=data)
    timeAfterUpdate = datetime.datetime.now()
    timeDiff = timeAfterUpdate - timeBeforeUpdate
    elapsed_ms = (timeDiff.days * 86400000) + (timeDiff.seconds * 1000) + (timeDiff.microseconds / 1000)
    print(elapsed_ms, ' ms')

# init()
# timer = QtCore.QTimer()
# timer.timeout.connect(updateSelf)
# timer.start(20)
