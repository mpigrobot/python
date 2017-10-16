class Person(object):
    address='Earth'
    __count=0
    __language='Chinese'
    @classmethod
    def how_many(cls):
        return cls.__count
    def __init__(self,name,score,gender):
        self.score=score
        self.__name=name
        self.__gender=gender
        Person.__count=Person.__count+1
    def get_name(self):
        return self.__name

p1=Person('Bob',90,'Male')
print Person.how_many()
p2=Person('Alice',65,'Female')
print Person.how_many()

print p1.address
p1.address='China'
print p1.address
print p2.address

print p1.score
print p1.get_name()
# print p1.gender
print p1.Language





