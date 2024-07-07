class Dog:
    age = 2
    def __init__(self,nickname):

        self.nickname=nickname   #动态添加属性,动态添加是添加到对象的属性地址里

    def run(self):      #self ---依赖于对象,类方法是不需要对象都能调用的,类方法是类cls去调用的

        print('{}在院子里跑来跑去！'.format(self.nickname))
    def eat(self):
        print('在吃饭......')
        self.run()
    @classmethod
    def test(cls):#cls
        print(cls)
        print(cls.age)
"""
类方法特点:
1.定义需要依赖装饰器classmethod  ---->系统规定的classmethod
2.类方法中的参数,不是对象,而是当前类
3.类方法中,只可以使用类属性,不能使用对象属性,类方法是因为对象还没创建前就已经创建了(所以访问不到self,此时self还没产生)
所以直接可以用类调用,二不仅仅是用对象调用,类方法不依赖于对象
4.类方法能否使用普通方法?  类中,兄弟方法(同为普通方法)可以相互调用,是平行的
"""
d=Dog('大黄')
d.run()
#d.test()  #调test是没法调的   cls调不到里面的cls.nickname   init这个初始化是初始化在对象的属性地址里,
#而现在cls 调的是cls的模板地址,真要调用,可以cls里  init外命名一个  nickname改成age
d.test()   #虽然调用的是模板的,但是也要有对象来调
Dog.test()#直接类名可以调用
d.eat()  #类中方法之间的调用,需要通过self.方法调用,普通和普通直之间的调用,如果方法里有self,cls的方法都不能调用,因为self传不过去
#类方法的作用,只能对模板进行调整,只能访问类属性类方法,可以在对象创建之前需要一些动作,改模板用

#补充类方法-------->只能用类不能用对象   也不是完全不能调,
"""
类方法是绑定到类而不是实例的，因此不能通过实例直接调用类方法。
然而，你可以在实例方法中通过类来调用类方法。d.__class__.test()  就能对象调用到类方法
类方法不能直接调用实例方法，因为类方法是绑定到类上的，而实例方法是绑定到具体实例（对象）上的。
类方法没有实例的上下文，因此无法直接调用实例方法。

  # 类方法
    @classmethod
    def class_method(cls, instance):
        print("This is a class method.")
        # 调用实例方法
        instance.instance_method()

# 创建对象
obj = MyClass(42)

# 调用类方法，并传入实例对象
MyClass.class_method(obj) 
用传参数方式传进去
"""
class Person:
    __age=18    #私有化__方式调用.   调用也要用__age去调用   /__age不同于age了
    def __init__(self):
        name='jack'

    def show(self):
        print('-------->', Person.age)

    @classmethod
    def test(cls):
        print('class -------------->method')
    @classmethod
    def showage(cls):
        print('查看私有化的类的年龄age--->{}'.format(Person.__age))

    @staticmethod
    def test():#既没有cls 也没有self
        print('--------->静态方法')
        #print(self.name)语法错误,静态没有对象,self不能用在这,对象不能用,但是能用类名
        print(Person.__age)   #是能够打印的,只不过,原来是cls.__age ,现在没有cls,就人工改成Person





# p1=Person()
# p1.age=p1.age+1
# p1.show()
#不创建对象怎么改类里的年龄
#Person.age=Person.age+1  私有化后这句访问不到就报错了
#如何私有化,只能在内部访问,外部就访问
#不到,只能里面操作,不介意对象内操作,
# 只能依赖于类方法对其进行修改和查看,可以定义一个类方法进行查看
#类方法没法操作到
Person.showage()

"""
静态方法  很类似类方法,依赖于装饰器
1.需要装饰器@staticmethod,内部是没有cls的,调用只能手动Person.   手动类名调用  。区别就两个
2.静态方法无需传递参数(cls,self)
3.也只能访问类的属性和方法,对象的是无法访问的
4.加载时机同类方法

总结:读源码会看到  
1.装饰器不同
2.类方法有参数,静态方法没有参数
相同
1.只能访问类的属性和方法,对象的是无法访问的
2.都可以通过类名调用访问
3.都可以在创建对象之前使用,因为不依赖于对象

普通方法和两者区别
不同:
    1.没有装饰器
    2.普通方法永远要依赖对象,因为每个普通方法都有一个self
    3.只有创建了对象,才可以调用普通方法(普通方法=对象方法),否则无法调用
    
"""