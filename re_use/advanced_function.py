#coding=utf8


#参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
#对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)
f1(1, 2, 3, 'a', 'b', x=99)


#return function
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
f = lazy_sum(1, 3, 5, 7, 9)
print f()

#decorator  下面只是一般写法 但是log2那样写其实也一样的
def log1(func):
    def wrapper(*args, **kw):
        print('log1 %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

def log2(func):
    print('log2 %s():' % func.__name__)
    return func

def log3(temp):
	print temp
	def decorator(func):
		print('log3 %s():' % func.__name__)
		return func
	return decorator
@log1
@log2
@log3('text')
def now(test):
    print('2015-3-25')

now('de')
'''
text
log3 now():
log2 now():
log1 now():
2015-3-25
'''
print '###############'
def now1(test):
    print('2015-3-25')
tempfunc = log1(now1)
tempfunc('test')
'''
log1 now1():
2015-3-25
'''

#实际上一个装饰器最好这样写  这样的目的是为了保持 函数的 __name__ 保持一致 免得挂了装饰器之后函数的这个名称变了
import functools

def log4(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

###############3
import generator
generator.__test()