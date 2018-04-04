#! /usr/bin/python

class Student(object):

    def get_score(self):
        return self.get_score()

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value >100:
            raise ValueError("score must between 0~100!")
        self._score = value

s=Student()
s.set_score('bob')
print(s.get_score())
