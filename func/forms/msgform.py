# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Admin\PycharmProjects\garage\msg.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(283, 201)
        self.okButton = QtWidgets.QPushButton(Dialog)
        self.okButton.setGeometry(QtCore.QRect(50, 100, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.okButton.setFont(font)
        self.okButton.setObjectName("okButton")
        self.msg = QtWidgets.QLabel(Dialog)
        self.msg.setGeometry(QtCore.QRect(20, 20, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.msg.setFont(font)
        self.msg.setObjectName("msg")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Сообщение"))
        self.okButton.setText(_translate("Dialog", "ОК"))
        self.msg.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt;\">TextLabel</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

