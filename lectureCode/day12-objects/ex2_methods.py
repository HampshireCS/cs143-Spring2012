class Student(object):
    def __init__(self, name):
        self.courses = ["CS 112", "Underwater Basket Weaving", "Fort Building 101", "Act like a penguin."]
        self.name = name
    def courses(self):
        print "%s takes these courses:" % self.name
        for i in self.courses:
            print i

student = Student("Tim")
student.courses()