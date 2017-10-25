class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __str__(self):
         return '(Person: %s, %s)' % (self.name, self.score)

s = Student('Bob', 59)
s.score = 60
# s.score = 1000
print s