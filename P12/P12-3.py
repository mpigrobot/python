class Person(object):
    def __init__(self,name):
        self.name1 = name
class Student(Person):
    def  __init__(self,name,score):
        super(Student,self).__init__(name)
        self.score = score
        
s = Student('Tom','67')
p = Person('Bob')
print isinstance(s,Student)
print isinstance(p,Student)
print isinstance(s,Person)
print isinstance(p,Person)
