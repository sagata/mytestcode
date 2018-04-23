#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 打开文件
fo = open("runoob.txt", "r")
print "文件名为: ", fo.name

line = fo.readline()
print "读取的数据为: %s" % (line)

# 重新设置文件读取指针到开头
fo.seek(0, 0)
line = fo.readline()
print "读取的数据为: %s" % (line)

# 从 结尾往前移动贯标52
fo.seek(-52, 2)
line = fo.readline()
print "读取的数据为: %s" % (line)
# 关闭文件
fo.close()

test = {'test':'','tes2':''}
print [i for i,o in test.items()]