"""常用的魔术方法"""
"""
1.初始化init
2.创建一个新的实例__new__:实例化的魔术方法,触发时机:在实例化时候触发
返回值：__new__ 必须返回一个类的实例（通常是通过调用 super().__new__(cls) 来实现）。
调用顺序：__new__ 在 __init__ 之前被调用。
ps:与 __init__ 不同，__init__ 方法初始化实例，而 __new__ 方法实际负责创建实例
    确保 __new__ 方法返回一个实例，否则会导致 __init__ 方法不会被调用。
    如果不调用 super().__new__(cls)，则不会实际创建类的实例，
    从而导致后续的 __init__ 方法无法被调用。
    通常情况下，除非有特殊需求，否则不需要重写 __new__ 方法。
固定格式:
instance = super(MyStr, cls).__new__(cls, value)
return instance
3.__call__:使得类的实例可以像函数一样被调用:触发时机,当对象被像函数一样调的时候 -----对象()  
就会运行__call__里的程序,此时当被当做函数调用时候如果想做点什么,就要改写call

4.__del__  涉及垃圾回收机制:当所有的引用都被内部函数del删除  这块地址引用为0   就会运行del中的  返回些什么信息
            正常来说  程序都结束才会del,如果提前把所有引用都断开,提早就会进__del__
5.__str__  触发条件:当打印对象名(是对象名,比如phone1)的时候,自动触发去调用__str__内容,一定要加返回值,需配合return
            return后的才是打印能看到的内容,用于如果想在打印对象名的时候能够给开发者更多的信息
总结魔术方法:
重点:
__init__
__str__
非重点:
__new__:作用,开辟空间,大多数不需要重写
__del__ 作用:没有指针引用的时候会调用,一般不需要重写
__cal__:需要把对象当函数用,就重写,否则不要重写

"""

import sys  #为了看地址引用需要调用



class Person:
    def __init__(self, name):
        print('----->init', self)
        self.name = name

    def __new__(cls, *args, **kwargs):  # *args,**kwargs  是要自己添加到
        print('------>new')
        instance = super(Person, cls).__new__(cls)  # super(Person,cls)  可以改为object
        print(instance)
        return instance  # 这返回值会return到init的self,
        # init没运行完就不会继续运行init了,就报错了,init接住了,才会创建对象p,一共三步,
        # new是向内存申请空间的,有空间就有新的地址了,地址再扔给init,再给p

    # 先new后init,new把原来自带的魔术方法覆盖了,目的是为了在init之前再增加打印一些什么

    # 即使不写new,系统里也已经有了__new__,__init__是依赖于__new__的
    def __call__(self, name):  # *args,**kwargs  是要自己添加的  或者改成name
        print('--------->call')
        print('执行的对象得到的参数是:', name)



    def __del__(self):
        """
        触发时机:使用del 删除对象p,p1,p2等等的时候,加到最后,最后打印
        1.对象赋值
        p=Person()
        p1=p
        说明共同指向同一个地址
        2.删除地址的引用
        del p1 删除p1对地址都引用
        3.查看对地址都引用次数
        import sys
        sys.getrefcount(p)
        4.del 只出现在,当一块空间 没任何引用,没p,p1,p2情况下,默认执行__del__ 执行在所有程序的最后
        5.如果不删除完,successfujio出现在,出现在后续程序的前面,当所有空间引用都没了才会调,最好别自己去写,不然会把原来的垃圾回收机制覆盖
        python解释器,回收所有在这一次执行过程中,使用到的空间.回收就会把所有引用干掉,用del垃圾回收机制,就打印del successful--->自带的内存释放,所有程序运行完后,触发垃圾回收机制
        先断开,再回收.
        只有所有内存都清空后,会调用__del__
        """
        print('del successful')
        print('del ---->', p.name)


p = Person('jack')
print(p)
print(p.name)
p('call')  # 调用__call__
p1 = p
p2 = p
print(p1.name)
print(p2.name)
print(sys.getrefcount(p))  # 3个名指向p这个地址
p1.name = 'Tom'  # 同一个地址,并不是指针关系  换新电视了 p,p1,p2都能看得到

del p2
del p1
print('这是末尾')

"""
在某些特定情况下，重写 __new__ 方法是必要的。
以下是一些需要重写 __new__ 方法的常见场景和原因：
1. 对于一些不可变对象（如 int、str、tuple 等），一旦创建就不能修改它们的内容。对于这些对象的子类，你可能需要在创建时进行一些特殊处理。
2.单例模式是一种设计模式，确保一个类只有一个实例。通过重写 __new__ 方法，可以控制实例的创建，从而实现单例模式。
3.通过重写 __new__ 方法，可以自定义类的创建过程。
4.你可能需要在实例创建之前进行一些特殊处理，例如预处理输入数据或缓存实例。
"""
# 如果要把 对象p  当做函数,怎么叫当做函数?  对象()   这样就调用了.
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return '姓名是'+self.name+',年龄:'+str(self.age)

p=Person('Tom',18)
print(p)