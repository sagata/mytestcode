#coding=utf8'

print [x * x for x in range(1, 11)]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#加条件的情况
print [x * x for x in range(1, 11) if x % 2 == 0]
[4, 16, 36, 64, 100]

#双层循环嵌套
print [m + n for m in 'ABC' for n in 'XYZ']
['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

#字典也可以哦
d = {'x': 'A', 'y': 'B', 'z': 'C' }
print [k + '=' + v for k, v in d.items()]
['y=B', 'x=A', 'z=C']