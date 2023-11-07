from db_connection.db_models.class_ import Class
from db_connection.db_models.person import Person
from db_connection.db_models.student import Student
from db_connection.db_models.subject import Subject
from db_connection.db_models.teacher import Teacher
from db_connection.db_models.metadata import Metadata
from db_connection.db_models.attendance import Attendance
from db_connection.db_models.class_group import ClassGroup
from db_connection.db_models.class_teacher import ClassTeacher
from db_connection.db_models.students_group import StudentsGroup
from db_connection.db_models.subject_teacher import SubjectTeacher


class Setter:
    def __init__(self, session):
        self.session = session

    def __findFirstFreeID(self, table_db):
        stmt = self.session.query(table_db).order_by(table_db.id.asc()).all()
        count = self.session.query(table_db).count()
        mass = []
        for i in range(1, count + 1):
            if i != stmt[i - 1].id:
                mass.append(i)
        if len(mass) != 0:
            count = mass[0]
        else:
            count += 1
        return count

    # 1
    # Добавление нового занятия
    def addClass(self, date_class: str, start_time: str, end_time: str, audience: str, subject_id: int):
        new_id = self.__findFirstFreeID(Class)
        new_class = Class(id=new_id, date_class=date_class, start_time=start_time, end_time=end_time, audience=audience,
                          subject_id=subject_id)
        self.session.add(new_class)

    # Обновление занятия
    def updClass(self, class_id: int, date_class: str, start_time: str, end_time: str, audience: str, subject_id: int):
        upd_class = self.session.query(Class).filter_by(id=class_id).first()
        upd_class.date_class = date_class
        upd_class.start_time = start_time
        upd_class.end_time = end_time
        upd_class.audience = audience
        upd_class.subject_id = subject_id

    # Удаление занятия
    def delClass(self, class_id: int):
        class_teachers = self.session.query(ClassTeacher).filter_by(class_id=class_id).all()
        for row in class_teachers:
            self.session.delete(row)

        class_groups = self.session.query(ClassGroup).filter_by(class_id=class_id).all()
        for row in class_groups:
            self.session.delete(row)

        attendance = self.session.query(Attendance).filter_by(class_id=class_id).all()
        for row in attendance:
            self.session.delete(row)

        self.session.query(Class).filter_by(id=class_id).delete()

    # 2
    # Добавление нового человека
    def addPerson(self, name: str, meta_id: int):
        new_id = self.__findFirstFreeID(Person)
        new_person = Person(id=new_id, name=name, meta_id=meta_id)
        self.session.add(new_person)

    # Обновление человека
    def updPerson(self, person_id: int, name: str, meta_id: int):
        upd_person = self.session.query(Person).filter_by(id=person_id).first()
        upd_person.name = name
        upd_person.meta_id = meta_id

    # Удаление человека
    def delPerson(self, person_id: int):
        students = self.session.query(Student).filter_by(person_id=person_id).all()
        for row in students:
            self.session.delete(row)

        teachers = self.session.query(Teacher).filter_by(person_id=person_id).all()
        for row in teachers:
            self.delTeacher(row.id)

        attendance = self.session.query(Attendance).filter_by(person_id=person_id).all()
        for row in attendance:
            self.session.delete(row)

        self.session.query(Person).filter_by(id=person_id).delete()

    # 3
    # Добавление нового студента
    def addStudent(self, person_id: int, group_id: int):
        new_id = self.__findFirstFreeID(Student)
        new_student = Student(id=new_id, person_id=person_id, group_id=group_id)
        self.session.add(new_student)

    # Обновление студента
    def updStudent(self, student_id: int, person_id: int, group_id: int):
        upd_student = self.session.query(Student).filter_by(id=student_id).first()
        upd_student.person_id = person_id
        upd_student.group_id = group_id

    # Удаление студента
    def delStudent(self, student_id: int):
        self.session.query(Student).filter_by(id=student_id).delete()

    # 4
    # Добавление нового предмета
    def addSubject(self, name: str):
        new_id = self.__findFirstFreeID(Subject)
        new_subject = Subject(id=new_id, name=name)
        self.session.add(new_subject)

    # Обновление предмета
    def updSubject(self, subject_id: int, name: str):
        upd_subject = self.session.query(Subject).filter_by(id=subject_id).first()
        upd_subject.name = name

    # Удаление предмета
    def delSubject(self, subject_id: int):
        classes = self.session.query(Class).filter_by(subject_id=subject_id).all()
        for row in classes:
            self.delClass(row.id)

        sub_tch = self.session.query(SubjectTeacher).filter_by(subject_id=subject_id).all()
        for row in sub_tch:
            self.session.delete(row)

        self.session.query(Subject).filter_by(id=subject_id).delete()

    # 5
    # Добавление нового преподавателя
    def addTeacher(self, work_experience: int, person_id: int):
        new_id = self.__findFirstFreeID(Teacher)
        new_teacher = Teacher(id=new_id, work_experience=work_experience, person_id=person_id)
        self.session.add(new_teacher)

    # Обновление преподавателя
    def updTeacher(self, teacher_id: int, work_experience: int, person_id: int):
        upd_teacher = self.session.query(Teacher).filter_by(id=teacher_id).first()
        upd_teacher.work_experience = work_experience
        upd_teacher.person_id = person_id

    # Удаление преподавателя
    def delTeacher(self, teacher_id: int):
        class_teachers = self.session.query(ClassTeacher).filter_by(teacher_id=teacher_id).all()
        for row in class_teachers:
            self.session.delete(row)

        sub_tch = self.session.query(SubjectTeacher).filter_by(teacher_id=teacher_id).all()
        for row in sub_tch:
            self.session.delete(row)

        self.session.query(Teacher).filter_by(id=teacher_id).delete()

    # 6
    # Добавление новых мета данных
    def addMetadata(self, path: str, add_date: str):
        new_id = self.__findFirstFreeID(Metadata)
        new_metadata = Metadata(id=new_id, path=path, add_date=add_date)
        self.session.add(new_metadata)

    # Обновление мета данных
    def updMetadata(self, meta_id: int, path: str, add_date: str):
        upd_metadata = self.session.query(Metadata).filter_by(id=meta_id).first()
        upd_metadata.path = path
        upd_metadata.add_date = add_date

    # Удаление мета данных
    def delMetadata(self, meta_id: int):
        persons = self.session.query(Person).filter_by(meta_id=meta_id).all()
        for row in persons:
            self.session.delete(row)

        self.session.query(Metadata).filter_by(id=meta_id).delete()

    # 7
    # Добавление новой посещаемости
    def addAttendance(self, status: bool, entry_time: str, leave_time: str, class_id: int, person_id: int):
        new_id = self.__findFirstFreeID(Attendance)
        new_attendance = Attendance(id=new_id, status=status, entry_time=entry_time, leave_time=leave_time,
                                    class_id=class_id, person_id=person_id)
        self.session.add(new_attendance)

    # Обновление посещаемости
    def updAttendance(self, attendance_id: int, status: bool, entry_time: str, leave_time: str, class_id: int, person_id: int):
        upd_attendance = self.session.query(Attendance).filter_by(id=attendance_id).first()
        upd_attendance.status = status
        upd_attendance.entry_time = entry_time
        upd_attendance.leave_time = leave_time
        upd_attendance.class_id = class_id
        upd_attendance.person_id = person_id

    # Удаление мета данных
    def delAttendance(self, attendance_id: int):
        self.session.query(Attendance).filter_by(id=attendance_id).delete()

    # 8
    # Добавление нового соотношения занятий и групп
    def addClassGroup(self, group_id: int, class_id: int):
        new_class_group = ClassGroup(group_id=group_id, class_id=class_id)
        self.session.add(new_class_group)

    # Обновление соотношения занятий и групп
    def updClassGroup(self, group_id: int, class_id: int):
        upd_class_group = self.session.query(ClassGroup).filter_by(group_id=group_id, class_id=class_id).first()
        upd_class_group.group_id = group_id
        upd_class_group.class_id = class_id

    # Удаление соотношения занятий и групп
    def delClassGroup(self, group_id: int, class_id: int):
        self.session.query(ClassGroup).filter_by(group_id=group_id, class_id=class_id).delete()

    # 9
    # Добавление нового соотношения занятий и преподавателей
    def addClassTeacher(self, teacher_id: int, class_id: int):
        new_class_teacher = ClassTeacher(teacher_id=teacher_id, class_id=class_id)
        self.session.add(new_class_teacher)

    # Обновление соотношения занятий и преподавателей
    def updClassTeacher(self, teacher_id: int, class_id: int):
        upd_class_teacher = self.session.query(ClassTeacher).filter_by(teacher_id=teacher_id, class_id=class_id).first()
        upd_class_teacher.teacher_id = teacher_id
        upd_class_teacher.class_id = class_id

    # Удаление соотношения занятий и преподавателей
    def delClassTeacher(self, teacher_id: int, class_id: int):
        self.session.query(ClassTeacher).filter_by(teacher_id=teacher_id, class_id=class_id).delete()

    # 10
    # Добавление новой группы
    def addStudentsGroup(self, name: str):
        new_id = self.__findFirstFreeID(StudentsGroup)
        new_group = StudentsGroup(id=new_id, name=name)
        self.session.add(new_group)

    # Обновление группы
    def updStudentsGroup(self, group_id: int, name: str):
        upd_class_teacher = self.session.query(StudentsGroup).filter_by(id=group_id).first()
        upd_class_teacher.name = name

    # Удаление группы
    def delStudentsGroup(self, group_id: int):
        students = self.session.query(Student).filter_by(group_id=group_id).all()
        for row in students:
            self.session.delete(row)

        class_groups = self.session.query(ClassGroup).filter_by(group_id=group_id).all()
        for row in class_groups:
            self.session.delete(row)

        self.session.query(StudentsGroup).filter_by(id=group_id).delete()

    # 11
    # Добавление нового соотношения занятий и преподавателей
    def addSubjectTeacher(self, teacher_id: int, subject_id: int):
        new_class_teacher = SubjectTeacher(teacher_id=teacher_id, subject_id=subject_id)
        self.session.add(new_class_teacher)

    # Обновление соотношения занятий и преподавателей
    def updSubjectTeacher(self, teacher_id: int, subject_id: int):
        upd_class_teacher = self.session.query(SubjectTeacher).filter_by(teacher_id=teacher_id, subject_id=subject_id).first()
        upd_class_teacher.teacher_id = teacher_id
        upd_class_teacher.subject_id = subject_id

    # Удаление соотношения занятий и преподавателей
    def delSubjectTeacher(self, teacher_id: int, subject_id: int):
        self.session.query(SubjectTeacher).filter_by(teacher_id=teacher_id, subject_id=subject_id).delete()
