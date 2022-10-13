import random

class Course:
    def __init__(self, name, course_code):
        self.name = name
        self.course_code = course_code
        self.students = []
    def __str__(self):
        return "%s [%s]" % (self.name, self.course_code)
    def print(self):
        print("=================")
        print(self)
        print("=================")
        for i, student in enumerate(self.students):
            print(f"{i+1}. {student}")

class Student:
    def __init__(self, name, lastname, student_number):
        self.name = name
        self.lastname = lastname
        self.student_number = student_number
        self.classes = []
    def __str__(self):
        return "%s %s (%s)" %(self.name, self.lastname, self.student_number)
    def enroll(self, course):
        self.classes.append(course)
        course.students.append(self)

def main():
    students = [ Student("Mario", "Maric", "1234"),
                 Student("Ivan", "Ivic", "2234"),
                 Student("Pero", "Peric", "3234"),
                 Student("Ivan", "Ivic", "4234"),
                 Student("Ivan", "Ivic", "5234"),
                 Student("Ivan", "Ivic", "6234"),
                 Student("Ana", "Anicic", "7334") ]
    courses = [ Course ("Programsko inzenjerstvo", "S303"),
                Course ("Matematika 1", "S101") ]
    for student in students:
        student.enroll(random.choice(courses))
    for course in courses:
        course.print()
    if __name__ == "__main__":
        main()