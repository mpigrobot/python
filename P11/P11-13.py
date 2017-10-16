class Person(object):
    def __init__(self,name,score):
        self.name=name
        self.score=score
    def get_score(self):
        return 'A'
p1=Person('Bob',90)
print p1.get_score
print p1.get_score()