# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QListWidgetItem

defaultNumberOfData = 129


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1090, 765)
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
        self.surfaceWidget = Surface3D_Graph(defaultNumberOfData, self.splitter)
        self.surfaceWidget.setMinimumSize(QtCore.QSize(0, 400))
        self.surfaceWidget.setObjectName("GLViewWidget")
        self.lineGraphWidget = Line2DGraph(defaultNumberOfData, self.splitter)
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
        self.gridLayout_5.addWidget(self.comboBox, 1, 0, 1, 3)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 0, 0, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.gridLayoutWidget_2)
        self.spinBox.setMaximum(5000)
        self.spinBox.setProperty("value", 1000)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout_5.addWidget(self.spinBox, 9, 2, 1, 3)
        self.pushButton_changeIncomingData = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_changeIncomingData.setObjectName("pushButton_changeIncomingData")
        self.gridLayout_5.addWidget(self.pushButton_changeIncomingData, 10, 2, 1, 3)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label.setObjectName("label")
        self.gridLayout_5.addWidget(self.label, 8, 2, 1, 3)
        self.pushButton_deactivateChannels = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_deactivateChannels.setObjectName("pushButton_deactivateChannels")
        self.gridLayout_5.addWidget(self.pushButton_deactivateChannels, 7, 5, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem, 2, 2, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_5.addWidget(self.lineEdit, 3, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_5.addWidget(self.label_5, 2, 5, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem1, 5, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem2, 6, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_5.addWidget(self.label_3, 0, 4, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout_5.addWidget(self.label_6, 2, 0, 1, 1)
        self.pushButton_activateChannels = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_activateChannels.setObjectName("pushButton_activateChannels")
        self.gridLayout_5.addWidget(self.pushButton_activateChannels, 7, 4, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout_5.addWidget(self.comboBox_2, 1, 4, 1, 2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem3, 7, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_5.addWidget(self.label_4, 2, 4, 1, 1)
        self.line = QtWidgets.QFrame(self.gridLayoutWidget_2)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_5.addWidget(self.line, 0, 3, 8, 1)
        self.pushButton_offset = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_offset.setObjectName("pushButton")
        self.gridLayout_5.addWidget(self.pushButton_offset, 4, 0, 1, 1)
        self.listWidget_activeChannels = QtWidgets.QListWidget(self.gridLayoutWidget_2)
        self.listWidget_activeChannels.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWidget_activeChannels.setObjectName("listWidget_activeChannels")
        self.gridLayout_5.addWidget(self.listWidget_activeChannels, 3, 5, 4, 1)
        self.listWidget_inactiveChannels = QtWidgets.QListWidget(self.gridLayoutWidget_2)
        self.listWidget_inactiveChannels.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWidget_inactiveChannels.setObjectName("listWidget_inactiveChannels")
        self.gridLayout_5.addWidget(self.listWidget_inactiveChannels, 3, 4, 4, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem4, 4, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem5, 3, 2, 1, 1)
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

        self.initChannelLists()
        self.setupTCP()

        self.comboBox.currentTextChanged.connect(self.on_combobox_3D_changed)
        self.comboBox_2.currentTextChanged.connect(self.on_combobox_2D_changed)
        self.pushButton_changeIncomingData.pressed.connect(self.on_pushButton_incData_changed)
        self.pushButton_activateChannels.pressed.connect(self.activateChannels)
        self.pushButton_deactivateChannels.pressed.connect(self.deactiveChannels)
        self.pushButton_offset.pressed.connect(self.changeOffset)

    def setupTCP(self):
        self.tcpHandler = TCP_Handler(self.surfaceWidget, self.lineGraphWidget)

    def on_combobox_3D_changed(self, value):
        try:
            print("combobox 3D changed", value)
            # wait for last update to finish, so that changes to data don't get overwritten
            self.tcpHandler.stopUpdating()
            self.surfaceWidget.updateWidthOfData(int(value))
            self.tcpHandler.startUpdating()
        except:
            print("Unexpected error:", sys.exc_info()[1])

    def on_combobox_2D_changed(self, value):
        print("combobox 2D changed", value)

    #        self.tcpHandler.stopUpdating()
    #        self.lineGraphWidget.updateWidthOfData(int(value))
    #        self.tcpHandler.startUpdating()

    def on_pushButton_incData_changed(self):
        # try:
        incomingData = self.spinBox.value()
        print("pushbutton pressed!", incomingData)
        # wait for last update to finish, so that changes to data don't get overwritten
        self.tcpHandler.stopUpdating()
        self.surfaceWidget.updateNumberOfData(incomingData)
        self.lineGraphWidget.updateNumberOfData(incomingData)
        self.tcpHandler.startUpdating()

    # except:
    # print("on_pushButton_incData_changed:", sys.exc_info()[1])

    def initChannelLists(self):
        for i in range(defaultNumberOfData):
            self.listWidget_inactiveChannels.addItem(ListWidgetItem(str(i)))

    def activateChannels(self):
        self.tcpHandler.stopUpdating()
        items = [item.text() for item in self.listWidget_inactiveChannels.selectedItems()]
        for item in items:
            item = ListWidgetItem(item)
        self.listWidget_activeChannels.addItems(items)
        for item in self.listWidget_inactiveChannels.selectedItems():
            self.listWidget_inactiveChannels.takeItem(self.listWidget_inactiveChannels.row(item))
        self.listWidget_activeChannels.sortItems()
        self.lineGraphWidget.addLines(items)
        self.tcpHandler.startUpdating()

    def deactiveChannels(self):
        self.tcpHandler.stopUpdating()
        items = [item.text() for item in self.listWidget_activeChannels.selectedItems()]
        for item in items:
            item = ListWidgetItem(item)
        self.listWidget_inactiveChannels.addItems(items)
        for item in self.listWidget_activeChannels.selectedItems():
            self.listWidget_activeChannels.takeItem(self.listWidget_activeChannels.row(item))
        self.listWidget_inactiveChannels.sortItems()
        self.lineGraphWidget.removeLines(items)
        self.tcpHandler.startUpdating()

    def changeOffset(self):
        self.tcpHandler.stopUpdating()
        try:
            self.surfaceWidget.updateOffset(int(self.lineEdit.text()))
        except:
            print("Unexpected error:", sys.exc_info()[1])
        self.tcpHandler.startUpdating()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RadarPlotter"))
        self.comboBox.setCurrentText(_translate("MainWindow", "500"))
        self.comboBox.setItemText(0, _translate("MainWindow", "50"))
        self.comboBox.setItemText(1, _translate("MainWindow", "100"))
        self.comboBox.setItemText(2, _translate("MainWindow", "250"))
        self.comboBox.setItemText(3, _translate("MainWindow", "500"))
        self.comboBox.setItemText(4, _translate("MainWindow", "1000"))
        self.label_2.setText(_translate("MainWindow", "Data Shown:"))
        self.pushButton_changeIncomingData.setText(_translate("MainWindow", "Ok"))
        self.label.setText(_translate("MainWindow", "Incoming Data/t:"))
        self.pushButton_deactivateChannels.setText(_translate("MainWindow", "Deactivate"))
        self.lineEdit.setText(_translate("MainWindow", "0"))
        self.label_5.setText(_translate("MainWindow", "Active Channels:"))
        self.label_3.setText(_translate("MainWindow", "Data Shown:"))
        self.label_6.setText(_translate("MainWindow", "Offset:"))
        self.pushButton_activateChannels.setText(_translate("MainWindow", "Activate"))
        self.comboBox_2.setCurrentText(_translate("MainWindow", "500"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "50"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "100"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "250"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "500"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "1000"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "2500"))
        self.label_4.setText(_translate("MainWindow", "Inactive Channels:"))
        self.pushButton_offset.setText(_translate("MainWindow", "Set Offset"))
        self.menutest.setTitle(_translate("MainWindow", "3D"))
        self.menuTest2.setTitle(_translate("MainWindow", "2D"))
        self.actionTestMen.setText(_translate("MainWindow", "TestMenü"))


class ListWidgetItem(QListWidgetItem):
    def __lt__(self, other):
        try:
            return int(self.text()) < int(other.text())
        except Exception:
            return QListWidgetItem.__lt__(self, other)


from Graphs.Line2D_Graph import Line2DGraph
from Graphs.Surface3D_Graph import Surface3D_Graph
from TCP.TCP_Handler import TCP_Handler
