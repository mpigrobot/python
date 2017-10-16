class Person(object):
    def __init__(self,name):
        self.__name=name
    def get_name(self):
        return self.__name

p1=Person('Bob')
print p1.get_name()