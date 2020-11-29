import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel


class Window(QMainWindow):
    def __init__(self, db_name):
        super(Window, self).__init__()
        uic.loadUi('main.ui', self)

        self.label.hide()
        self.label_2.hide()
        self.db, self.model = None, None
        self.init_database(db_name)

    def init_database(self, db_name):
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName(db_name)
        self.db.open()
        self.model = QSqlTableModel(self, self.db)
        self.model.setTable('sorts')
        self.model.select()
        self.tableView.setModel(self.model)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Window('coffee.sqlite')
    wnd.show()
    sys.exit(app.exec())