import re

import mysqlx
from PyQt5 import QtWidgets
from datetime import datetime, date as dt_date

from PyQt5.QtWidgets import QMessageBox

from config import mysql_config
from func.forms import avtoform
from func.msg import MsgForm
from func.report import make_report


class AvtoForm(QtWidgets.QMainWindow, avtoform.Ui_AvtoForm,):
    def __init__(self,pre_exit=None, insert=False,obj_out=None):
        super().__init__()
        self.setupUi(self)
        self.SaveButton.clicked.connect(self.save_to_db)
        self.insert = insert
        self.pre_exit=pre_exit
        self.obj_out = obj_out

    def validate_fields(self):
        date = self.DateEdit.text().strip()
        id = self.IdEdit.text().strip()
        znak = self.NumberEdit.text().strip()
        valid = True

        try:
            date = dt_date(int(date),1,1)
            if (date < datetime(1970, 1, 1, 0, 0).date()) or date> datetime.today().date():
                valid = False
            if str(int(id)) != id:
                valid = False
            if len(znak)!=6 or re.match(r'[abekmnopctyx]\d{3}[abekmnopctyx]{2}',znak) is None :
                valid = False

        except Exception:
            valid = False
        return valid

    def save_to_db(self):
        if not self.validate_fields():
            self.dialog = MsgForm("Поля не прошли проверки")
            return
        connection = mysqlx.get_session(mysql_config)
        msg="Сохранено"
        query=""
        if self.insert:
            query = "Insert into garage.avto values(\"{0}\",\"{1}\", \"{2}\" ,{3})".format(
                self.MarkEdit.text(),
                self.NumberEdit.text(),
                str(dt_date(int(self.DateEdit.text()), 1, 1)),
                self.IdEdit.text()
            )
        else:
            try:
                query = "Update garage.avto set mark=\"{0}\", number=\"{1}\", date=\"{2}\" where id={3}".format(
                    self.MarkEdit.text(),
                    self.NumberEdit.text(),
                    str(dt_date(int(self.DateEdit.text()),1,1)),
                    self.IdEdit.text()
                )
            except Exception as e:
                print(e)

        try:
            connection.sql(query).execute()
        except Exception as e:
            msg="Ошибка сохранения"
        finally:
            connection.close()

        self.dialog = MsgForm(msg)
        if self.pre_exit is not None:
            self.pre_exit(self,self.obj_out)
        if self.insert:
            self.insert=False

    def fill_fields(self, *args, **kwargs):
        self.MarkEdit.setText(kwargs['mark'])
        self.DateEdit.setText(kwargs['date'])
        self.NumberEdit.setText(kwargs['number'])
        self.IdEdit.setText(kwargs['id'])

    def fill_field(self,field):
        return self.__getattribute__(field)


class Avto():
    def avto_create(self):
        self.window = AvtoForm(insert=True, pre_exit=self.avto_update_pre_exit, obj_out=self.tableWidget)
        try:
            new_id = int(self.tableWidget.item(
                self.tableWidget.rowCount()-1, 3
            ).text())+1
        except:
            new_id = 0
        self.window.fill_field("IdEdit").setText(str(new_id))
        self.tableWidget.insertRow(self.tableWidget.rowCount())
        self.tableWidget.setItem( self.tableWidget.rowCount()-1, 3, QtWidgets.QTableWidgetItem(str(new_id)))
        self.window.show()

    def avto_update(self):
        selected_row = self.tableWidget.currentItem()
        if selected_row ==None:
            self.dialog = MsgForm("Выбирите строку в таблице")
            # self.dialog.show()
            return
        selected_row = selected_row.row()
        self.window = AvtoForm(pre_exit=self.avto_update_pre_exit, obj_out=self.tableWidget)
        self.window.fill_fields(
            mark=self.tableWidget.item(selected_row,0).text(),
            number=self.tableWidget.item(selected_row,1).text(),
            date=self.tableWidget.item(selected_row,2).text(),
            id=self.tableWidget.item(selected_row,3).text()
        )
        self.window.show()

    def avto_update_pre_exit(self, obj_in, obj_out):
        id = obj_in.IdEdit.text()
        number = obj_in.NumberEdit.text(),
        date = obj_in.DateEdit.text(),
        mark = obj_in.MarkEdit.text(),
        try:
            for i in range(obj_out.rowCount()):
                if id == obj_out.item(i,3).text():
                    obj_out.setItem(i,0, QtWidgets.QTableWidgetItem(mark[0]))
                    obj_out.setItem(i,1, QtWidgets.QTableWidgetItem(number[0]))
                    obj_out.setItem(i,2, QtWidgets.QTableWidgetItem(date[0]))
        except Exception as e:
            return

    def avto_delete(self):
        reply = QMessageBox.question(self, 'Удалить!',
                                     'Вы действительно хотите удалить запись?',
                                     QMessageBox.Yes | QMessageBox.No)
        if reply != QMessageBox.Yes:
            return
        selected_row = self.tableWidget.currentItem().row()
        if selected_row == None:
            self.dialog = MsgForm("Выбирите строку в таблице")
            return
        id = self.tableWidget.item(selected_row, 3).text()
        self.session = mysqlx.get_session(mysql_config)
        query = "Delete from garage.avto where id={}".format(id)
        self.session.sql(query).execute()
        self.session.close()
        self.tableWidget.removeRow(selected_row)

    def avto_print(self):
        f = 'report_avto' + datetime.now().strftime("%Y%m%d-%H%M%S") + '.xlsx'
        headers = ['марка', 'номер', 'год выпуска']
        table = self.tableWidget
        make_report(f, headers, table)
