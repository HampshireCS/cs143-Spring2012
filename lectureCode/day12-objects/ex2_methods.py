class Student(object):
    def __init__(self, name):
        self.classes = ["CS 112", "Underwater Basket Weaving", "Fort Building 101", "Act like a penguin."]
        self.name = name
    def classes(self):
        print "%s takes these classes:" % self.name
        for i in self.classes:
            print i

student = Student("Tim")
student.classes()