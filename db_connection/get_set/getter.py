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


class Getter:
    def __init__(self, session):
        self.session = session

    # Получение всех занятий
    def getAllClasses(self):
        classes = self.session.query(Class).all()
        return classes

    # Получение занятия
    def getClassById(self, id_: int):
        class_ = self.session.query(Class).filter_by(id=id_).first()
        return class_

    # Получение всех занятий определнной группы
    def getAllClassesByGroupId(self, group_id):
        class_groups = self.session.query(ClassGroup).filter_by(group_id=group_id).all()
        classes = []
        for class_group in class_groups:
            class_ = self.session.query(Class).filter_by(id=class_group.class_id).first()
            classes.append(class_)
        return classes

    # Получение всех занятий определнного преподавателя
    def getAllClassesByTeacherId(self, teacher_id):
        class_teachers = self.session.query(ClassTeacher).filter_by(teacher_id=teacher_id).all()
        classes = []
        for class_teacher in class_teachers:
            class_ = self.session.query(Class).filter_by(id=class_teacher.class_id).first()
            classes.append(class_)
        return classes

    # Получение всех людей
    def getAllPersons(self):
        persons = self.session.query(Person).all()
        return persons

    # Получение человека
    def getPerson(self, id_: int):
        person = self.session.query(Person).filter_by(id=id_).first()
        return person

    # Получение всех студентов
    def getAllStudents(self):
        students = self.session.query(Student).all()
        return students

    # Получение студента
    def getStudent(self, id_: int):
        students = self.session.query(Student).filter_by(id=id_).first()
        return students

    # Получение общей посещаемости студента
    def getAttendanceByStudent(self, student_id):
        student = self.session.query(Student).filter_by(id=student_id).first()
        attendance = self.session.query(Attendance).filter_by(person_id=student.person_id).all()
        return attendance

    # Получение посещаемости студента по определённому предмету
    def getAttendanceByStudentBySubject(self, student_id, subject_id):
        student = self.session.query(Student).filter_by(id=student_id).first()
        attendance = []
        classes = self.session.query(Class).filter_by(subject_id=subject_id).all()
        for class_ in classes:
            att = self.session.query(Attendance).filter_by(person_id=student.person_id, class_id=class_.id).all()
            attendance.append(att)
        return attendance

    # Получение всех предметов
    def getAllSubjects(self):
        subjects = self.session.query(Subject).all()
        return subjects

    # Получение предмета
    def getSubject(self, id_: int):
        subject = self.session.query(Subject).filter_by(id=id_).first()
        return subject

    # Получение всех преподавателей, которые ведут этот предмет
    def getAllTeachersBySubj(self, subject_id):
        subject_teachers = self.session.query(SubjectTeacher).filter_by(subject_id=subject_id).all()
        teachers = []
        for sub_th in subject_teachers:
            teacher = self.session.query(Teacher).filter_by(id=sub_th.teacher_id).first()
            teachers.append(teacher)
        return teachers

    # Получение всех преподавателей
    def getAllTeachers(self):
        teachers = self.session.query(Teacher).all()
        return teachers

    # Получение преподавателя
    def getTeacher(self, id_: int):
        teacher = self.session.query(Teacher).filter_by(id=id_).first()
        return teacher

    # Получение всех предметов, которые ведёт этот преподаватель
    def getAllSubjectsByTeachers(self, teacher_id):
        subject_teachers = self.session.query(SubjectTeacher).filter_by(teacher_id=teacher_id).all()
        subjects = []
        for sub_th in subject_teachers:
            subject = self.session.query(Subject).filter_by(id=sub_th.subject_id).first()
            subjects.append(subject)
        return subjects

    # Получение всех мета данных
    def getAllMetadata(self):
        metadata = self.session.query(Metadata).all()
        return metadata

    # Получение мета данных
    def getMetadata(self, id_: int):
        metadata = self.session.query(Metadata).filter_by(id=id_).first()
        return metadata

    # Получение общей посещаемости
    def getAllAttendance(self):
        attendance = self.session.query(Attendance).all()
        return attendance

    # Получение посещаемости
    def getAttendance(self, id_: int):
        attendance = self.session.query(Attendance).filter_by(id=id_).first()
        return attendance

    # Получение всех групп
    def getAllStudentsGroup(self):
        students_groups = self.session.query(StudentsGroup).all()
        return students_groups

    # Получение группы
    def getStudentsGroup(self, id_: int):
        students_group = self.session.query(StudentsGroup).filter_by(id=id_).first()
        return students_group

    # Получение списка студентов определённой группы
    def getAllStudentsByGroup(self, group_id):
        students = self.session.query(Student).filter_by(group_id=group_id).all()
        return students

    # Получение всех записей таблицы
    def getAllClassGroup(self):
        class_groups = self.session.query(ClassGroup).all()
        return class_groups

    # Получение всех записей таблицы
    def getAllClassTeacher(self):
        class_teachers = self.session.query(ClassTeacher).all()
        return class_teachers

    # Получение всех записей таблицы
    def getAllSubjectTeacher(self):
        subject_teachers = self.session.query(SubjectTeacher).all()
        return subject_teachers
