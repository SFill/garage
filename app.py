
import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets, QtPrintSupport, QtGui, QtCore

# config
from config import mysql_config

# forms
from func.forms import loginform

#func
from func.avto import Avto
from func.driver import Driver
from func.route import Route
from func.user import User
import test



#mysql api
import mysqlx.protobuf.mysqlx_crud_pb2
import mysqlx
# date
from _datetime import datetime



class LoginForm(QtWidgets.QMainWindow, loginform.Ui_LoginForm ):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.app=None
        self.admin=False
        self.moder=False
        self.driver=True

        self.pushButton.clicked.connect(self.verify_login_and_password)


    def verify_login_and_password(self):
        login = self.LoginEdit.text()
        password = self.PasswordEdit.text()
        try:
            self.connection = mysqlx.get_session(mysql_config)
        except Exception as e:
            return
        id_driver = None

        if login=='director' and password=='director':
            self.admin=True
        else:
            query = "Select * from garage.user where login=\"{0}\" and password=\"{1}\";".format(login, password)
            try:
                result=self.connection.sql(query).execute().fetch_one()
                if result is None:
                   return
                if result[1]==2:
                    self.moder=True
                else:
                    id_driver=result[0]

            except Exception as e:
                print(e)
                return
            finally:
                self.connection.close()


        if self.app is None:
            self.app = MyApp(admin=self.admin,
                             moder=self.moder,
                             login=login,
                             id_driver=id_driver
                             )
        self.app.show()
        self.close()


class MyApp(
    Avto,
    Driver,
    Route,
    User,
    QtWidgets.QMainWindow,
    test.Ui_MainWindow
    ):

    def __init__(self,admin=False,moder=False,login='user',id_driver=None):
        super().__init__()
        self.setupUi(self)
        self.session = None
        self.admin_mode=admin
        self.moder_mode=moder
        self.id_driver=id_driver
        self.login=login
        self.search_form=None
        self
        self._load_data_from_db()


        # buttons avto
        if self.admin_mode or self.moder_mode:
            self.AvtoCreateButton.clicked.connect(self.avto_create)
            self.AvtoDeleteButton.clicked.connect(self.avto_delete)
            self.AvtoUpdateButton.clicked.connect(self.avto_update)
            self.AvtoPrintButton.clicked.connect(self.avto_print)
        else:
            self.AvtoCreateButton.setEnabled(False)
            self.AvtoDeleteButton.setEnabled(False)
            self.AvtoUpdateButton.setEnabled(False)
            self.AvtoPrintButton.setEnabled(False)

        # buttons driver
        if self.admin_mode or self.moder_mode:
            self.DriverCreateButton.clicked.connect(self.driver_create)
            self.DriverDeleteButton.clicked.connect(self.driver_delete)
            self.DriverUpdateButton.clicked.connect(self.driver_update)
            self.DriverPrintButton.clicked.connect(self.driver_print)
        else:
            self.DriverCreateButton.setEnabled(False)
            self.DriverDeleteButton.setEnabled(False)
            self.DriverUpdateButton.setEnabled(False)
            self.DriverPrintButton.setEnabled(False)

        # buttons route
        if self.admin_mode or self.moder_mode:
            self.RouteCreateButton.clicked.connect(self.route_create)
            self.RouteDeleteButton.clicked.connect(self.route_delete)
            self.RouteUpdateButton.clicked.connect(self.route_update)
            self.RoutePrintButton.clicked.connect(self.route_print)
        else:
            self.RouteCreateButton.setEnabled(False)
            self.RouteDeleteButton.setEnabled(False)
            self.RouteUpdateButton.setEnabled(False)
            self.RoutePrintButton.setEnabled(False)

        # search
        if self.admin_mode:
            self.UserSearchButton.clicked.connect(lambda: self.search_onSubmit(self.tableWidget_4))
        else:
            self.UserSearchButton.setEnabled(False)

        if self.admin_mode or self.moder_mode:
            self.DriverSearchButton.clicked.connect(lambda: self.search_onSubmit(self.tableWidget_2))
            self.AvtoSearchButton.clicked.connect(lambda: self.search_onSubmit(self.tableWidget))
            self.UserSearchButton.clicked.connect(lambda: self.search_onSubmit(self.tableWidget_4))
        else:
            self.DriverSearchButton.setEnabled(False)
            self.AvtoSearchButton.setEnabled(False)
        self.RouteSearchButton.clicked.connect(lambda: self.search_onSubmit(self.tableWidget_3))



        # buttons user
        if self.admin_mode:
            self.UserCreateButton.clicked.connect(self.user_create)
            self.UserDeleteButton.clicked.connect(self.user_delete)
            self.UserUpdateButton.clicked.connect(self.user_update)

        else:
            self.UserCreateButton.setEnabled(False)
            self.UserDeleteButton.setEnabled(False)
            self.UserUpdateButton.setEnabled(False)


    def _load_data_from_db(self):
        self.session = mysqlx.get_session(mysql_config)
        self.a = datetime.today().strftime("%b %d %Y %H:%M")

        if self.admin_mode or self.moder_mode:
            try:
                self.result = self.session.sql('Select mark,number,Date(date),id from garage.avto order by id;').execute().fetch_all()
            except Exception as e:
                return
            for i,row_data in enumerate(self.result):
                self.tableWidget.insertRow(i)
                for j, data in enumerate(row_data):
                    if j == 2:
                        try:
                            data = data.year
                        except Exception as e:
                            continue
                    self.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(data)))


        if self.admin_mode or self.moder_mode:
            self.result = self.session.sql('Select * from garage.driver;').execute().fetch_all()
            for i, row_data in enumerate(self.result):
                self.tableWidget_2.insertRow(i)
                for j, data in enumerate(row_data):
                    self.tableWidget_2.setItem(i, j, QtWidgets.QTableWidgetItem(str(data)))

        query = """
                           Select
                               r.start,
                               r.finish,
                               r.plane,
                               r.success,
                               r.client,
                               r.id_avto,
                               d.name,
                               r.id_driver,
                               r.id
                           from 
                               garage.route r 
                           inner join 
                               garage.driver d 
                           on 
                               r.id_driver=d.id
                           inner join 
                               garage.avto a 
                           on 
                               r.id_avto=a.id 
                            """

        if not (self.admin_mode or self.moder_mode):
            query+=' where r.id_driver = {}'.format(self.id_driver)

        query+=" order by r.id"

        try:
            self.result = self.session.sql(query).execute().fetch_all()
        except Exception as e:
            pass
        for i, row_data in enumerate(self.result):
            self.tableWidget_3.insertRow(i)
            for j, data in enumerate(row_data):
                self.tableWidget_3.setItem(i, j, QtWidgets.QTableWidgetItem(str(data)))

        if self.admin_mode:
            try:
                self.result = self.session.sql(
                    """
                    Select u.id, p.name,u.login,u.password,u.name from garage.user u 
                    inner join garage.position p on p.id=u.id_position order by u.id;
                    """
                ).execute().fetch_all()
            except Exception as e:
                print(e)
            for i, row_data in enumerate(self.result):
                self.tableWidget_4.insertRow(i)
                for j, data in enumerate(row_data):
                    self.tableWidget_4.setItem(i, j, QtWidgets.QTableWidgetItem(str(data)))

        self.session.close()



def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    translator = QtCore.QTranslator(app)
    locale = QtCore.QLocale.system().name()
    path = QtCore.QLibraryInfo.location(QtCore.QLibraryInfo.TranslationsPath)
    translator.load('qt_%s' % locale, path)
    app.installTranslator(translator)
    login = LoginForm()
    login.show()

    app.exec_()

if __name__ == '__main__':
    main()
