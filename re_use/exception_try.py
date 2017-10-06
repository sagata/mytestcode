#coding=utf8

class XYException(Exception):
	pass

#finally 是无论如何都会走到的
try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')


try:
	raise XYException('test')
except XYException as e:
	print('except:', e)

	