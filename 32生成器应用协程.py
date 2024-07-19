# 进程>线程>协程   线程内开的小分支就是协程  一个线程内多任务，就会用到线程
def task1(n):
    for i in range(n):
        print('正在搬第{}块砖'.format(i))
        yield i  # temp=task1(10)能接到返回值  temp.__next__()是有返回值的


def task2(n):
    for i in range(n):
        print('正在听第{}首歌'.format(i))
        yield None


g1 = task1(5)
g2 = task2(5)
while True:
    try:
        returnvalue = g1.__next__()
        g2.__next__()
        # print(returnvalue)
    except:
        break
"""
生成器自己的方法:
g.__next__()
g.sent(values)

生成器的作用，取代了列表推导式，为了节省空间，用的时候再生成
应用在协程
生成器系统函数：__next__()，[send(None), send(e)]
函数用法:isinstance(x, Iterable) ---> 用这个函数能看x 是不是可迭代类型  返回值True, False  
生成器就是一个迭代器，迭代器不是生成器，迭代器的范围更广阔
可迭代类型(Iterable)不是迭代器,可迭代类型有如下
1. 生成器 2. 字符串, 列表, 集合,...
"""
