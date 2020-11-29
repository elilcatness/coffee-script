import sys
from PyQt5 import uic
from PyQt5.QtCore import QModelIndex
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QComboBox,
                             QLineEdit, QPlainTextEdit, QAbstractItemView)
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery


class AddEditForm(QWidget):
    def __init__(self, parent, insert_type, field_id=None):
        super(AddEditForm, self).__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        window_title = 'Добавление элемента' if insert_type == 'add' else 'Изменение элемента'
        self.setWindowTitle(window_title)
        self.insert_type, self.parent = insert_type, parent
        self.field_id = field_id
        self.fill_boxes()
        if insert_type == 'edit':
            self.fill_fields()
        self.sort_line.setFocus()

        self.pushButton.clicked.connect(self.insert_item)

    def fill_boxes(self):
        db = self.parent.get_db()
        query = QSqlQuery('SELECT name FROM roastings', db)
        while query.next():
            self.roasting_box.addItem(query.value(0))
        query = QSqlQuery('SELECT name FROM conditions', db)
        while query.next():
            self.condition_box.addItem(query.value(0))

    def fill_fields(self):
        query = QSqlQuery("""SELECT sorts.sort, roastings.name, conditions.name, 
                             sorts.taste, sorts.price, sorts.size
                             FROM roastings, conditions JOIN sorts
                             ON roastings.id = sorts.roasting
                             AND conditions.id = sorts.condition
                             WHERE sorts.id = %d""" % self.field_id, self.parent.get_db())
        query.next()
        fields = [self.sort_line, self.roasting_box, self.condition_box,
                  self.taste_text, self.price_line, self.size_line]
        for i, val in enumerate([query.value(i) for i in range(6)]):
            field = fields[i]
            val = str(val)
            methods = {QLineEdit: 'setText', QComboBox: 'setCurrentText',
                       QPlainTextEdit: 'setPlainText'}
            eval('field.%s("%s")' % (methods[field.__class__], val))

    def insert_item(self):
        self.status_label.setText('')
        fields = [self.sort_line.text(), self.taste_text.toPlainText(),
                  self.price_line.text(), self.size_line.text()]
        if not all(map(lambda x: x, fields)):
            self.status_label.setText('Поля должны быть заполнены')
            return
        sort, taste, price, size = fields
        int_values = [price, size]
        for i in range(len(int_values)):
            try:
                int_values[i] = int(int_values[i])
            except ValueError:
                field_name = 'цены' if i == 0 else 'объёма'
                self.status_label.setText('Неверный формат %s' % field_name)
                return
        price, size = int_values
        roasting, condition = self.roasting_box.currentText(), self.condition_box.currentText()

        db = self.parent.get_db()

        query = QSqlQuery('SELECT id FROM roastings WHERE name = ?', db)
        query.addBindValue(roasting)
        query.exec()
        query.next()
        roasting_id = query.value(0)

        query = QSqlQuery('SELECT id FROM conditions WHERE name = ?', db)
        query.addBindValue(condition)
        query.exec()
        query.next()
        condition_id = query.value(0)

        values = (sort, roasting_id, condition_id, taste, price, size)
        raw_query = ("""INSERT INTO sorts (id, sort, roasting, condition, taste, price, size)
                        VALUES (?, ?, ?, ?, ?, ?, ?)""" if self.insert_type == 'add' else
                     """UPDATE sorts SET
                        sort = ?,
                        roasting = ?,
                        condition = ?,
                        taste = ?,
                        price = ?,
                        size = ?
                        WHERE id = ?""")
        query = QSqlQuery(raw_query, db)
        if self.insert_type == 'add':
            get_count_query = QSqlQuery('SELECT COUNT (*) FROM sorts')
            get_count_query.next()
            field_id = get_count_query.value(0) + 1
            query.addBindValue(field_id)
        for val in values:
            query.addBindValue(val)
        if self.insert_type == 'edit':
            query.addBindValue(self.field_id)
        query.exec()
        self.parent.init_database()
        self.destroy()


class Window(QMainWindow):
    def __init__(self, db_name):
        super(Window, self).__init__()
        uic.loadUi('main.ui', self)

        self.label.hide()
        self.db_name, self.db, self.model = db_name, None, None
        self.init_database()

        self.form = None
        self.add_btn.clicked.connect(self.add_field)
        self.tableView.doubleClicked.connect(self.edit_field)

    def get_db(self):
        return self.db

    def get_model(self):
        return self.model

    def get_table(self):
        return self.tableView

    def init_database(self):
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName(self.db_name)
        self.db.open()
        self.model = QSqlTableModel(self, self.db)
        self.model.setQuery(QSqlQuery("""SELECT sorts.sort AS 'Сорт', roastings.name AS 'Обжарка',
                                                conditions.name AS 'Состояние', 
                                                sorts.taste AS 'Вкус', sorts.price AS 'Цена, руб', 
                                                sorts.size AS 'Объём, грамм'
                                                FROM roastings, conditions JOIN sorts
                                                ON roastings.id = sorts.roasting
                                                AND conditions.id = sorts.condition""", self.db))
        self.model.select()
        self.tableView.setModel(self.model)
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def add_field(self):
        self.form = AddEditForm(self, 'add')
        self.form.show()

    def edit_field(self, index: QModelIndex):
        self.form = AddEditForm(self, 'edit', index.row() + 1)
        self.form.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Window('coffee.sqlite')
    wnd.show()
    sys.exit(app.exec())