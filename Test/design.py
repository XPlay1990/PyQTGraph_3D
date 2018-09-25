# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1090, 752)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.surfaceWidget = Surface3D_Graph(self.splitter)
        self.surfaceWidget.setObjectName("GLViewWidget")
        self.lineGraphWidget = Line2DGraph(self.splitter)
        self.lineGraphWidget.setObjectName("widget")
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout.addWidget(self.checkBox_2, 7, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 2, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 5, 0, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 6, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1090, 26))
        self.menubar.setObjectName("menubar")
        self.menutest = QtWidgets.QMenu(self.menubar)
        self.menutest.setEnabled(True)
        self.menutest.setObjectName("menutest")
        self.menuTest2 = QtWidgets.QMenu(self.menubar)
        self.menuTest2.setObjectName("menuTest2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbarTest = QtWidgets.QStatusBar(MainWindow)
        self.statusbarTest.setEnabled(True)
        self.statusbarTest.setObjectName("statusbarTest")
        MainWindow.setStatusBar(self.statusbarTest)
        self.actionTestMen = QtWidgets.QAction(MainWindow)
        self.actionTestMen.setObjectName("actionTestMen")
        self.menutest.addAction(self.actionTestMen)
        self.menubar.addAction(self.menutest.menuAction())
        self.menubar.addAction(self.menuTest2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.setupTCP()

    def setupTCP(self):
        tcp = TCP_Handler(self.surfaceWidget, self.lineGraphWidget)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RadarPlotter"))
        self.checkBox_2.setText(_translate("MainWindow", "CheckBox"))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.checkBox.setText(_translate("MainWindow", "CheckBox"))
        self.menutest.setTitle(_translate("MainWindow", "test"))
        self.menuTest2.setTitle(_translate("MainWindow", "Test2"))
        self.actionTestMen.setText(_translate("MainWindow", "TestMenü"))


from Test.Line2D_Graph import Line2DGraph
from Test.Surface3D_Graph import Surface3D_Graph
from Test.TCP_Handler import TCP_Handler
