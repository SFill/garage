# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Admin\PycharmProjects\garage\routeform.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RouteForm(object):
    def setupUi(self, RouteForm):
        RouteForm.setObjectName("RouteForm")
        RouteForm.resize(562, 440)
        self.centralwidget = QtWidgets.QWidget(RouteForm)
        self.centralwidget.setObjectName("centralwidget")
        self.StartEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.StartEdit.setGeometry(QtCore.QRect(140, 70, 113, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.StartEdit.setFont(font)
        self.StartEdit.setObjectName("StartEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(46, 70, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(56, 110, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.FinishEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.FinishEdit.setGeometry(QtCore.QRect(140, 110, 113, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.FinishEdit.setFont(font)
        self.FinishEdit.setObjectName("FinishEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(300, 30, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.SaveButton = QtWidgets.QPushButton(self.centralwidget)
        self.SaveButton.setGeometry(QtCore.QRect(280, 220, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.SaveButton.setFont(font)
        self.SaveButton.setObjectName("SaveButton")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(36, 160, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.ClientEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.ClientEdit.setGeometry(QtCore.QRect(140, 160, 113, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ClientEdit.setFont(font)
        self.ClientEdit.setObjectName("ClientEdit")
        self.SuccessCheck = QtWidgets.QCheckBox(self.centralwidget)
        self.SuccessCheck.setGeometry(QtCore.QRect(120, 220, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.SuccessCheck.setFont(font)
        self.SuccessCheck.setObjectName("SuccessCheck")
        self.PlanTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.PlanTextEdit.setGeometry(QtCore.QRect(280, 70, 161, 121))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.PlanTextEdit.setFont(font)
        self.PlanTextEdit.setObjectName("PlanTextEdit")
        self.IdEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.IdEdit.setGeometry(QtCore.QRect(140, 20, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.IdEdit.setFont(font)
        self.IdEdit.setText("")
        self.IdEdit.setReadOnly(True)
        self.IdEdit.setObjectName("IdEdit")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(90, 20, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.DriverComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.DriverComboBox.setGeometry(QtCore.QRect(60, 310, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.DriverComboBox.setFont(font)
        self.DriverComboBox.setObjectName("DriverComboBox")
        self.AvtoComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.AvtoComboBox.setGeometry(QtCore.QRect(280, 310, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.AvtoComboBox.setFont(font)
        self.AvtoComboBox.setObjectName("AvtoComboBox")
        RouteForm.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(RouteForm)
        self.statusbar.setObjectName("statusbar")
        RouteForm.setStatusBar(self.statusbar)

        self.retranslateUi(RouteForm)
        QtCore.QMetaObject.connectSlotsByName(RouteForm)

    def retranslateUi(self, RouteForm):
        _translate = QtCore.QCoreApplication.translate
        RouteForm.setWindowTitle(_translate("RouteForm", "Водитель"))
        self.label.setText(_translate("RouteForm", "Начало"))
        self.label_2.setText(_translate("RouteForm", "Конец"))
        self.label_3.setText(_translate("RouteForm", "План выезда"))
        self.SaveButton.setText(_translate("RouteForm", "Сохранить"))
        self.label_4.setText(_translate("RouteForm", "Заказчик"))
        self.SuccessCheck.setText(_translate("RouteForm", "Исполнение"))
        self.label_5.setText(_translate("RouteForm", "id"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RouteForm = QtWidgets.QMainWindow()
    ui = Ui_RouteForm()
    ui.setupUi(RouteForm)
    RouteForm.show()
    sys.exit(app.exec_())

