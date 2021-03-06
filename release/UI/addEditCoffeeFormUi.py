from PyQt5.QtCore import QSize, QMetaObject, QCoreApplication, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QGridLayout, QLabel, QLineEdit, QComboBox,
                             QPlainTextEdit, QPushButton, QSizePolicy)


class Ui_Form:
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(440, 380)
        font = QFont()
        font.setPointSize(10)
        Form.setFont(font)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.price_line = QLineEdit(Form)
        self.price_line.setObjectName("price_line")
        self.gridLayout.addWidget(self.price_line, 4, 1, 1, 1)
        self.size_line = QLineEdit(Form)
        self.size_line.setObjectName("size_line")
        self.gridLayout.addWidget(self.size_line, 5, 1, 1, 1)
        self.sort_line = QLineEdit(Form)
        self.sort_line.setObjectName("sort_line")
        self.gridLayout.addWidget(self.sort_line, 0, 1, 1, 1)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.condition_box = QComboBox(Form)
        self.condition_box.setObjectName("condition_box")
        self.gridLayout.addWidget(self.condition_box, 2, 1, 1, 1)
        self.taste_text = QPlainTextEdit(Form)
        self.taste_text.setObjectName("taste_text")
        self.gridLayout.addWidget(self.taste_text, 3, 1, 1, 1)
        self.roasting_box = QComboBox(Form)
        self.roasting_box.setObjectName("roasting_box")
        self.gridLayout.addWidget(self.roasting_box, 1, 1, 1, 1)
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 6, 1, 1, 1, Qt.AlignRight)
        self.status_label = QLabel(Form)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.status_label.sizePolicy().hasHeightForWidth())
        self.status_label.setSizePolicy(sizePolicy)
        self.status_label.setMaximumSize(QSize(136, 16777215))
        font = QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.status_label.setFont(font)
        self.status_label.setText("")
        self.status_label.setWordWrap(True)
        self.status_label.setObjectName("status_label")
        self.gridLayout.addWidget(self.status_label, 6, 0, 1, 1)

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Добавление/изменение элемента"))
        self.label_5.setText(_translate("Form", "Цена"))
        self.label_3.setText(_translate("Form", "Состояние"))
        self.label_2.setText(_translate("Form", "Степень обжарки"))
        self.label.setText(_translate("Form", "Название сорта"))
        self.label_6.setText(_translate("Form", "Объём упаковки"))
        self.label_4.setText(_translate("Form", "Описание вкуса"))
        self.pushButton.setText(_translate("Form", "Подтвердить"))