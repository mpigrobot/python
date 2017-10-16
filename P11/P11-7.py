class Person(object):
    def __init__(self,name):
        self.name=name
        self._title='Mr'
        self.__job='Student'
p=Person('Bob')
print p.name
print p._title
print p.__job

