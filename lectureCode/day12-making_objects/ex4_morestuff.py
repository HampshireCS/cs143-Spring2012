class Student(object):
    next_id = 0
    def __init__(self, name="Tim"):
        self.name = name
        self.id = Student.next_id
        Student.next_id += 1
    def __str__(self):
        return "%d %s" % (self.id, self.name)
    __repr__ = __str__

class Course(object):
    def __init__(self, name):
        self.name = name
        self.enrolled = []
    def enroll(self, *students):
        self.enrolled += students

forts = Course("Fort Building 101")
acting = Course("Acting: like a penguin.")
scuba = Course("Underwater Basket Weaving")
cs = Course("CS 112")

stu1 = Student()
rob = Student(name="Rob")
ella = Student(name="Ella")
justine = Student(name="Justine")

cs.enroll(stu1, rob, ella, justine)
print cs.enrolled