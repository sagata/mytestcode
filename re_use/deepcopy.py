#coding=utf8
# 除了基本类型  比如 整形 什么的  像列表 字典 或者是类 这些东西
#垃圾回收机制就是在对象不再有人引用的时候回收
test1 = [1,2,3]
test2 = test1
test1[0] = 12
print test1
print test2
'''
# 这里的话 就会是一样的
# 如果这不是你的意图的话  请使用 深复制
'''
import copy
test1 = [1,2,3]
test2 = copy.deepcopy(test1)
test1[0] = 12
print test1
print test2
'''这里打印出就不一样啦 '''

'''有意思'''
l1 = [1,('a',1)]
l2 = [1,('a',1)]
print l1 == l2, l1 is l2
'''True False'''

