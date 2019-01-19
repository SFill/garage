# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Admin\PycharmProjects\garage\searchform.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SearchForm(object):
    def setupUi(self, SearchForm):
        SearchForm.setObjectName("SearchForm")
        SearchForm.resize(293, 190)
        self.centralwidget = QtWidgets.QWidget(SearchForm)
        self.centralwidget.setObjectName("centralwidget")
        self.IndexEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.IndexEdit.setGeometry(QtCore.QRect(30, 60, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.IndexEdit.setFont(font)
        self.IndexEdit.setObjectName("IndexEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.SearchButton = QtWidgets.QPushButton(self.centralwidget)
        self.SearchButton.setGeometry(QtCore.QRect(29, 100, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.SearchButton.setFont(font)
        self.SearchButton.setStyleSheet("")
        self.SearchButton.setObjectName("SearchButton")
        SearchForm.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SearchForm)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 293, 21))
        self.menubar.setObjectName("menubar")
        SearchForm.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SearchForm)
        self.statusbar.setObjectName("statusbar")
        SearchForm.setStatusBar(self.statusbar)

        self.retranslateUi(SearchForm)
        QtCore.QMetaObject.connectSlotsByName(SearchForm)

    def retranslateUi(self, SearchForm):
        _translate = QtCore.QCoreApplication.translate
        SearchForm.setWindowTitle(_translate("SearchForm", "MainWindow"))
        self.label.setText(_translate("SearchForm", "Идентификатор"))
        self.SearchButton.setText(_translate("SearchForm", "Поиск"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SearchForm = QtWidgets.QMainWindow()
    ui = Ui_SearchForm()
    ui.setupUi(SearchForm)
    SearchForm.show()
    sys.exit(app.exec_())

