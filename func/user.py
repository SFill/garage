import re

import mysqlx
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from config import mysql_config
from func.forms import userform
from func.msg import MsgForm


class UserForm(QtWidgets.QMainWindow, userform.Ui_UserForm):
    def __init__(self, pre_exit=None, insert=False, obj_out=None):
        super().__init__()
        self.setupUi(self)
        self.insert = insert
        self.pre_exit = pre_exit
        self.obj_out = obj_out
        self.poss={}
        self.fill_poss()
        self.SaveButton.clicked.connect(self.save_to_db)

    def validate_fields(self):
        login = self.LoginEdit.text().strip()
        password = self.PasswordEdit.text().strip()
        name =  self.NameEdit.text().strip()
        poss = self.poss[self.PosComboBox.currentText()]
        id =  self.IdEdit.text().strip()
        valid = True

        try:
            if len(login)> 20:
                valid = False
            if (len(name)> 40) or bool(re.search(r'\d', name)) :
                valid = False
            if bool(re.search(r'[=!*&?]', password)):
                valid = False
            if int(poss) != poss:
                valid = False
            if str(int(id)) != id:
                valid = False
        except Exception:
            valid=False
        return valid



    def fill_poss(self):
        session = mysqlx.get_session(mysql_config)
        query_to_driver_table = "Select name,id from garage.position;"
        result = session.sql(query_to_driver_table).execute().fetch_all()
        for row_data in result:
            self.PosComboBox.addItem(row_data[0])
            self.poss[row_data[0]] = row_data[1]
        session.close()

    def save_to_db(self):
        connection = mysqlx.get_session(mysql_config)
        msg="Сохранено"
        if not self.validate_fields():
            self.dialog = MsgForm("Поля не прошли проверки")
            return

        try:
            if self.insert:
                query = "Insert into garage.user values({0},{1},\"{2}\", \"{3}\" ,\"{4}\")".format(
                    self.IdEdit.text(),
                    self.poss[self.PosComboBox.currentText()],
                    self.LoginEdit.text(),
                    self.PasswordEdit.text(),
                    self.NameEdit.text(),

                )
            else:
                try:
                    query = "Update garage.user set  login=\"{0}\", password=\"{1}\", name=\"{2}\", id_position={3} where id={4}".format(
                        self.LoginEdit.text(),
                        self.PasswordEdit.text(),
                        self.NameEdit.text(),
                        self.poss[self.PosComboBox.currentText()],
                        self.IdEdit.text(),

                    )
                except Exception as e:
                    raise Exception

            connection.sql(query).execute()
        except Exception as e:
            msg = "Ошибка сохранения"
        finally:
            connection.close()
        self.dialog = MsgForm(msg)
        if self.pre_exit is not None:
            self.pre_exit(self, self.obj_out)
        if self.insert:
            self.insert = False

    def fill_fields(self, *args, **kwargs):
        try:
            self.IdEdit.setText(kwargs['id'])
            self.LoginEdit.setText(kwargs['login'])
            self.PasswordEdit.setText(kwargs['password'])
            self.NameEdit.setText(kwargs['name'])
            self.PosComboBox.setCurrentIndex(int(kwargs['id_position'])-1)
        except Exception as e:
            print(e)
            return

    def fill_field(self, field):
        return self.__getattribute__(field)


class User():
    def user_create(self):
        self.window = UserForm(insert=True, pre_exit=self.user_update_pre_exit, obj_out=self.tableWidget_4)
        try:
            new_id = int(self.tableWidget_4.item(
                self.tableWidget_4.rowCount() - 1, 0
            ).text()) + 1
        except:
            new_id = 0
        self.window.fill_field("IdEdit").setText(str(new_id))
        self.tableWidget_4.insertRow(self.tableWidget_4.rowCount())
        self.tableWidget_4.setItem(self.tableWidget_4.rowCount() - 1, 0, QtWidgets.QTableWidgetItem(str(new_id)))
        self.window.show()

    def user_update(self):
        selected_row = self.tableWidget_4.currentItem()
        if selected_row == None:
            self.dialog = MsgForm("Выбирите строку в таблице")
            return
        selected_row = selected_row.row()

        self.window = UserForm(pre_exit=self.user_update_pre_exit, obj_out=self.tableWidget_4)
        self.window.fill_fields(
            id=self.tableWidget_4.item(selected_row, 0).text(),
            id_position=2 if self.tableWidget_4.item(selected_row, 1).text() == 'диспетчер' else 1,
            login=self.tableWidget_4.item(selected_row, 2).text(),
            password=self.tableWidget_4.item(selected_row, 3).text(),
            name=self.tableWidget_4.item(selected_row, 4).text(),

        )
        self.window.show()

    def user_delete(self):
        reply = QMessageBox.question(self, 'Удалить!',
                                     'Вы действительно хотите удалить запись?',
                                     QMessageBox.Yes | QMessageBox.No)
        if reply != QMessageBox.Yes:
            return
        selected_row = self.tableWidget_4.currentItem()
        if selected_row == None:
            self.dialog = MsgForm("Выбирите строку в таблице")
            return
        selected_row = selected_row.row()
        id = self.tableWidget_4.item(selected_row, 0).text()
        self.session = mysqlx.get_session(mysql_config)
        query = "Delete from garage.user where id={}".format(id)
        try:
            self.session.sql(query).execute()
        except Exception as e:
            print(e)
            return
        self.session.close()
        self.tableWidget_4.removeRow(selected_row)

    def user_update_pre_exit(self, obj_in, obj_out):
        id = obj_in.IdEdit.text()
        id_pos = obj_in.poss[obj_in.PosComboBox.currentText()]
        name = obj_in.NameEdit.text(),
        login = obj_in.LoginEdit.text(),
        password = obj_in.PasswordEdit.text(),

        try:
            for i in range(obj_out.rowCount()):
                if id == obj_out.item(i, 0).text():
                    obj_out.setItem(i, 0, QtWidgets.QTableWidgetItem(id))
                    obj_out.setItem(i, 1, QtWidgets.QTableWidgetItem(obj_in.PosComboBox.currentText()))
                    obj_out.setItem(i, 2, QtWidgets.QTableWidgetItem(login[0]))
                    obj_out.setItem(i, 3, QtWidgets.QTableWidgetItem(password[0]))
                    obj_out.setItem(i, 4, QtWidgets.QTableWidgetItem(name[0]))
        except Exception as e:
            print(e)
            return
