class Person(object):
    def __init__(self,name):
        self.name1 = name
class Student(Person):
    def  __init__(self,name,score):
        Person.__init__(self,name)
        self.score = score
s = Student('Tom','67')
print s.name1
print s.score


