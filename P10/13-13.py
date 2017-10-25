# -*- coding: utf-8 -*-
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score
    @property
    def score(self):
        return self.__score
    @score.sett
    def score(self, score):
        if score < 0 or score > 100:
            raise ValueError('invalid score')
        self.__score = score
s = Student('Bob', 59)
s.score = 60  #OK!实际转化为s.set_score(60)
print s.score  #实际转化为s.get_score()