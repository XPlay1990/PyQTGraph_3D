# -*- coding: utf-8 -*-
"""
Jan Adamczyk - 2018
"""
from PyQt5 import QtGui  # Import the PyQt4 module we'll need
import sys  # We need sys so that we can pass argv to QApplication

import Test.design  # This file holds our MainWindow and all design related things


# it also keeps events etc that we defined in Qt Designer

class ExampleApp(QtGui.QMainWindow, Test.design.Ui_MainWindow):
    def __init__(self):
        # Explaining super is out of the scope of this article
        # So please google it if you're not familar with it
        # Simple reason why we use it here is that it allows us to
        # access variables, methods etc in the design.py file
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in design.py file automatically
        # It sets up layout and widgets that are defined


def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = ExampleApp()  # We set the form to be our ExampleApp (design)
    form.show()  # Show the form
    sys.exit(app.exec_())  # and execute the app


if __name__ == '__main__':  # if we're running file directly and not importing it
    main()  # run the main function