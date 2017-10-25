class Person(object):
    __slots__ = ('name', 'gender')
    def __init__(self, name, gender,score):
        self.name = name
        self.gender = gender
        self.score = score
class Student(Person):
    def __init__(self, name, gender,score):
        super(Student, self).__init__(name, gender,score)
s = Student('Bob', 'male',59)
s.score = 59
print s.score