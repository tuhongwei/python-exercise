from datetime import datetime,timedelta
now = datetime.now()
class Student(object):
    """docstring for Student"""
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self,score):
        if not isinstance(score,int):
            raise ValueError('score must be an integer!')
        elif score <0 or score >100:
            raise ValueError('score must between 0~100!')
        else:
            self._score = score

    @property
    def birth(self):
        return self._birth
    @birth.setter
    def birth(self,birth):
        self._birth = birth

    # age只读属性
    @property 
    def age(self):
        return now.year - datetime.strptime(self._birth,'%Y-%m-%d').year

s = Student()
s.score = 95
print(s.score)
s.birth = '1992-9-28'
print(s.age)
    
        