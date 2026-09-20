class Student:
    def __init__(self, name):
        self.name = name

class Course:
    def __init__(self, title):
        self.title = title
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def list_students(self):
        for s in self.students:
            print(s.name)


