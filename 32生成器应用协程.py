#进程>线程>协程   线程内开的小分支就是协程  一个线程内多任务，就会用到线程
def task1(n):
    for i in range(n):
        print('正在搬第{}块砖'.format(i))
        yield i  #temp=task1(10)能接到返回值  temp.__next__()是有返回值的
def task2(n):
    for i in range(n):
        print('正在听第{}首歌'.format(i))
        yield None
g1=task1(5)
g2=task2(5)
while True:
    try:
        returnvalue=g1.__next__()
        g2.__next__()
        #print(returnvalue)
    except:
        break
"""
生成器:generator
定义生成器的方式:
1.通过列表推导式方式构建
g=(x+1 for x in range(6))
2.函数 yield 
def func():
    yield
g=func()
产生元素:
1.next(generator)---->  每次调用都会产生一个新的元素，如果元素产生完毕，再此调用就会产生异常
2.生成器自己的方法:
g.__next__()
g.sent(values)

生成器的作用，取代了列表推导式，为了节省空间，用的时候再生成
应用在协程
"""
"""
获取里面的元素：

系统函数：next(g)

生成器里面函数：__next__()，[send(None), send(e)]

可迭代的与迭代器：
1. 生成器 2. 字符串, 列表, 集合,...

Iterable

isinstance(x, Iterable) ---> True, False

生成器就是一个迭代器 --->）next(g) ---> 下一个元素
next(list) ---> iter(list) ---> next(iter(list)) ---> 下一个元素

"""