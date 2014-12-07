#!/usr/bin/python
# -*- coding: utf-8 -*-
 
from PyQt4 import QtGui, QtCore
import sys
 
import ImageViewerUI
 
class ImageViewer(QtGui.QMainWindow, ImageViewerUI.Ui_MainWindow): 
    def __init__(self, parent=None):
        super(ImageViewer, self).__init__(parent)
        self.setupUi(self)
        self.connectActions()
 
    def connectActions(self):
        self.actionQuit.triggered.connect(QtGui.qApp.quit)
        self.actionOpen.triggered.connect(self.openImage)
 
    def openImage(self):
        fileName = QtGui.QFileDialog.getOpenFileName(
                        self,
                        "Ouvrir un fichier d'image",
                        QtCore.QDir.homePath(),
                        "Fichiers d'image (*.jpg, *.jpeg, *.gif, *.png)"
                    )
        if fileName:
            self.imageLabel.setPixmap(QtGui.QPixmap(fileName))
 
    def main(self):
        self.show()
 
if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    imageViewer = ImageViewer()
    imageViewer.main()
    app.exec_()
