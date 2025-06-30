
class TooManyStudentsException(Exception):
    pass

class Person:
    def __init__(self, name: str):
        self.name = name

class Teacher(Person):
    pass

class Student(Person):
    pass


class Classroom:
    def __init__(self, teacher: str, students: list[Student], course_title: str):
        self.teacher = teacher
        self.students = students
        self.course_title = course_title

    def add_student(self, student: Student):
        if len(self.students) < 30:
            self.students.append(student)
        else:
            raise TooManyStudentsException

    def remove_student(self, name: str):
        self.students = [s for s in self.students if s.name != name]

    def change_teacher(self, teacher: str):
        self.teacher = teacher

