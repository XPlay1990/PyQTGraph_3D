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
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.layoutWidget = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtWidgets.QSplitter(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.surfaceWidget = Surface3D_Graph(self.splitter)
        self.surfaceWidget.setMinimumSize(QtCore.QSize(0, 400))
        self.surfaceWidget.setObjectName("GLViewWidget")
        self.lineGraphWidget = Line2DGraph(self.splitter)
        self.lineGraphWidget.setObjectName("widget")
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.splitter_2)
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_5.addWidget(self.comboBox, 1, 0, 1, 2)
        self.comboBox_2 = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout_5.addWidget(self.comboBox_2, 1, 2, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_5.addWidget(self.label_3, 0, 2, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.gridLayoutWidget_2)
        self.spinBox.setMaximum(5000)
        self.spinBox.setProperty("value", 1000)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout_5.addWidget(self.spinBox, 3, 1, 1, 2)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_5.addWidget(self.pushButton, 4, 1, 1, 2)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label.setObjectName("label")
        self.gridLayout_5.addWidget(self.label, 2, 1, 1, 2)
        self.verticalLayout.addWidget(self.splitter_2)
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
        self.comboBox.setCurrentIndex(3)
        self.comboBox_2.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.setupTCP()

    def setupTCP(self):
        tcp = TCP_Handler(self.surfaceWidget, self.lineGraphWidget)

    def on_combobox_3D_changed(self, value):
        print("combobox 3D changed", value)
        self.surfaceWidget.updateNumberOfData(value)

    def on_combobox_2D_changed(self, value):
        print("combobox 2D changed", value)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RadarPlotter"))
        self.comboBox.setCurrentText(_translate("MainWindow", "500"))
        self.comboBox.setItemText(0, _translate("MainWindow", "50"))
        self.comboBox.setItemText(1, _translate("MainWindow", "100"))
        self.comboBox.setItemText(2, _translate("MainWindow", "250"))
        self.comboBox.setItemText(3, _translate("MainWindow", "500"))
        self.comboBox.setItemText(4, _translate("MainWindow", "1000"))
        self.comboBox.setItemText(5, _translate("MainWindow", "2500"))
        self.comboBox_2.setCurrentText(_translate("MainWindow", "500"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "50"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "100"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "250"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "500"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "1000"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "2500"))
        self.label_2.setText(_translate("MainWindow", "Data Shown:"))
        self.label_3.setText(_translate("MainWindow", "Data Shown:"))
        self.pushButton.setText(_translate("MainWindow", "Ok"))
        self.label.setText(_translate("MainWindow", "Incoming Data/t:"))
        self.menutest.setTitle(_translate("MainWindow", "test"))
        self.menuTest2.setTitle(_translate("MainWindow", "Test2"))
        self.actionTestMen.setText(_translate("MainWindow", "TestMenü"))

        self.comboBox.currentTextChanged.connect(self.on_combobox_3D_changed)
        self.comboBox_2.currentTextChanged.connect(self.on_combobox_2D_changed)


from Graphs.Line2D_Graph import Line2DGraph
from Graphs.Surface3D_Graph import Surface3D_Graph
from TCP.TCP_Handler import TCP_Handler
