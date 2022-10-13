import random
from classes.course import Course
from classes.student import Student

def main():
    students = [ Student("Mario", "Maric", "1234"),
                 Student("Ivana", "Ivica", "2234"),
                 Student("Pero", "Peric", "3234"),
                 Student("Ivana", "Ivic", "4234"),
                 Student("Marina", "Marijanovic", "5234"),
                 Student("Mario", "Maric", "6234"),
                 Student("Marko", "Markic", "2324"),
                 Student("Ante", "Antic", "9999"),
                 Student("Ana", "Anicic", "7334") ]
    courses = [ Course ("Programsko inzenjerstvo", "S303"),
                Course ("Matematika 1", "S101") ]
    for student in students:
        student.enroll(random.choice(courses))
    for course in courses:
        course.print()
    if __name__ == "__main__":
        main()