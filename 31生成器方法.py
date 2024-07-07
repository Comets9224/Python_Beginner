"""生成器方法
.__next__获取下一个元素
.sent(value)  传值赋给yield   既能够传值给yield
也能够传到temp，给生成器后面去用，需要外界往里送的情况，首次使用要None

        temp = yield i
        for i in temp
            print('temp:',temp)





"""
def gen():
    """
       next() 的行为:

       当你调用 next() 时，生成器恢复执行，并且 yield 表达式的值为 None。
       例如，在 temp = yield i 这一行，yield i 会暂停生成器并返回 i 的值，但 temp 会被赋值为 None。
       send(value) 的行为:

       当你调用 send(value) 时，生成器恢复执行，并且 yield 表达式的值为 value。
       例如，在 temp = yield i 这一行，yield i 会暂停生成器并返回 i 的值，而当生成器恢复执行时，temp 会被赋值为 send 方法传递的 value。


       """
    i=0
    while i<5:
        temp = yield i  #yield 类似return 返回值   temp是接不到值的 yield返回i值
                        #为什么不用field接不到？  因为每次进来，生成器会清楚掉上次的i，并且赋值为None
                        # send相当于 在此运行，重新给yield赋值，就给temp接到了  只会发一次，下次进来还是None

        print('temp:',temp)
        i+=1
    return '没有更多数据了'
"""
必须要g=gen() 吗  直接打印不行吗?
直接打印是不行的，因为每次调用 gen()
都会创建一个新的生成器对象。要连续获取生成器的值，你必须使用同一个生成器对象
"""
g=gen()
"""
在 Python 中，当你第一次启动一个生成器时，
你不能使用 send() 方法传递一个值。必须使用
 next() 方法或 send(None) 来启动生成器。
 这是因为在生成器刚刚创建时，它还没有执行到
 第一个 yield 语句，因此没有地方可以接收传递的值。
"""
n0=g.send(None)   #sent(None)不是一个字符串的None
n1=g.send('hhhh')
print('n1',n1)
n2=g.send('hahahaha')   #结果发现用了sent  haha 被temp接到了  算是当运行到yield  抛出你想要的信息
                        #实际上  走到yield 就停了，yield就没有抛出给temp
                        #send有调用的作用 ，除此之外还有  send用于 上一次的调用停在了yield 这次把send的东西 进到yield 赋值给temp
print('n2',n2)
