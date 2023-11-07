import os
import pytz
from datetime import datetime
from dateutil.parser import parse
from PyQt5.QtWidgets import QMainWindow
from db_connection.db_class import DBClass
from interface.adm_db_panel_ui import AdmDbPanelUI
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem


class AdmDbPanel(QMainWindow):
    def __init__(self, parent=None):
        super(AdmDbPanel, self).__init__(parent)
        self.db = DBClass()
        self.checker = True
        self.ui = AdmDbPanelUI()
        self.ui.setupUi(self)
        self.prov = 0
        self.data = []
        self.result = []
        self.columns_names = []

        self.ui.tabl.itemChanged.connect(self.handleItemChanged)
        self.ui.cancel_button.clicked.connect(lambda: self.undo_change())
        self.ui.add_row_button.clicked.connect(lambda: self.add_row_table())
        self.ui.del_row_button.clicked.connect(lambda: self.del_row_table())
        self.ui.show_table_button.clicked.connect(lambda: self.show_table())
        self.ui.export_word_button.clicked.connect(lambda: self.export_db())
        self.ui.confirm_button.clicked.connect(lambda: self.confirm_change())

    # Экспорт БД в Word
    def export_db(self):
        try:
            self.db.create_word_document()
            self.__showMessage("Успех", "Экспорт базы данных в Word завершён.")
        except Exception:
            self.__showMessage("Ошибка", "Экспортировать базу данных в Word не удалось.\nПроверьте, не открыта ли "
                                         "предыдущая версия экспорта.")

    # Вывод таблицы
    def show_table(self):
        self.data.clear()
        self.checker = False
        self.columns_names.clear()
        self.ui.choose_row.clear()
        self.ui.tabl.clearSelection()
        self.result = self.ui.choose_tabl.currentText()
        self.__dataPreparation(table_name=self.result)
        self.ui.tabl.setRowCount(len(self.data))
        self.ui.tabl.setColumnCount(len(self.columns_names))
        self.ui.tabl.setHorizontalHeaderLabels(self.columns_names)

        if len(self.data) == 0:
            return
        i = 0
        for _, form in enumerate(self.data):
            j = 0
            for c in self.columns_names:
                for k, v in vars(form).items():
                    if c == k:
                        self.ui.tabl.setItem(i, j, QTableWidgetItem(str(v)))
                        j += 1
            i += 1
            self.ui.choose_row.addItem(str(i))
        self.ui.tabl.setStyleSheet("selection-color: rgb(255, 0, 127);\n"
                                   "selection-background-color: rgb(85, 255, 127);")
        self.ui.tabl.resizeColumnsToContents()
        self.checker = True

    # Добавление строки
    def add_row_table(self):
        if self.prov == 0:
            self.prov = 1
        if self.result == "metadata":
            current_time = datetime.now(pytz.timezone('Europe/Moscow'))
            tz_offset = current_time.utcoffset().total_seconds()
            tz_hours = int(tz_offset // 3600)
            tz_minutes = int((tz_offset % 3600) // 60)
            tz_str = "{:02d}:{:02d}".format(tz_hours, tz_minutes)
            formatted_timestamp = current_time.strftime('%Y-%m-%d %H:%M:%S') + "+" + tz_str
            self.db.setter.addMetadata(path="", add_date=formatted_timestamp)
        elif self.result == "person":
            self.db.setter.addPerson(name="", meta_id=1)
        elif self.result == "subject":
            self.db.setter.addSubject(name="")
        elif self.result == "students_group":
            self.db.setter.addStudentsGroup(name="")
        elif self.result == "student":
            self.db.setter.addStudent(person_id=1, group_id=1)
        elif self.result == "teacher":
            self.db.setter.addTeacher(work_experience=0, person_id=1)
        elif self.result == "class":
            current_date = datetime.now().date()
            date_str = current_date.strftime("%Y-%m-%d")
            current_time = datetime.now().time()
            time_str = current_time.strftime("%H:%M:%S")
            self.db.setter.addClass(date_class=date_str, start_time=time_str, end_time=time_str, audience="", subject_id=1)
        elif self.result == "class_teacher":
            self.db.setter.addClassTeacher(teacher_id=1, class_id=1)
        elif self.result == "class_group":
            self.db.setter.addClassGroup(group_id=1, class_id=1)
        elif self.result == "subject_teacher":
            self.db.setter.addSubjectTeacher(teacher_id=1, subject_id=1)
        elif self.result == "attendance":
            current_time = datetime.now().time()
            time_str = current_time.strftime("%H:%M:%S")
            self.db.setter.addAttendance(status=True, entry_time=time_str, leave_time=time_str, class_id=1, person_id=1)
        self.show_table()

    # Удаление строки
    def del_row_table(self):
        if self.prov == 0:
            self.prov = 1
        row_num = int(self.ui.choose_row.currentText()) - 1
        if self.result == "metadata":
            self.db.setter.delMetadata(self.data[row_num].id)
        elif self.result == "person":
            self.db.setter.delPerson(self.data[row_num].id)
        elif self.result == "subject":
            self.db.setter.delSubject(self.data[row_num].id)
        elif self.result == "students_group":
            self.db.setter.delStudentsGroup(self.data[row_num].id)
        elif self.result == "student":
            self.db.setter.delStudent(self.data[row_num].id)
        elif self.result == "teacher":
            self.db.setter.delTeacher(self.data[row_num].id)
        elif self.result == "class":
            self.db.setter.delClass(self.data[row_num].id)
        elif self.result == "class_teacher":
            self.db.setter.delClassTeacher(teacher_id=self.data[row_num].teacher_id,
                                           class_id=self.data[row_num].class_id)
        elif self.result == "class_group":
            self.db.setter.delClassGroup(group_id=self.data[row_num].group_id, class_id=self.data[row_num].class_id)
        elif self.result == "subject_teacher":
            self.db.setter.delSubjectTeacher(teacher_id=self.data[row_num].teacher_id,
                                             subject_id=self.data[row_num].subject_id)
        elif self.result == "attendance":
            self.db.setter.delAttendance(self.data[row_num].id)
        self.show_table()

    # Подтвердить изменения
    def confirm_change(self):
        if self.prov != 0:
            self.db.session.commit()
            self.prov = 0
            self.show_table()
            self.__showMessage("Успех", "Вы изменили таблицу")
        else:
            self.__showMessage("Ошибка", "Сначала внесите изменение в таблицу")

    # Отменить изменения
    def undo_change(self):
        if self.prov != 0:
            self.db.session.rollback()
            self.prov = 0
            self.show_table()
            self.__showMessage("Успех", "Вы отменили изменения таблицы")
        else:
            self.__showMessage("Ошибка", "Сначала внесите изменение в таблицу")

    # Изменение данный в ячейке
    def handleItemChanged(self, item):
        if self.checker:
            if (self.result == "class_teacher") or (self.result == "class_group") or (self.result == "subject_teacher"):
                self.__showMessage("Ошибка", "Данные этой таблицы нельзя изменять")
                self.show_table()
                return
            new_value_str = item.text()
            row = item.row()
            col = item.column()
            if self.prov == 0:
                self.prov = 1
            value = self.check_input_data(col, new_value_str)
            if value is None:
                self.show_table()
                return
            self.set_new_value(value, row, col)
            self.show_table()

    # Подготовка данных для таблицы
    def __dataPreparation(self, table_name: str):
        if table_name == "metadata":
            self.data = self.db.getter.getAllMetadata()
            self.columns_names = ['id', 'path', 'add_date']
        elif table_name == "person":
            self.data = self.db.getter.getAllPersons()
            self.columns_names = ['id', 'name', 'meta_id']
        elif table_name == "subject":
            self.data = self.db.getter.getAllSubjects()
            self.columns_names = ['id', 'name']
        elif table_name == "students_group":
            self.data = self.db.getter.getAllStudentsGroup()
            self.columns_names = ['id', 'name']
        elif table_name == "student":
            self.data = self.db.getter.getAllStudents()
            self.columns_names = ['id', 'person_id', 'group_id']
        elif table_name == "teacher":
            self.data = self.db.getter.getAllTeachers()
            self.columns_names = ['id', 'work_experience', 'person_id']
        elif table_name == "class":
            self.data = self.db.getter.getAllClasses()
            self.columns_names = ['id', 'date_class', 'start_time', 'end_time', 'audience', 'subject_id']
        elif table_name == "class_teacher":
            self.data = self.db.getter.getAllClassTeacher()
            self.columns_names = ['teacher_id', 'class_id']
        elif table_name == "class_group":
            self.data = self.db.getter.getAllClassGroup()
            self.columns_names = ['group_id', 'class_id']
        elif table_name == "subject_teacher":
            self.data = self.db.getter.getAllSubjectTeacher()
            self.columns_names = ['teacher_id', 'subject_id']
        elif table_name == "attendance":
            self.data = self.db.getter.getAllAttendance()
            self.columns_names = ['id', 'status', 'entry_time', 'leave_time', 'class_id', 'person_id']

    # Проверка введённых данных
    def check_input_data(self, col: int, new_value_str):
        if self.columns_names[col] == 'id':
            self.__showMessage("Ошибка", "Значение id изменять запрещено.")
            return None
        if self.result == "metadata":
            if self.columns_names[col] == 'path':
                if os.path.exists(new_value_str):
                    return new_value_str
                else:
                    self.__showMessage("Ошибка", "Введите путь к существующей папке с данными.")
            elif self.columns_names[col] == 'add_date':
                try:
                    parse(new_value_str)
                    return new_value_str
                except ValueError:
                    self.__showMessage("Ошибка", "Введите дату и время в соответствующем формате.")

        elif self.result == "person":
            if self.columns_names[col] == 'meta_id':
                try:
                    meta_id = int(new_value_str)
                    if self.db.getter.getMetadata(meta_id) is None:
                        self.__showMessage("Ошибка", "Введите id существующих мета данных.")
                    else:
                        return meta_id
                except ValueError:
                    self.__showMessage("Ошибка", "Введите id в соответствующем формате.")
            else:
                return new_value_str

        elif self.result == "subject":
            return new_value_str

        elif self.result == "students_group":
            return new_value_str

        elif self.result == "student":
            if self.columns_names[col] == 'person_id':
                try:
                    person_id = int(new_value_str)
                    if self.db.getter.getPerson(person_id) is None:
                        self.__showMessage("Ошибка", "Введите id существующего человека.")
                    else:
                        return person_id
                except ValueError:
                    self.__showMessage("Ошибка", "Введите id в соответствующем формате.")
            elif self.columns_names[col] == 'group_id':
                try:
                    group_id = int(new_value_str)
                    if self.db.getter.getStudentsGroup(group_id) is None:
                        self.__showMessage("Ошибка", "Введите id существующей группы.")
                    else:
                        return group_id
                except ValueError:
                    self.__showMessage("Ошибка", "Введите id в соответствующем формате.")

        elif self.result == "teacher":
            if self.columns_names[col] == 'work_experience':
                try:
                    new_value = int(new_value_str)
                    return new_value
                except ValueError:
                    self.__showMessage("Ошибка", "Введите стаж работы в формате целого числа.")
            elif self.columns_names[col] == 'person_id':
                try:
                    person_id = int(new_value_str)
                    if self.db.getter.getPerson(person_id) is None:
                        self.__showMessage("Ошибка", "Введите id существующего человека.")
                    else:
                        return person_id
                except ValueError:
                    self.__showMessage("Ошибка", "Введите id в соответствующем формате.")

        elif self.result == "class":
            if self.columns_names[col] == 'date_class':
                try:
                    datetime.strptime(new_value_str, '%Y-%m-%d')
                    return new_value_str
                except ValueError:
                    self.__showMessage("Ошибка", "Введите дату в соответствующем формате.")
            elif self.columns_names[col] == 'start_time':
                try:
                    datetime.strptime(new_value_str, '%H:%M:%S')
                    return new_value_str
                except ValueError:
                    try:
                        datetime.strptime(new_value_str, '%H:%M')
                        return new_value_str
                    except ValueError:
                        self.__showMessage("Ошибка", "Введите время в соответствующем формате.")
            elif self.columns_names[col] == 'end_time':
                try:
                    datetime.strptime(new_value_str, '%H:%M:%S')
                    return new_value_str
                except ValueError:
                    try:
                        datetime.strptime(new_value_str, '%H:%M')
                        return new_value_str
                    except ValueError:
                        self.__showMessage("Ошибка", "Введите время в соответствующем формате.")
            elif self.columns_names[col] == 'subject_id':
                try:
                    subject_id = int(new_value_str)
                    if self.db.getter.getSubject(subject_id) is None:
                        self.__showMessage("Ошибка", "Введите id существующего предмета.")
                    else:
                        return subject_id
                except ValueError:
                    self.__showMessage("Ошибка", "Введите id в соответствующем формате.")
            else:
                return new_value_str

        elif self.result == "attendance":
            if self.columns_names[col] == 'status':
                if (new_value_str == "True") or (new_value_str == "true"):
                    return True
                elif (new_value_str == "False") or (new_value_str == "false"):
                    return False
                else:
                    self.__showMessage("Ошибка", "Введите статус в следующем формате: \"True\" или \"true\" или "
                                                 "\"False\" или \"false\".")
            elif self.columns_names[col] == 'entry_time':
                try:
                    datetime.strptime(new_value_str, '%H:%M:%S')
                    return new_value_str
                except ValueError:
                    try:
                        datetime.strptime(new_value_str, '%H:%M')
                        return new_value_str
                    except ValueError:
                        self.__showMessage("Ошибка", "Введите время в соответствующем формате.")
            elif self.columns_names[col] == 'leave_time':
                try:
                    datetime.strptime(new_value_str, '%H:%M:%S')
                    return new_value_str
                except ValueError:
                    try:
                        datetime.strptime(new_value_str, '%H:%M')
                        return new_value_str
                    except ValueError:
                        self.__showMessage("Ошибка", "Введите время в соответствующем формате.")
            elif self.columns_names[col] == 'class_id':
                try:
                    class_id = int(new_value_str)
                    if self.db.getter.getClassById(class_id) is None:
                        self.__showMessage("Ошибка", "Введите id существующего занятия.")
                    else:
                        return class_id
                except ValueError:
                    self.__showMessage("Ошибка", "Введите id в соответствующем формате.")
            elif self.columns_names[col] == 'person_id':
                try:
                    person_id = int(new_value_str)
                    if self.db.getter.getPerson(person_id) is None:
                        self.__showMessage("Ошибка", "Введите id существующего человека.")
                    else:
                        return person_id
                except ValueError:
                    self.__showMessage("Ошибка", "Введите id в соответствующем формате.")
        return None

    def set_new_value(self, value, row, col):
        table = self.data[row]
        if self.result == "metadata":
            if self.columns_names[col] == 'path':
                self.db.setter.updMetadata(meta_id=table.id, path=value, add_date=table.add_date)
            elif self.columns_names[col] == 'add_date':
                self.db.setter.updMetadata(meta_id=table.id, path=table.path, add_date=value)

        elif self.result == "person":
            if self.columns_names[col] == 'meta_id':
                self.db.setter.updPerson(person_id=table.id, name=table.name, meta_id=value)
            elif self.columns_names[col] == 'name':
                self.db.setter.updPerson(person_id=table.id, name=value, meta_id=table.meta_id)

        elif self.result == "subject":
            self.db.setter.updSubject(subject_id=table.id, name=value)

        elif self.result == "students_group":
            self.db.setter.updStudentsGroup(group_id=table.id, name=value)

        elif self.result == "student":
            if self.columns_names[col] == 'person_id':
                self.db.setter.updStudent(student_id=table.id, person_id=value, group_id=table.group_id)
            elif self.columns_names[col] == 'group_id':
                self.db.setter.updStudent(student_id=table.id, person_id=table.person_id, group_id=value)

        elif self.result == "teacher":
            if self.columns_names[col] == 'work_experience':
                self.db.setter.updTeacher(teacher_id=table.id, work_experience=value, person_id=table.person_id)
            elif self.columns_names[col] == 'person_id':
                self.db.setter.updTeacher(teacher_id=table.id, work_experience=table.work_experience, person_id=value)

        elif self.result == "class":
            if self.columns_names[col] == 'date_class':
                self.db.setter.updClass(class_id=table.id, date_class=value, start_time=table.start_time,
                                        end_time=table.end_time, audience=table.audience, subject_id=table.subject_id)
            elif self.columns_names[col] == 'start_time':
                self.db.setter.updClass(class_id=table.id, date_class=table.date_class, start_time=value,
                                        end_time=table.end_time, audience=table.audience, subject_id=table.subject_id)
            elif self.columns_names[col] == 'end_time':
                self.db.setter.updClass(class_id=table.id, date_class=table.date_class, start_time=table.start_time,
                                        end_time=value, audience=table.audience, subject_id=table.subject_id)
            elif self.columns_names[col] == 'subject_id':
                self.db.setter.updClass(class_id=table.id, date_class=table.date_class, start_time=table.start_time,
                                        end_time=table.end_time, audience=table.audience, subject_id=value)
            elif self.columns_names[col] == 'audience':
                self.db.setter.updClass(class_id=table.id, date_class=table.date_class, start_time=table.start_time,
                                        end_time=table.end_time, audience=value, subject_id=table.subject_id)

        elif self.result == "attendance":
            if self.columns_names[col] == 'status':
                self.db.setter.updAttendance(attendance_id=table.id, status=value, entry_time=table.entry_time,
                                             leave_time=table.leave_time, class_id=table.class_id,
                                             person_id=table.person_id)
            elif self.columns_names[col] == 'entry_time':
                self.db.setter.updAttendance(attendance_id=table.id, status=table.status, entry_time=value,
                                             leave_time=table.leave_time, class_id=table.class_id,
                                             person_id=table.person_id)
            elif self.columns_names[col] == 'leave_time':
                self.db.setter.updAttendance(attendance_id=table.id, status=table.status, entry_time=table.entry_time,
                                             leave_time=value, class_id=table.class_id, person_id=table.person_id)
            elif self.columns_names[col] == 'class_id':
                self.db.setter.updAttendance(attendance_id=table.id, status=table.status, entry_time=table.entry_time,
                                             leave_time=table.leave_time, class_id=value, person_id=table.person_id)
            elif self.columns_names[col] == 'person_id':
                self.db.setter.updAttendance(attendance_id=table.id, status=table.status, entry_time=table.entry_time,
                                             leave_time=table.leave_time, class_id=table.class_id, person_id=value)

    # Показать сообщение
    def __showMessage(self, title, message):
        QMessageBox.warning(self, title, message)
