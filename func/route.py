import mysqlx
from PyQt5 import QtWidgets, QtPrintSupport, QtGui
from PyQt5.QtWidgets import QMessageBox, QAbstractButton

from config import mysql_config
from func.forms import routeform
from func.msg import MsgForm


class RouteForm(QtWidgets.QMainWindow, routeform.Ui_RouteForm ):
    def __init__(self,pre_exit=None, insert=False,obj_out=None):
        super().__init__()
        self.setupUi(self)
        self.drivers = {}
        self.avtos = {}
        self.insert = insert
        self.pre_exit = pre_exit
        self.obj_out=obj_out
        self._fill_drivers_and_avtos()
        self.SaveButton.clicked.connect(self.save_to_db)

    def validate_fields(self):
        start = self.StartEdit.text().strip()
        finish =  self.FinishEdit.text().strip()
        plan = self.PlanTextEdit.toPlainText().strip()
        success =  1 if self.SuccessCheck.isChecked() else 0
        client  = self.ClientEdit.text().strip()
        id =  self.IdEdit.text().strip()
        avto = self.avtos[self.AvtoComboBox.currentText()],
        driver = self.drivers[self.DriverComboBox.currentText()]
        valid = True
        try:
            if len(start)> 40:
                valid = False
            if len(finish)> 40:
                valid = False
        except Exception:
            valid=False
        return valid

    def _fill_drivers_and_avtos(self):
        session = mysqlx.get_session(mysql_config)
        query_to_driver_table = "Select name,id from garage.driver ORDER by id;"
        result=session.sql(query_to_driver_table).execute().fetch_all()
        for row_data in result:
            self.DriverComboBox.addItem(row_data[0])
            self.drivers[row_data[0]] = row_data[1]

        query_to_avto_table = "Select mark,number,id from garage.avto;"
        result = session.sql( query_to_avto_table).execute().fetch_all()

        for row_data in result:
            avto_present=row_data[0]+'('+row_data[1]+')'
            self.avtos[avto_present] = row_data[2]
            self.AvtoComboBox.addItem(avto_present)
        session.close()

    def save_to_db(self):
        msg = "Сохранено"
        connection = mysqlx.get_session(mysql_config)

        if not self.validate_fields():
            self.dialog = MsgForm("Поля не прошли проверки")
            return

        try:
            if self.insert:
                query = "Insert into garage.route values(\"{0}\",\"{1}\", \"{2}\" ,{3},\"{4}\",{5},{6},{7})".format(
                    self.StartEdit.text(),
                    self.FinishEdit.text(),
                    self.PlanTextEdit.toPlainText(),
                    1 if self.SuccessCheck.isChecked() else 0,
                    self.ClientEdit.text(),
                    self.avtos[self.AvtoComboBox.currentText()],
                    self.drivers[self.DriverComboBox.currentText()],
                    self.IdEdit.text()
                )
            else:
                try:
                    query = "Update garage.route set  start=\"{0}\", finish=\"{1}\", plane=\"{2}\", " \
                            "success={3}, client=\"{4}\", id_driver={5},id_avto={6} where id={7}"\
                    .format(
                    self.StartEdit.text(),
                    self.FinishEdit.text(),
                    self.PlanTextEdit.toPlainText(),
                    1 if self.SuccessCheck.isChecked() else 0,
                    self.ClientEdit.text(),
                    self.drivers[self.DriverComboBox.currentText()],
                    self.avtos[self.AvtoComboBox.currentText()],

                    self.IdEdit.text()
                    )
                except Exception as e:
                    raise Exception

            connection.sql(query).execute()
        except Exception as e:
            msg = "Ошибка сохранения"
            print(e)

        finally:
            connection.close()
        self.dialog = MsgForm(msg)

        if self.pre_exit is not None:
            self.pre_exit(self, self.obj_out)
        if self.insert:
            self.insert = False

    def fill_fields(self, *args, **kwargs):
        self.IdEdit.setText(kwargs['id'])
        self.StartEdit.setText(kwargs['start'])
        self.FinishEdit.setText(kwargs['finish'])
        self.ClientEdit.setText(kwargs['client'])
        self.PlanTextEdit.insertPlainText(kwargs['plane'])
        self.SuccessCheck.setChecked(kwargs['success'])

        # try:
        #     self.AvtoComboBox.setCurrentIndex(int(kwargs["id_avto"])-1)
        #     self.DriverComboBox.setCurrentIndex(int(kwargs["id_driver"])-1)
        # except Exception as e:
        #     pass

    def fill_field(self,field):
        return self.__getattribute__(field)


class Route():
    def route_create(self):
        self.window = RouteForm(insert=True, pre_exit=self.route_update_pre_exit, obj_out=self.tableWidget_3)
        try:
            new_id = int(self.tableWidget_3.item(
                self.tableWidget_3.rowCount() - 1, 8
            ).text()) + 1
        except:
            new_id = 0
        self.window.fill_field("IdEdit").setText(str(new_id))
        self.tableWidget_3.insertRow(self.tableWidget_3.rowCount())
        self.tableWidget_3.setItem(self.tableWidget_3.rowCount() - 1, 8, QtWidgets.QTableWidgetItem(str(new_id)))
        self.window.show()

    def route_update(self):
        selected_row = self.tableWidget_3.currentItem()
        if selected_row == None:
            self.dialog = MsgForm("Выбирите строку в таблице")
            return
        selected_row = selected_row.row()
        self.window = RouteForm(pre_exit=self.route_update_pre_exit, obj_out=self.tableWidget_3)
        self.window.fill_fields(
            start=self.tableWidget_3.item(selected_row, 0).text(),
            finish=self.tableWidget_3.item(selected_row, 1).text(),
            plane=self.tableWidget_3.item(selected_row, 2).text(),
            success=self.tableWidget_3.item(selected_row, 3).text() in ['1'],
            client=self.tableWidget_3.item(selected_row, 4).text(),
            id_avto=self.tableWidget_3.item(selected_row, 5).text(),
            id_driver=self.tableWidget_3.item(selected_row, 7).text(),
            id=self.tableWidget_3.item(selected_row, 8).text(),
        )
        self.window.show()

    def route_delete(self):
        reply = QMessageBox.question(self, 'Удалить!',
                             'Вы действительно хотите удалить запись?',
                             QMessageBox.Yes | QMessageBox.No)
        if reply != QMessageBox.Yes:
            return
        selected_row = self.tableWidget_3.currentItem()
        if selected_row == None:
            self.dialog = MsgForm("Выбирите строку в таблице")
            return
        selected_row = selected_row.row()
        id = self.tableWidget_3.item(selected_row, 7).text()
        self.session = mysqlx.get_session(mysql_config)
        query = "Delete from garage.route where id={}".format(id)
        try:
            self.session.sql(query).execute()
        except Exception as e:
            print(e)
            return
        self.session.close()
        self.tableWidget_3.removeRow(selected_row)

    def route_update_pre_exit(self, obj_in, obj_out):
        id = obj_in.IdEdit.text()
        start = obj_in.StartEdit.text(),
        finish = obj_in.FinishEdit.text(),
        plane = obj_in.PlanTextEdit.toPlainText(),
        success = 1 if obj_in.SuccessCheck.isChecked() else 0
        client = obj_in.ClientEdit.text(),
        id_avto = obj_in.avtos[obj_in.AvtoComboBox.currentText()]
        id_driver = obj_in.drivers[obj_in.DriverComboBox.currentText()]
        driver_name = obj_in.DriverComboBox.currentText()

        try:
            for i in range(obj_out.rowCount()):
                if id == obj_out.item(i, 8).text():
                    obj_out.setItem(i, 0, QtWidgets.QTableWidgetItem(start[0]))
                    obj_out.setItem(i, 1, QtWidgets.QTableWidgetItem(finish[0]))
                    obj_out.setItem(i, 2, QtWidgets.QTableWidgetItem(plane[0]))
                    obj_out.setItem(i, 3, QtWidgets.QTableWidgetItem(str(success)))
                    obj_out.setItem(i, 4, QtWidgets.QTableWidgetItem(client[0]))
                    obj_out.setItem(i, 5, QtWidgets.QTableWidgetItem(str(id_avto)))
                    obj_out.setItem(i, 6, QtWidgets.QTableWidgetItem(str(driver_name)))
                    obj_out.setItem(i, 7, QtWidgets.QTableWidgetItem(str(id_driver)))
                    obj_out.setItem(i, 8, QtWidgets.QTableWidgetItem(id))
        except Exception as e:
            print(e)

    def route_print(self):
        printer = QtPrintSupport.QPrinter()
        # Create painter
        painter = QtGui.QPainter()
        # Start painter
        painter.begin(printer)
        # Grab a widget you want to print
        screen = self.tableWidget_3.grab()
        # Draw grabbed pixmap
        painter.drawPixmap(10, 10, screen)
        # End painting
        painter.end()
