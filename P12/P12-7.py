class Person(object):
    def __init__(self,name):
        self.name = name
class Student(Person):
    def  __init__(self,name,score):
        super(Student,self).__init__(name)
        self.score = score
class Skill(object):
    def __init__(self):
        print'My name is' 
        
class SStudent(Student,Skill):
    def __init__(self,name,score,weight):
        Student.__init__(self,name,score)
        Skill.__init__(self)
        self.bw = weight
        
        
s = SStudent('Tom','67','100')
print s.name
print s.score
print s.bw
