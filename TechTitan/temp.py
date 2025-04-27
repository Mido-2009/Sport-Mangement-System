from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
import sys

from PyQt5.uic import loadUiType
import urllib.request
#import pafy
#import humanize

import os
from os import path


FORM_CLASS_ = loadUiType(path.join(path.dirname(__file__),'login.ui'))

class mainapp(QMainWindow,FORM_CLASS_):
    def __init__(self,parent=None):
        
        super(mainapp,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.input_handler)
        self.lineEdit_Password.setEchoMode(QLineEdit.Password)
        self.lineEdit_passw.setEchoMode(QLineEdit.Password)
    def input_handler(self):
        saveEmail=self.lineEdit_Email.text()
        savepassword=self.lineEdit_Password.text()
        self.lineEdit_Email.setText("")
        self.lineEdit_Password.setText("")
        savepass=self.lineEdit_passw.text()
        self.lineEdit_passw.setText("")
        print(saveEmail)
        print(savepassword)
        print(savepass)
        




def main():
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()  
    window = mainapp(widget)  
    widget.addWidget(window)
    widget.setFixedWidth(1000)
    widget.setFixedHeight(1000)
    
    widget.show()
    app.exec_()

if __name__ == '__main__':
    main()
