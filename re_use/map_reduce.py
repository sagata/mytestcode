#coding=utf8

'''
map reduce zip 
map 的用法 其实就是 函数式编程而已 没什么啦
'''

print list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
test = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print [str(x) for x in test]

'''
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
'''

'''
zip 同步循环 
'''
test1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
test2 = [11, 12, 13, 14, 15, 16, 17, 18, 19]
print zip(test1,test2)
'''[(1, 11), (2, 12), (3, 13), (4, 14), (5, 15), (6, 16), (7, 17), (8, 18), (9, 19)]'''
for x,y in zip(test1,test2):
	print x,y