class Student(object):
    def __init__(self, name):
        self.courses = ["CS 112", "Underwater Basket Weaving", "Fort Building 101", "Act like a penguin."]
        self.name = name

student = Student("Tim")

print "%s takes these courses:" % student.name
for i in student.courses:
    print i
