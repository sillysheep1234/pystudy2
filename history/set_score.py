class Student(object):

    def get_score(self):
         return self._score

    def set_score(self, value):
        if type(value)!=int:
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student()
s.set_score(60) # ok!
print(s._score)
s.get_score

#s.set_score(9999)

#s.set_score('abc')

