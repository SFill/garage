from PyQt5 import QtWidgets

from func.forms import searchform


class SearchForm(QtWidgets.QMainWindow, searchform.Ui_SearchForm):
    def __init__(self,table):
        super().__init__()
        self.setupUi(self)
        self.SearchButton.clicked.connect(self._search)
        self.table = table
        self.define_table()

    def define_table(self):
        if self.table.objectName() == "tableWidget":
            self.label.setText("Учетный номер")
            self.search_col = 3
        elif self.table.objectName() == "tableWidget_2":
            self.label.setText("Номер водителя")
            self.search_col = 4
        elif self.table.objectName() == "tableWidget_3":
            self.label.setText("ID маршрута")
            self.search_col = 8
        elif self.table.objectName() == "tableWidget_4":
            self.label.setText("ID пользователя")
            self.search_col = 0
        else:
            pass

    def _search(self):
        try:
            for i in range(self.table.rowCount()):
                txt = self.table.item(i,self.search_col).text()
                if txt == self.IndexEdit.text():
                    self.table.selectRow(i)
                    self.close()
        except Exception as e:
            pass


class Search():
    def search_onSubmit(self, table):
        self.search_form = SearchForm(table)
        self.search_form.show()
