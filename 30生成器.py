"""
通过列表生成式(列表推导式)，可直接创建一个列表
但是受到内存的限制，列表容量肯定有限制
不适合生成元素数量众多的列表 比如有一百万个元素的列表
如果我们仅仅需要访问前几个元素，后面的元素空间都白费了

所以，如果列表元素可以按照某个算法推算出，是否可以在后续的循环中 推算出后续的元素？
"""
"""生成器的定义方式1:"""
# 得到生成器   只要将列表换成圆括号,就是生成器
g = (x * 3 for x in range(10))
print(type(g))  # 类型为generate
print(g)  # 打印为一个地址
# 对于生成器，不是一下产生的
"""调用方式:两种方式,虽然与列表推导式一样,有范围,超出范围也一样报错
所以需要增加判断,不调用的时候是不会占用内存的
生成器的结果是列表里的数字
"""
# 方式1：通过调用__next__()
print(g.__next__())  # 不调用不会占用内存
# 方式2：next()   使用系统内置的next  内部放生成器类型的对象
print(next(g))

# 以上两种方式是一样的  如果超出生成器范围  会抛出StopIteration错误
while True:
    try:
        print(next(g))
    except:
        print('没有更多元素了')
        break
"""生成器的定义方式2:yield关键字"""
# 定义生成器方式二：借助函数完成  只要函数中出现了yield 关键字，说明函数就不是函数啦，函数变成生成器了
"""
拿函数写生成器的方式，
步骤1.定义一个函数，函数中使用yield关键字
步骤2.调用函数，接受调用的结果
步骤3.得到的结果就是生成器
步骤4.借助__next__  和next()  调用
"""


def func():
    n = 0
    while True:
        n += 1
        yield n  # 只要用到yield   就是一个生成器了
        # yield == return n +暂停  while True 也不是死循环了
        # 这次暂停，下次再调用会从暂停的地方开始  也就是从while循环开始


gen = func()

# 打印生成器产生的前五个值   这样就不用考虑范围里
for i in range(5):  # 可以for  也可以while
#while True:
    print(next(gen))

"""生成器内return有别的作用"""
# 用生成器得到斐波那契数列
def fib(length):
    a, b = 0, 1
    n = 0
    while n < length:
        yield b  # 这次暂停，下次再调用会从暂停的地方开始   类似返回值，不是返回值
        a, b = b, a + b
        n += 1
    return 'abc'  # 生成器内 return 就是再得到StopIteration后 的提示形象  以报错的形式返回


gene = fib(8)
# while True:
#     print(next(gene))#如果超出范围，还是会报错的。
