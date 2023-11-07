import sys
from PyQt5 import QtCore, QtWidgets


class AdmDbPanelUI(object):
    def __init__(self):
        self.tabl = None
        self.groupBox = None
        self.add_row_button = None
        self.choose_tabl = None
        self.cancel_button = None
        self.choose_row = None
        self.del_row_button = None
        self.confirm_button = None
        self.central_widget = None
        self.horizontalLayout = None
        self.verticalLayout_2 = None
        self.verticalLayout_4 = None
        self.label_choose_tabl = None
        self.show_table_button = None
        self.rows_action_label = None
        self.export_word_button = None
        self.horizontalLayout_2 = None
        self.change_table_label = None
        self.choose_row_label = None
        self.app = QtWidgets.QApplication(sys.argv)

    def setupUi(self, MainScreenUI):
        MainScreenUI.resize(1115, 600)
        MainScreenUI.setMinimumSize(QtCore.QSize(910, 620))

        self.central_widget = QtWidgets.QWidget(MainScreenUI)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.central_widget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()

        self.tabl = QtWidgets.QTableWidget(self.central_widget)
        self.tabl.setMinimumSize(QtCore.QSize(670, 599))
        self.tabl.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.horizontalLayout.addWidget(self.tabl)

        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.label_choose_tabl = QtWidgets.QLabel(self.central_widget)
        self.label_choose_tabl.setMinimumSize(QtCore.QSize(170, 15))
        self.label_choose_tabl.setMaximumSize(QtCore.QSize(170, 15))
        self.verticalLayout_2.addWidget(self.label_choose_tabl, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        self.choose_tabl = QtWidgets.QComboBox(self.central_widget)
        self.choose_tabl.setMinimumSize(QtCore.QSize(220, 30))
        self.choose_tabl.setMaximumSize(QtCore.QSize(220, 30))
        self.verticalLayout_2.addWidget(self.choose_tabl, 0, QtCore.Qt.AlignHCenter)

        self.groupBox = QtWidgets.QGroupBox(self.central_widget)
        self.groupBox.setMinimumSize(QtCore.QSize(220, 15))
        self.groupBox.setMaximumSize(QtCore.QSize(220, 1000000))
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox)

        self.choose_row_label = QtWidgets.QLabel(self.groupBox)
        self.choose_row_label.setMinimumSize(QtCore.QSize(200, 15))
        self.choose_row_label.setMaximumSize(QtCore.QSize(200, 15))
        self.verticalLayout_4.addWidget(self.choose_row_label)

        self.choose_row = QtWidgets.QComboBox(self.groupBox)
        self.choose_row.setMinimumSize(QtCore.QSize(200, 30))
        self.choose_row.setMaximumSize(QtCore.QSize(200, 30))
        self.choose_row.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.verticalLayout_4.addWidget(self.choose_row)

        self.rows_action_label = QtWidgets.QLabel(self.groupBox)
        self.rows_action_label.setMinimumSize(QtCore.QSize(195, 15))
        self.rows_action_label.setMaximumSize(QtCore.QSize(200, 15))
        self.verticalLayout_4.addWidget(self.rows_action_label)

        self.add_row_button = QtWidgets.QPushButton(self.groupBox)
        self.add_row_button.setMinimumSize(QtCore.QSize(200, 30))
        self.add_row_button.setMaximumSize(QtCore.QSize(200, 30))
        self.verticalLayout_4.addWidget(self.add_row_button)

        self.del_row_button = QtWidgets.QPushButton(self.groupBox)
        self.del_row_button.setMinimumSize(QtCore.QSize(200, 30))
        self.del_row_button.setMaximumSize(QtCore.QSize(200, 30))
        self.verticalLayout_4.addWidget(self.del_row_button)

        self.change_table_label = QtWidgets.QLabel(self.groupBox)
        self.change_table_label.setMinimumSize(QtCore.QSize(195, 15))
        self.change_table_label.setMaximumSize(QtCore.QSize(200, 15))
        self.verticalLayout_4.addWidget(self.change_table_label)

        self.confirm_button = QtWidgets.QPushButton(self.groupBox)
        self.confirm_button.setMinimumSize(QtCore.QSize(200, 30))
        self.confirm_button.setMaximumSize(QtCore.QSize(200, 30))
        self.verticalLayout_4.addWidget(self.confirm_button)

        self.cancel_button = QtWidgets.QPushButton(self.groupBox)
        self.cancel_button.setMinimumSize(QtCore.QSize(200, 30))
        self.cancel_button.setMaximumSize(QtCore.QSize(200, 30))
        self.verticalLayout_4.addWidget(self.cancel_button)

        self.verticalLayout_2.addWidget(self.groupBox, 0, QtCore.Qt.AlignHCenter)

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)

        self.export_word_button = QtWidgets.QPushButton(self.central_widget)
        self.export_word_button.setMinimumSize(QtCore.QSize(220, 30))
        self.export_word_button.setMaximumSize(QtCore.QSize(220, 30))
        self.verticalLayout_2.addWidget(self.export_word_button, 0, QtCore.Qt.AlignHCenter)

        self.show_table_button = QtWidgets.QPushButton(self.central_widget)
        self.show_table_button.setMinimumSize(QtCore.QSize(220, 30))
        self.show_table_button.setMaximumSize(QtCore.QSize(220, 30))
        self.verticalLayout_2.addWidget(self.show_table_button, 0, QtCore.Qt.AlignHCenter)

        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        MainScreenUI.setCentralWidget(self.central_widget)

        self.translateUi(MainScreenUI)
        QtCore.QMetaObject.connectSlotsByName(MainScreenUI)

    def translateUi(self, MainScreenUI):
        self.choose_tabl.addItem("metadata")
        self.choose_tabl.addItem("person")
        self.choose_tabl.addItem("subject")
        self.choose_tabl.addItem("students_group")
        self.choose_tabl.addItem("student")
        self.choose_tabl.addItem("teacher")
        self.choose_tabl.addItem("class")
        self.choose_tabl.addItem("class_teacher")
        self.choose_tabl.addItem("class_group")
        self.choose_tabl.addItem("subject_teacher")
        self.choose_tabl.addItem("attendance")

        _translate = QtCore.QCoreApplication.translate
        MainScreenUI.setWindowTitle(_translate("AdmDbPanelUI", "Панель администратора"))
        self.groupBox.setTitle(_translate("AdmDbPanelUI", "Изменение таблицы"))
        self.del_row_button.setText(_translate("AdmDbPanelUI", "Удалить строку"))
        self.add_row_button.setText(_translate("AdmDbPanelUI", "Добавить строку"))
        self.cancel_button.setText(_translate("AdmDbPanelUI", "Отменить изменение"))
        self.show_table_button.setText(_translate("AdmDbPanelUI", "Вывести таблицу"))
        self.confirm_button.setText(_translate("AdmDbPanelUI", "Подтвердить изменение"))
        self.export_word_button.setText(_translate("AdmDbPanelUI", "Экспортировать БД в Word"))
        self.label_choose_tabl.setText(_translate("AdmDbPanelUI", "Выберите таблицу из списка"))
        self.rows_action_label.setText(_translate("AdmDbPanelUI", "<html><head/><body><p align=\"center\">Действия со строками</p></body></html>"))
        self.change_table_label.setText(_translate("AdmDbPanelUI", "<html><head/><body><p align=\"center\">Подтверждение/отмена</p></body></html>"))
        self.choose_row_label.setText(_translate("AdmDbPanelUI", "<html><head/><body><p align=\"center\">Выберите строку таблицы</p></body></html>"))
