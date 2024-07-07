#__str__
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        """

        __str__  触发条件:当打印对象名的时候,
        自动触发去调用__str__内容,一定要加返回值,
        return后的才是打印能看到的内容
        """

        return '姓名是'+self.name+',年龄:'+str(self.age)

p=Person('Tom',18)
print(p)

#单纯打印对象名称,出来的是一个地址,地址对开发者没意义
#如果想在打印对象名的时候能够给开发者更多的信息


"""
总结魔术方法:
重点:
__init__
__str__
非重点:
__new__:作用,开辟空间,大多数不需要重写
__del__ 作用:没有指针引用的时候会调用,一般不需要重写
__cal__:需要把对象当函数用,就重写,否则不要重写


大总结:
    普通方法--->重点
        def 方法名(self,[参数]):
            方法体
        对象.方法()
        
            方法之间的调用:
            class A:
                def a(self):
                    pass
                def b(self):
                    #调用a方法
                    self.a()
    
    
    
    类方法:@classmethod
        def 方法名(cls,[参数]):
            pass
        类名.方法名()
        对象.方法名()
    
    魔术方法:
        自动执行方法




"""