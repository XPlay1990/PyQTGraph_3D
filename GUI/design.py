# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QListWidgetItem

defaultNumberOfData = 128


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1090, 791)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.layoutWidget = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget.setObjectName("layoutWidget")
        self.graphLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.graphLayout.setContentsMargins(0, 0, 0, 0)
        self.graphLayout.setObjectName("graphLayout")
        self.graphSplitter = QtWidgets.QSplitter(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphSplitter.sizePolicy().hasHeightForWidth())
        self.graphSplitter.setSizePolicy(sizePolicy)
        self.graphSplitter.setOrientation(QtCore.Qt.Horizontal)
        self.graphSplitter.setObjectName("graphSplitter")
        self.graph3DWidget = Surface3D_Graph(defaultNumberOfData, self.graphSplitter)
        self.graph3DWidget.setMinimumSize(QtCore.QSize(0, 400))
        self.graph3DWidget.setObjectName("graph3DWidget")
        self.graph2DWidget = Line2DGraph(defaultNumberOfData, self.graphSplitter)
        self.graph2DWidget.setObjectName("graph2DWidget")
        self.graphLayout.addWidget(self.graphSplitter, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.splitter_2)
        self.controlLayout = QtWidgets.QGridLayout()
        self.controlLayout.setObjectName("controlLayout")
        self.control3D_Layout = QtWidgets.QGridLayout()
        self.control3D_Layout.setObjectName("control3D_Layout")
        self.offset_lable = QtWidgets.QLabel(self.centralwidget)
        self.offset_lable.setObjectName("offset_lable")
        self.control3D_Layout.addWidget(self.offset_lable, 2, 0, 1, 1)
        self.dataShown_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.dataShown_comboBox.setObjectName("dataShown_comboBox")
        self.dataShown_comboBox.addItem("")
        self.dataShown_comboBox.addItem("")
        self.dataShown_comboBox.addItem("")
        self.dataShown_comboBox.addItem("")
        self.dataShown_comboBox.addItem("")
        self.control3D_Layout.addWidget(self.dataShown_comboBox, 1, 0, 1, 1)
        self.dataShown_lable = QtWidgets.QLabel(self.centralwidget)
        self.dataShown_lable.setObjectName("dataShown_lable")
        self.control3D_Layout.addWidget(self.dataShown_lable, 0, 0, 1, 1)
        self.offset_Button = QtWidgets.QPushButton(self.centralwidget)
        self.offset_Button.setObjectName("offset_Button")
        self.control3D_Layout.addWidget(self.offset_Button, 4, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.control3D_Layout.addItem(spacerItem, 5, 0, 1, 1)
        self.offset_LineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.offset_LineEdit.setObjectName("offset_LineEdit")
        self.control3D_Layout.addWidget(self.offset_LineEdit, 3, 0, 1, 1)
        self.controlLayout.addLayout(self.control3D_Layout, 1, 0, 1, 1)
        self.control2D_Layout = QtWidgets.QGridLayout()
        self.control2D_Layout.setObjectName("control2D_Layout")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.control2D_Layout.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.controlLayout.addLayout(self.control2D_Layout, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.controlLayout)
        self.controlIncomingData_Layout = QtWidgets.QGridLayout()
        self.controlIncomingData_Layout.setObjectName("controlIncomingData_Layout")
        self.incomingData_spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.incomingData_spinBox.setObjectName("incomingData_spinBox")
        self.incomingData_spinBox.setMaximum(5000)
        self.incomingData_spinBox.setProperty("value", defaultNumberOfData)
        self.controlIncomingData_Layout.addWidget(self.incomingData_spinBox, 1, 1, 1, 1)
        self.incomingData_Lable = QtWidgets.QLabel(self.centralwidget)
        self.incomingData_Lable.setObjectName("incomingData_Lable")
        self.controlIncomingData_Layout.addWidget(self.incomingData_Lable, 0, 1, 1, 1)
        self.incomingData_Button = QtWidgets.QPushButton(self.centralwidget)
        self.incomingData_Button.setObjectName("incomingData_Button")
        self.controlIncomingData_Layout.addWidget(self.incomingData_Button, 2, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.controlIncomingData_Layout.addItem(spacerItem1, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.controlIncomingData_Layout.addItem(spacerItem2, 1, 2, 1, 1)
        self.verticalLayout.addLayout(self.controlIncomingData_Layout)
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
        self.actionTestMen.setCheckable(True)
        self.actionTestMen.setChecked(True)
        self.actionTestMen.setObjectName("actionTestMen")
        self.menutest.addAction(self.actionTestMen)
        self.menubar.addAction(self.menutest.menuAction())
        self.menubar.addAction(self.menuTest2.menuAction())

        self.retranslateUi(MainWindow)
        self.dataShown_comboBox.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # self.initChannelLists()
        self.setupTCP()

        self.dataShown_comboBox.currentTextChanged.connect(self.on_combobox_3D_changed)
        self.incomingData_Button.pressed.connect(self.on_pushButton_incData_changed)
        self.offset_Button.pressed.connect(self.changeOffset)
        self.tableWidget.itemSelectionChanged.connect(self.changeSelected2DLines)

    def setupTCP(self):
        self.tcpHandler = TCP_Handler(self.graph3DWidget, self.graph2DWidget)

    def on_combobox_3D_changed(self, value):
        try:
            print("combobox 3D changed", value)
            # wait for last update to finish, so that changes to data don't get overwritten
            self.tcpHandler.stopUpdating()
            self.graph3DWidget.updateWidthOfData(int(value))
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
        incomingData = self.incomingData_spinBox.value()
        print("pushbutton pressed!", incomingData)
        # wait for last update to finish, so that changes to data don't get overwritten
        self.tcpHandler.stopUpdating()
        self.graph3DWidget.updateNumberOfData(incomingData)
        self.graph2DWidget.updateNumberOfData(incomingData)
        self.tcpHandler.startUpdating()

    # except:
    # print("on_pushButton_incData_changed:", sys.exc_info()[1])

    # def initChannelLists(self):

    # def activateChannels(self):

    # def deactiveChannels(self):

    def changeOffset(self):
        self.tcpHandler.stopUpdating()
        try:
            self.graph3DWidget.updateOffset(int(self.offset_LineEdit.text()))
        except:
            print("Unexpected error:", sys.exc_info()[1])
        self.tcpHandler.startUpdating()

    def changeSelected2DLines(self):
        x = self.tableWidget.selectedIndexes()
        rows = []
        for idx in self.tableWidget.selectedIndexes():
            rows.append(idx.row())
        cols = []
        for idx in self.tableWidget.selectedIndexes():
            cols.append(idx.column())
        print("ROW: ", rows)
        print("COL: ", cols)
        self.graph2DWidget.setActiveChannels(rows, cols)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RadarPlotter"))
        self.offset_lable.setText(_translate("MainWindow", "Offset:"))
        self.dataShown_comboBox.setItemText(0, _translate("MainWindow", "50"))
        self.dataShown_comboBox.setItemText(1, _translate("MainWindow", "100"))
        self.dataShown_comboBox.setItemText(2, _translate("MainWindow", "250"))
        self.dataShown_comboBox.setItemText(3, _translate("MainWindow", "500"))
        self.dataShown_comboBox.setItemText(4, _translate("MainWindow", "1000"))
        self.dataShown_lable.setText(_translate("MainWindow", "Data Shown:"))
        self.offset_Button.setText(_translate("MainWindow", "Set Offset"))
        self.offset_LineEdit.setText(_translate("MainWindow", "0"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "T1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "T2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "T3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "T4"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "T5"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Dist"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "db"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Phi"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Speed"))
        self.incomingData_Lable.setText(_translate("MainWindow", "Incoming Data/t:"))
        self.incomingData_Button.setText(_translate("MainWindow", "Ok"))
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
