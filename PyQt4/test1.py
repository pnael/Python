#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
import sys


class demowind(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setGeometry(300, 300, 200, 200)
        self.setWindowTitle('Demo window')
        quit = QtGui.QPushButton('Close', self)
        quit.setGeometry(10, 10, 70, 40)
        self.connect(quit, QtCore.SIGNAL('clicked()'), QtGui.qApp, QtCore.SLOT('quit()'))

def main():
    app = QtGui.QApplication(sys.argv)
    myapp = demowind()
    myapp.show()
    sys.exit(app.exec_())


if __name__=="__main__":
    main()
