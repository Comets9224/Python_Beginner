class Dog:
    age = 2

    def __init__(self, nickname):
        self.nickname = nickname  # 动态添加属性,动态添加是添加到对象的属性地址里

    def run(self):  # self ---依赖于对象,类方法是不需要对象都能调用的,类方法是类cls去调用的
        print('{}在院子里跑来跑去！'.format(self.nickname))

    def eat(self):
        print('在吃饭......')
        self.run()

    @classmethod
    def test(cls):  # cls
        print(cls)
        print(cls.age)


"""
类方法特点:
1.定义需要依赖装饰器@classmethod  ---->系统规定的classmethod
2.类方法中的参数,不是对象,而是当前类
-->重要区别3.类方法中,只可以使用类属性,不能使用对象属性,类方法是因为对象还没创建前就已经创建了(所以访问不到self,此时self还没产生)
所以直接可以用类调用,而不仅仅是用对象调用,类方法不依赖于对象
4.类方法能否使用普通方法(实例方法)?   ------>不能，因为类创建的时候还没有实例。
5.实例能调用类方法:类方法是绑定到类而不是实例的，但需要实例或类进行调用
然而，你可以在实例方法中通过类来调用类方法。d.__class__.test()  就能对象调用到类方法  
===============================================================================
类: Dog
---------------------
| - age: int        |  <--- 类属性
|                   |
| + __init__(self, nickname)  |  <--- 实例方法
| + run(self)       |  <--- 实例方法
| + eat(self)       |  <--- 实例方法
| + test(cls)       |  <--- 类方法
---------------------
          |
          |
          v
实例: d = Dog('大黄')
---------------------
| - nickname: str   |  <--- 实例属性
---------------------

调用关系:
    d.run()    -> 合法 (实例调用实例方法)
    d.eat()    -> 合法 (实例调用实例方法)
    d.test()   -> 合法 (实例调用类方法)
    Dog.test() -> 合法 (类调用类方法)
    Dog.run()  -> 不合法 (类不能调用实例方法)
    Dog.eat()  -> 不合法 (类不能调用实例方法)
============================================================================================
实例-->通过__class__能调用类函数
例:
self.__class__.class_method()

    @classmethod
    def class_method(cls):          #里面放的不是self而是classmethod
        print(f'这是类方法，访问类属性：{cls.class_attribute}')
        
d.test() 是调用类方法的简洁方式。
d.__class__.test() 是通过实例的类调用类方法的方式，效果相同，但更冗长。
在实际编程中，使用 d.test() 更加简洁和直观，因为 Python 会自动解析实例的类并调用相应的类方法。使用 d.__class__.test() 
的情况相对较少，通常在需要明确处理类的情况下才会使用。

__class__ 属性指向对象的类，因此可以通过实例的 __class__ 属性来访问类方法。
类方法就是直接对类属性等操作的，比如直接对上面age操作的方法。 
6.类中,兄弟方法(同为普通方法)可以相互调用,是平行的
"""
d = Dog('大黄')
d.run()
# d.test()  #调test是没法调的   cls调不到里面的cls.nickname   init这个初始化是初始化在对象的属性地址里,
# 而现在cls 调的是cls的模板地址,真要调用,可以cls里  init外命名一个  nickname改成age
d.test()  # 虽然调用的是模板的,但是也要有对象来调
Dog.test()  # 直接类名可以调用
d.eat()  # 类中方法之间的调用,需要通过self.方法调用,普通和普通直之间的调用,如果方法里有self,
# 那么cls的方法都不能调用带self的,因为self传不过去
# 类方法的作用,只能对模板进行调整,只能访问类属性类方法,可以在对象创建之前需要一些动作,改模板用

# 补充类方法-------->只能用类cls不能用对象
"""
应用场景:还没创建对象就要修改，就可以用类调用类方法。

类方法不能直接调用实例方法，因为类方法是绑定到类上的，而实例方法是绑定到具体实例（对象）上的。
类方法没有实例的上下文，因此无法直接调用实例方法。

# 类方法
@classmethod
def class_method(cls, instance):
    print("This is a class method.")
    # 调用实例方法
    instance.instance_method()   #调不了  因为没创建self呢还

# 创建对象
obj = MyClass(42)

# 调用类方法，并传入实例对象
MyClass.class_method(obj) 
用传参数方式传进去
"""


class Person:
    __age = 18  # 私有化__方式调用.   调用也要用__age去调用   /__age不同于age了

    def __init__(self):
        name = 'jack'

    def show(self):
        print('-------->', Person.age)

    @classmethod
    def test(cls):
        print('class -------------->method')

    @classmethod
    def showage(cls):
        print('查看私有化的类的年龄age--->{}'.format(Person.__age))

    @staticmethod
    def test():  # 既没有cls 也没有self
        print('--------->静态方法')
        # print(self.name)语法错误,静态没有对象,self不能用在这,对象不能用,但是能用类名
        print(Person.__age)  # 是能够打印的,只不过,原来是cls.__age ,现在没有cls,就人工改成Person


# 不同与原来的cls调用 而是要用类的名才能调用

# p1=Person()
# p1.age=p1.age+1
# p1.show()
# 不创建对象怎么改类里的年龄
# Person.age=Person.age+1  私有化后这句访问不到就报错了
#
"""
如何私有化
只能在内部访问,外部就访问不到,只能里面操作,不建议对象内操作,
因为是对类的修改,类没创建只能直接用类的方法修改
只能依赖于类方法对其进行修改和查看,可以定义一个类方法进行查看


私有化了会怎样？
外界无法读取也无法修改._______>刚创建的时候还是能修改的
私有化属性主要通过实例方法来访问和修改，因为这些属性与具体的实例相关。
类方法也可以访问和修改实例的私有化属性，但需要通过实例来操作。
使用类方法修改实例的私有化属性时，需要确保传入的对象是正确的实例类型。

#好处:可以添加判断.
#私有化就要设置专门的函数入口 get set
"""

# 总得来说,类和对象  就是鸡和蛋的关系 鸡能访问蛋,蛋却管不了鸡
Person.showage()
print(Person.__age)
"""
静态方法  很类似类方法,依赖于装饰器    Person.调用   即---直接改类的模板用,静态和类的作用 区别不大.
1.需要装饰器@staticmethod,内部是没有cls的,调用只能手动Person.   手动类名调用  。区别就两个
2.静态方法无需传递参数(cls,self),要传也可以传,但cls和self是不需要的
3.也只能访问类的属性和方法,对象的是无法访问的
4.加载时机同类方法



总结:读源码会看到  区别:
1.装饰器不同
2.类方法有参数,静态方法没有参数
相同
1.只能访问类的属性和方法,对象的是无法访问的
2.都可以通过类名调用访问.
3.都可以在创建对象之前使用,因为不依赖于对象

普通方法(实例方法，对象方法)和两者区别
不同:
    1.没有装饰器
    2.普通方法永远要依赖对象,因为每个普通方法都有一个self
    3.只有创建了对象,才可以调用普通方法(普通方法=对象方法),否则无法调用
    
"""


class Student:
    # __age=18 #类属性
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__score = 59  # __私有化以后  外面能打印查看,但是没有权限修改

    def __str__(self):
        return '姓名:{},年龄{},考试分数{}'.format(self.name, self.age, self.__score)

    def fix_score(self, temp):
        self.__score = temp


s = Student('cx', 18)
s.age = 21
s.score = 95  # 无法修改,只能在类的对象方法内部进行修改
s.fix_score(95)
print(s)  # 私有化后,打印可以打 但是单独要取__age 也是没法取的,打印能打的原因是由于__str__是类内部方法
print(dir(Student))
print(dir(s))  # 看不到私有的__name,能看到,就是能调用的,看不到,就没法调用
# print(dir())  dir就是拿到各种函数,和系统自带的Artubute ,为什么访问不到,因为底层自己会进行改名_Student__name,所以私有并不是真的私有
# 要访问还是能访问的
# print(s.__Student__age)  可以但不建议
print(__name__)
print(s.__dir__())  # 用于返回对象的属性和方法的列表。
