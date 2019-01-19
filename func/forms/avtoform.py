# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Admin\PycharmProjects\garage\avtoform.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AvtoForm(object):
    def setupUi(self, AvtoForm):
        AvtoForm.setObjectName("AvtoForm")
        AvtoForm.resize(573, 206)
        self.centralwidget = QtWidgets.QWidget(AvtoForm)
        self.centralwidget.setObjectName("centralwidget")
        self.MarkEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.MarkEdit.setGeometry(QtCore.QRect(160, 70, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.MarkEdit.setFont(font)
        self.MarkEdit.setObjectName("MarkEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(66, 70, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(66, 110, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.NumberEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.NumberEdit.setGeometry(QtCore.QRect(160, 110, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.NumberEdit.setFont(font)
        self.NumberEdit.setObjectName("NumberEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(310, 30, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.DateEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.DateEdit.setGeometry(QtCore.QRect(430, 30, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.DateEdit.setFont(font)
        self.DateEdit.setObjectName("DateEdit")
        self.SaveButton = QtWidgets.QPushButton(self.centralwidget)
        self.SaveButton.setGeometry(QtCore.QRect(310, 70, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.SaveButton.setFont(font)
        self.SaveButton.setObjectName("SaveButton")
        self.IdEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.IdEdit.setGeometry(QtCore.QRect(160, 30, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.IdEdit.setFont(font)
        self.IdEdit.setText("")
        self.IdEdit.setReadOnly(True)
        self.IdEdit.setObjectName("IdEdit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(110, 30, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        AvtoForm.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(AvtoForm)
        self.statusbar.setObjectName("statusbar")
        AvtoForm.setStatusBar(self.statusbar)

        self.retranslateUi(AvtoForm)
        QtCore.QMetaObject.connectSlotsByName(AvtoForm)

    def retranslateUi(self, AvtoForm):
        _translate = QtCore.QCoreApplication.translate
        AvtoForm.setWindowTitle(_translate("AvtoForm", "Автомобиль"))
        self.label.setText(_translate("AvtoForm", "Марка"))
        self.label_2.setText(_translate("AvtoForm", "Номер"))
        self.label_3.setText(_translate("AvtoForm", "Год выпуска"))
        self.SaveButton.setText(_translate("AvtoForm", "Сохранить"))
        self.label_4.setText(_translate("AvtoForm", "id"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AvtoForm = QtWidgets.QMainWindow()
    ui = Ui_AvtoForm()
    ui.setupUi(AvtoForm)
    AvtoForm.show()
    sys.exit(app.exec_())

