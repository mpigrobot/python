class Person(object):
    def __init__(self,name,gender,birth):
        self.name=name
        self.gender=gender
        self.birth=birth

xiaoming=Person('Xiao Ming','Male','1990-1-1')
print xiaoming.name