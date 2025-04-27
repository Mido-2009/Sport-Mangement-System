from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
import sys
from PyQt5.uic import loadUi
import os
from os import path

save_username=""
Total_price=0 
total=0
vip =0 
high=0
normal=0
av_vip=100
av_high=250
av_normal=1000
expen=0
dic ={"admin":'1234','Mido':"2009","Ahmed":"2009","Hamza":"2012"}
class Loginapp(QMainWindow):
    
    def __init__(self, widget, parent=None):
        super(Loginapp, self).__init__(parent)
        QMainWindow.__init__(self)
        loadUi("login.ui", self) 
        self.setWindowTitle("Login Page")
        self.widget = widget  # Store the widget (QStackedWidget) reference here
        self.lineEdit_pass.setEchoMode(QLineEdit.Password)
        self.lineEdit_pass.returnPressed.connect(self.pushButton_login.click)
        self.lineEdit_email.returnPressed.connect(self.pushButton_login.click)
        self.pushButton_login.clicked.connect(self.validate)
        self.pushButton.clicked.connect(self.go_to_creatacc)

    


    def validate(self):
        if (self.lineEdit_email.text() in dic):
            if (self.lineEdit_pass.text() == dic[self.lineEdit_email.text()]):  
                global save_username
                save_username=self.lineEdit_email.text()
                self.lineEdit_email.setText("")
                self.lineEdit_pass.setText("")
                self.go_to_mainapp()
            else:
                self.password_incorect()
        else :
            self.username_incorect()
    

    def go_to_mainapp(self):
        window2 = mainapp(self.widget)
        self.widget.addWidget(window2)  # Use the stored widget reference
        self.widget.setCurrentWidget(window2)  # Change the page
        self.widget.setFixedWidth(600)# resize the stack
        self.widget.setFixedHeight(991)# resize the stack


    def go_to_creatacc(self):
        window3 = creatapp(self.widget)
        self.widget.addWidget(window3)  # Use the stored widget reference
        self.widget.setCurrentIndex(1)  # Change the page
        self.widget.setFixedWidth(1143)
        self.widget.setFixedHeight(750)


    def password_incorect(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setText("Password incorect")
        msg.setWindowTitle("Error ")
        msg.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        retval = msg.exec()


    def username_incorect(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setText("Username incorect")
        msg.setWindowTitle("Error ")
        msg.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        retval = msg.exec()

class mainapp(QMainWindow):
    def __init__(self,widget, parent=None):
        super(mainapp, self).__init__(parent)
        QMainWindow.__init__(self)
        loadUi("welcomeonly.ui", self) 
        self.widget = widget
        self.setWindowTitle("Welcome Page")
        self.Ticket.clicked.connect(self.gototicketes)
        self.shop_8.clicked.connect(self.gotoshop)
        global save_username
        self.user_welcome.setText("Welcome "+save_username)
        self.log_out.clicked.connect(self.golog_out)
        self.Enter.clicked.connect(self.go_to_expen)


    def go_to_expen(self):
        global expen
        global Total_price 
        expen+=int(self.lineEdit.text())
        self.label_79.setText("Total Expense: "+str(expen))
        self.lineEdit.setText("")
        Total_price-=expen
        self.label.setText("Total Price: "+str(Total_price)) 

    def golog_out(self):
        self.widget.setCurrentIndex(0)
        self.widget.setFixedWidth(1100)
        self.widget.setFixedHeight(800)

    def gototicketes(self):
        witck = ticketes(self.widget, self)  # Pass self as main_window
        self.widget.addWidget(witck)
        self.widget.setCurrentWidget(witck)
        self.widget.setFixedWidth(961)
        self.widget.setFixedHeight(719)

    def gotoshop(self):
        wshop = shop(self.widget, self)  # Pass self as main_window
        self.widget.addWidget(wshop)
        self.widget.setCurrentWidget(wshop)
        self.widget.setFixedWidth(707)
        self.widget.setFixedHeight(655)
        
class creatapp(QMainWindow):
    def __init__(self,widget, parent=None):
        super(creatapp, self).__init__(parent)
        QMainWindow.__init__(self)
        loadUi("creat acount.ui", self)                     
        self.widget =widget
        self.setWindowTitle("Create Account Page")
        self.pushButton_sub.clicked.connect(self.subbut)
        self.lineEdit_Password.setEchoMode(QLineEdit.Password)
        self.lineEdit_passw.setEchoMode(QLineEdit.Password)
        self.lineEdit_passw.returnPressed.connect(self.pushButton_sub.click)

    def subbut(self):
        if (self.lineEdit_Password.text() == self.lineEdit_passw.text()):
            # add new user to dic l
            dic[self.lineEdit_Email.text()] = self.lineEdit_Password.text()
            self.lineEdit_Email.setText("")
            self.lineEdit_Password.setText("")
            self.lineEdit_passw.setText("")
            self.backlog()
        else:
            self.password_incorect()    
    def backlog(self):
        self.widget.setCurrentIndex(0)
        self.widget.setFixedWidth(1100)
        self.widget.setFixedHeight(800)
    
    def password_incorect(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setText("Not Confirmed Password")
        msg.setWindowTitle("Error ")
        msg.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        retval = msg.exec()

class ticketes(QMainWindow):
    def __init__(self, widget, main_window, parent=None):
        super(ticketes, self).__init__(parent)
        QMainWindow.__init__(self)
        loadUi("TICKTES_only.ui", self)
        self.widget = widget
        global av_vip
        self.main_window = main_window  # Save the mainapp instance
        self.Back.clicked.connect(self.goback)
        self.spinBox_vip.setMinimum(1)
        self.spinBox_vip.setMaximum(av_vip)
        self.spinBox_vip_2.setMinimum(1)
        self.spinBox_vip_2.setMaximum(av_high)
        self.spinBox_vip_3.setMinimum(1)
        self.spinBox_vip_3.setMaximum(av_normal)
        self.label_100.setText(str(av_vip))
        self.label_250.setText(str(av_high))
        self.label_1000.setText(str(av_normal))
        self.pushButton_bvi_2.clicked.connect(self.connect_vip)
        self.pushButton_hip_2.clicked.connect(self.connect_high)
        self.pushButton_nor_2.clicked.connect(self.connect_normal)
    def goback(self):
        self.widget.setCurrentWidget(self.main_window)  # Switch back to mainapp
        self.widget.setFixedWidth(600)
        self.widget.setFixedHeight(705)

    def connect_vip(self):
        global Total_price
        global vip
        global av_vip
        global total
        vip +=self.spinBox_vip.value()
        Total_price +=self.spinBox_vip.value()*300
        av_vip -=int(self.spinBox_vip.value())
        self.main_window.label_71.setText("VIP: " + str(vip))
        self.main_window.label.setText("Total Price: "+str(Total_price))
        self.label_100.setText(str(av_vip))
        total+=vip
        self.main_window.label_2.setText("Total Tickets: "+str(total))

    def connect_high(self):
        global Total_price
        global high
        global av_high
        global total
        high+=self.spinBox_vip_2.value()
        Total_price +=self.spinBox_vip_2.value()*150
        av_high-=int(self.spinBox_vip_2.value())
        self.main_window.label_77.setText("High Class: " + str(high))
        self.main_window.label.setText("Total Price: "+str(Total_price))
        self.label_250.setText(str(av_high))
        total+=high
        self.main_window.label_2.setText("Total Tickets: "+str(total))
    
    def connect_normal(self):
        global Total_price
        global normal
        global av_normal
        global total
        normal+=self.spinBox_vip_3.value()
        Total_price +=self.spinBox_vip_3.value()*75
        av_normal-=int(self.spinBox_vip_3.value())
        self.main_window.label_73.setText("Noraml: " + str(normal))
        self.main_window.label.setText("Total Price: "+str(Total_price))
        self.label_1000.setText(str(av_normal)) 
        total+=normal
        self.main_window.label_2.setText("Total Tickets: "+str(total))
        

class shop(QMainWindow):
    def __init__(self, widget, main_window, parent=None):
        super(shop, self).__init__(parent)
        QMainWindow.__init__(self)
        loadUi("shop.ui", self)
        self.widget = widget
        self.main_window = main_window
        self.Back.clicked.connect(self.goback)
        self.football.clicked.connect(self.addfootball)
        self.naturalgrassfgshoes.clicked.connect(self.addnaturalgrassfgshoes)
        self.sportbags.clicked.connect(self.addsportbags)
        self.sportsweabottles.clicked.connect(self.addsportsweabottles)
        self.trainingshirts.clicked.connect(self.addtrainingshirts)
        self.spinBox.setMinimum(0)
        self.spinBox.setMaximum(100)
        

    def goback(self):
        self.widget.setCurrentWidget(self.main_window)
        self.widget.setFixedWidth(600)
        self.widget.setFixedHeight(705)

    def addfootball(self):
        global Total_price
        Total_price+=self.spinBox.value()*300
        self.main_window.label.setText("Total Price: "+str(Total_price))
    
    def addnaturalgrassfgshoes(self):
        global Total_price
        Total_price+=self.spinBox_3.value()*800
        self.main_window.label.setText("Total Price: "+str(Total_price))

    def addsportbags(self):
        global Total_price
        Total_price+=self.spinBox_2.value()*1500
        self.main_window.label.setText("Total Price: "+str(Total_price))
         
    def addsportsweabottles(self):
        global Total_price
        Total_price+=self.spinBox_7.value()*250
        self.main_window.label.setText("Total Price: "+str(Total_price))

    def addtrainingshirts(self):
        global Total_price
        Total_price+=self.spinBox_4.value()*550
        self.main_window.label.setText("Total Price: "+str(Total_price))



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
