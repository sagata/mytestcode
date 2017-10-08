# -*- coding: utf-8 -*-

'''
使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：
'''

from collections import defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print dd['key1'] # key1存在
'abc'
print dd['key2'] # key2不存在，返回默认值
'N/A'

'''
使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
'''

from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
print d # dict的Key是无序的
{'a': 1, 'c': 3, 'b': 2}
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print od # OrderedDict的Key是有序的
for key in od:
    print key