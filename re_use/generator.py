# -*- coding: utf-8 -*-
#生成器的作用是为了避免大量数据放在内存里，  所以只做了一个迭代器，需要查第几号数据的时候才去生成
s = (x * x for x in range(5))
print(s)
for x in s:
    print(x)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1


f = fib(10)
print('fib(10):', f)
test = []
test += f
print 'fsd'
print test
for x in f:
    print(x)

# call generator manually:
g = fib(5)
while 1:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        #print('Generator return value:', e.value)
        break
