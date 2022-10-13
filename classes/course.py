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