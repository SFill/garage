from PyQt5 import QtWidgets

from func.forms import msgform


class MsgForm(QtWidgets.QDialog,msgform.Ui_Dialog):
    def __init__(self, msg=None):
        super().__init__()
        self.setupUi(self)
        self.msg.setText(msg)
        self.okButton.clicked.connect(self.close)
        self.exec()
