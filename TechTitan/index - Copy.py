from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
import sys
from PyQt5.uic import loadUi
import os
from os import path



dic ={"admin":'1234','Mido':"2009","Ahmed":"2009","Hamza":"2012"}
class Loginapp(QMainWindow):
    def __init__(self, widget, parent=None):
        super(Loginapp, self).__init__(parent)
        QMainWindow.__init__(self)
        loadUi("login.ui", self) 
        self.widget = widget  # Store the widget (QStackedWidget) reference here
        self.lineEdit_pass.setEchoMode(QLineEdit.Password)
        # self.pushButton_login.clicked.connect(self.gotonewwindow)
        self.pushButton_login.clicked.connect(self.validate)
        self.pushButton.clicked.connect(self.go_to_creatacc)

    def validate(self):
        if (self.lineEdit_email.text() in dic):
            if (self.lineEdit_pass.text() == dic[self.lineEdit_email.text()]):        
                    self.go_to_mainapp()

    def go_to_mainapp(self):
        window2 = mainapp(self.widget)
        self.widget.addWidget(window2)  # Use the stored widget reference
        self.widget.setCurrentWidget(window2)  # Change the page
        self.widget.setFixedWidth(600)# resize the stack
        self.widget.setFixedHeight(705)# resize the stack
    def go_to_creatacc(self):
        window3 = creatapp(self.widget)
        self.widget.addWidget(window3)  # Use the stored widget reference
        self.widget.setCurrentIndex(1)  # Change the page
        self.widget.setFixedWidth(1143)
        self.widget.setFixedHeight(924)

class mainapp(QMainWindow):
    def __init__(self,widget, parent=None):
        super(mainapp, self).__init__(parent)
        QMainWindow.__init__(self)
        loadUi("welcomeonly.ui", self) 
        self.widget = widget
        self.Ticket.clicked.connect(self.gototicketes)
        self.shop_8.clicked.connect(self.gotoshop)

    def gototicketes(self):
        witck = ticketes(self.widget)
        self.widget.addWidget(witck)  # Use the stored widget reference
        self.widget.setCurrentWidget(witck)  # Change the page
        self.widget.setFixedWidth(961)
        self.widget.setFixedHeight(719)

    def gotoshop(self):
        wshop = shop(self.widget)
        self.widget.addWidget(wshop)  # Use the stored widget reference
        self.widget.setCurrentWidget(wshop)  # Change the page
        self.widget.setFixedWidth(707)
        self.widget.setFixedHeight(844)

         
class creatapp(QMainWindow):
    def __init__(self,widget, parent=None):
        super(creatapp, self).__init__(parent)
        QMainWindow.__init__(self)
        loadUi("creat acount.ui", self)
        self.widget =widget
        self.pushButton_sub.clicked.connect(self.subbut)
        self.lineEdit_Password.setEchoMode(QLineEdit.Password)
        self.lineEdit_passw.setEchoMode(QLineEdit.Password)
    def subbut(self):
        if (self.lineEdit_Password.text() == self.lineEdit_passw.text()):
            dic[self.lineEdit_Email.text()] = self.lineEdit_Password.text()
            self.backlog()
    def backlog(self):
        self.widget.setCurrentIndex(0)
        self.widget.setFixedWidth(1100)
        self.widget.setFixedHeight(800)

class ticketes(QMainWindow):
    def __init__(self,widget, parent=None):
        super(ticketes, self).__init__(parent)
        QMainWindow.__init__(self)
        loadUi("TICKTES_only.ui", self)
        self.widget =widget
        self.Back.clicked.connect(self.goback)


    def goback(self):
        self.widget.setCurrentIndex(self.widget.currentIndex())  # Change the page
        self.widget.setFixedWidth(600)# resize the stack
        self.widget.setFixedHeight(705)# resize the stac


class shop(QMainWindow):
    def __init__(self,widget, parent=None):
        super(shop, self).__init__(parent)
        QMainWindow.__init__(self)
        loadUi("shop.ui", self)
        self.widget =widget
        self.Back.clicked.connect(self.goback)


    def goback(self):
        self.widget.setCurrentIndex(self.widget.currentIndex())  # Change the page
        self.widget.setFixedWidth(707)# resize the stack
        self.widget.setFixedHeight(844)# resize the stac


def main():
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()  # Create the QStackedWidget
    window = Loginapp(widget)  # Pass the widget instance to Loginapp
    widget.addWidget(window)
    window.setFixedWidth(1100)
    window.setFixedHeight(800)
    widget.show()
    app.exec_()


if __name__ == '__main__':
    main()
