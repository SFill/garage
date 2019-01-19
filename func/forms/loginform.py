# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Admin\PycharmProjects\garage\loginform.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LoginForm(object):
    def setupUi(self, LoginForm):
        LoginForm.setObjectName("LoginForm")
        LoginForm.resize(206, 234)
        self.centralwidget = QtWidgets.QWidget(LoginForm)
        self.centralwidget.setObjectName("centralwidget")
        self.LoginEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.LoginEdit.setGeometry(QtCore.QRect(6, 60, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.LoginEdit.setFont(font)
        self.LoginEdit.setObjectName("LoginEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(76, 20, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.PasswordEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.PasswordEdit.setGeometry(QtCore.QRect(6, 140, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.PasswordEdit.setFont(font)
        self.PasswordEdit.setText("")
        self.PasswordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.PasswordEdit.setObjectName("PasswordEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(66, 100, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 180, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        LoginForm.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(LoginForm)
        self.statusbar.setObjectName("statusbar")
        LoginForm.setStatusBar(self.statusbar)

        self.retranslateUi(LoginForm)
        QtCore.QMetaObject.connectSlotsByName(LoginForm)

    def retranslateUi(self, LoginForm):
        _translate = QtCore.QCoreApplication.translate
        LoginForm.setWindowTitle(_translate("LoginForm", "Login"))
        self.label.setText(_translate("LoginForm", "логин"))
        self.label_2.setText(_translate("LoginForm", "пароль"))
        self.pushButton.setText(_translate("LoginForm", "войти"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginForm = QtWidgets.QMainWindow()
    ui = Ui_LoginForm()
    ui.setupUi(LoginForm)
    LoginForm.show()
    sys.exit(app.exec_())

