#coding=utf8

#lambda 其实就是匿名函数 
func=lambda x:x+1
print(func(1))
#2
print(func(2))
#3

#以上lambda等同于以下函数
def func(x):
    return(x+1)

#结合 map  reduce 和fulter 来看你看 
from functools import reduce 
foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]

print (list(filter(lambda x: x % 3 == 0, foo)))
#[18, 9, 24, 12, 27]

print (list(map(lambda x: x * 2 + 10, foo)))
#[14, 46, 28, 54, 44, 58, 26, 34, 64]

print (reduce(lambda x, y: x + y, foo))
#139

# 顺便说一下 sorted
print sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
['Zoo', 'Credit', 'bob', 'about']

