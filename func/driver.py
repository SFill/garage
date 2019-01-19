from decimal import Decimal

import mysqlx
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from config import mysql_config
from func.forms import driverform
from func.msg import MsgForm

class DriverForm(QtWidgets.QMainWindow, driverform.Ui_DriverForm ):
    def __init__(self,pre_exit=None, insert=False,obj_out=None):
        super().__init__()
        self.setupUi(self)
        self.insert = insert
        self.pre_exit = pre_exit
        self.obj_out = obj_out
        self.SaveButton.clicked.connect(self.save_to_db)

    def validate_fields(self):
        name = self.NameEdit.text().strip()
        old =  self.OldEdit.text().strip()
        exp =  self.ExperienceEdit.text().strip()
        payment = self.PaymentEdit.text()
        id = self.IdEdit.text().strip()
        valid = True

        try:
            if (len(name)> 40) or bool(re.search(r'\d', name)):
                valid = False
            if str(int(old)) != old:
                valid = False
            Decimal(payment)
            if (int(exp)>70) or int(old)<int(exp)+14:
                valid=False
            if str(int(id)) != id:
                valid = False
        except Exception:
            valid = False
        return valid

    def save_to_db(self):
        if not self.validate_fields():
            self.dialog = MsgForm("Поля не прошли проверки")
            return

        msg = "Сохранено"
        connection = mysqlx.get_session(mysql_config)
        if self.insert:
            query = "Insert into garage.driver values(\"{0}\",\"{1}\", \"{2}\" ,{3},{4})".format(
                self.NameEdit.text(),
                self.OldEdit.text(),
                self.ExperienceEdit.text(),
                self.PaymentEdit.text(),
                self.IdEdit.text()
            )
        else:
            query = "Update garage.driver set name=\"{0}\", old=\"{1}\", experience=\"{2}\", payment=\"{3}\" where id={4}".format(
                self.NameEdit.text(),
                self.OldEdit.text(),
                self.ExperienceEdit.text(),
                self.PaymentEdit.text(),
                self.IdEdit.text()
            )
        try:
            connection.sql(query).execute()

        except:
            msg = "Ошибка сохранения"
        finally:
            connection.close()

        self.dialog = MsgForm(msg)

        if self.pre_exit is not None:
            self.pre_exit(self, self.obj_out)
        if self.insert:
            self.insert = False

    def fill_fields(self, *args, **kwargs):
        self.NameEdit.setText(kwargs['name'])
        self.OldEdit.setText(kwargs['old'])
        self.ExperienceEdit.setText(kwargs['experience'])
        self.PaymentEdit.setText(kwargs['payment'])
        self.IdEdit.setText(kwargs['id'])

    def fill_field(self,field):
        return self.__getattribute__(field)


class Driver():
    def driver_create(self):
        self.window = DriverForm(insert=True, pre_exit=self.driver_update_pre_exit, obj_out=self.tableWidget_2)
        try:
            new_id = int(self.tableWidget_2.item(
                self.tableWidget_2.rowCount()-1, 4
            ).text())+1
        except Exception as e:
            new_id = 0
        self.window.fill_field("IdEdit").setText(str(new_id))
        self.tableWidget_2.insertRow(self.tableWidget_2.rowCount())
        self.tableWidget_2.setItem( self.tableWidget_2.rowCount()-1, 4, QtWidgets.QTableWidgetItem(str(new_id)))
        self.window.show()

    def driver_update(self):
        selected_row = self.tableWidget_2.currentItem()
        if selected_row == None:
            self.dialog = MsgForm("Выбирите строку в таблице")
            # self.dialog.show()
            return
        selected_row = selected_row.row()
        self.window = DriverForm(pre_exit=self.driver_update_pre_exit, obj_out=self.tableWidget_2)
        self.window.fill_fields(
            name=self.tableWidget_2.item(selected_row, 0).text(),
            old=self.tableWidget_2.item(selected_row, 1).text(),
            experience=self.tableWidget_2.item(selected_row, 2).text(),
            payment=self.tableWidget_2.item(selected_row, 3).text(),
            id=self.tableWidget_2.item(selected_row, 4).text()
        )
        self.window.show()

    def driver_delete(self):
        reply = QMessageBox.question(self, 'Удалить!',
                                     'Вы действительно хотите удалить запись?',
                                     QMessageBox.Yes | QMessageBox.No)
        if reply != QMessageBox.Yes:
            return
        selected_row = self.tableWidget_2.currentItem()
        if selected_row == None:
            self.dialog = MsgForm("Выбирите строку в таблице")
            return
        selected_row = selected_row.row()
        id = self.tableWidget_2.item(selected_row, 4).text()
        self.session = mysqlx.get_session(mysql_config)
        query = "Delete from garage.driver where id={}".format(id)
        try:
            self.session.sql(query).execute()
        except Exception as e:
            print(e)
            return
        self.session.close()
        self.tableWidget_2.removeRow(selected_row)

    def driver_update_pre_exit(self, obj_in, obj_out):
        name = obj_in.NameEdit.text(),
        old = obj_in.OldEdit.text(),
        experience = obj_in.ExperienceEdit.text(),
        payment = obj_in.PaymentEdit.text(),
        id = obj_in.IdEdit.text()
        try:
            for i in range(obj_out.rowCount()):
                if id == obj_out.item(i,4).text():
                    obj_out.setItem(i,0, QtWidgets.QTableWidgetItem(name[0]))
                    obj_out.setItem(i,1, QtWidgets.QTableWidgetItem(old[0]))
                    obj_out.setItem(i,2, QtWidgets.QTableWidgetItem(experience[0]))
                    obj_out.setItem(i, 3, QtWidgets.QTableWidgetItem(payment[0]))
                    obj_out.setItem(i, 4, QtWidgets.QTableWidgetItem(id[0]))
        except Exception as e:
            return
