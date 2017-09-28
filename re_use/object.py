#coding=utf8

class Student(object):
	#下面那个相当于static变量
    name = 'hehe'
    #使用__slots__
    #__slots__ = ('__name', '__score') # 用tuple定义允许绑定的属性名称
    def __init__(self):
    	#私有变量
    	self.__name = 'name'
    	self.__score = 'score'

    def __get_name(self):
        return self.__name

    def get_score(self):
        return self.__score,self.__get_name()

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student()
#s.__score = 'fsd'
print s.get_score()
#  print s.__get_name()  这样调用私有方法是不行的
'''
('score', 'name')
'''
print Student.name
s.test = 'test'
print s.test

#动态给对象添加属性和方法
def set_age(self, age): # 定义一个函数作为实例方法
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s) # 给实例绑定一个方法
s.set_age(25) # 调用实例方法
print s.age # 测试结果

#动态给类添加属性和方法
def set_score(self, score):
    self.score = score
Student.set_score = set_score

#property 装饰器
'''
>>> s = Student()
>>> s.score = 60 # OK，实际转化为s.set_score(60)
>>> s.score # OK，实际转化为s.get_score()
60
>>> s.score = 9999
Traceback (most recent call last):
  ...
ValueError: score must between 0 ~ 100!
'''