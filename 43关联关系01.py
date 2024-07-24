""""""
"""
关联关系: 继承 is a, 包括has a  -----之前都是一个类里调来调去
现在涉及 一个类里 要用到另一个类里的信息
---->解决方法,r作为参数传过去  r是一个对象,在另一个对象内部 r.name  取出属性  .
当然内部不能直接写r.name   而是定义了形参,road  ,取也是取road.name


一个类里,也能调用另一个类的方法,但是要通过实例

总结:包含关系有两种方式,1.传递对象
                    2.在另一个普通方法中创建实例进行方法调用
-----------------------------------------------------------------------------------
不同类之间普通方法的调用如下:
class ClassA:
    def method_a(self):
        print("Method A from ClassA")

class ClassB:
    def method_b(self):
        # 创建 ClassA 的实例
        a = ClassA()
        # 调用 ClassA 的普通方法
        a.method_a()
------------------------------------------------------------------
不同类之间 类方法之间的调用如下:不需要实例,直接类名调用
class ClassA:
    @classmethod
    def class_method_a(cls):
        print("Class Method A from ClassA")

class ClassB:
    @classmethod
    def class_method_b(cls):
        # 调用 ClassA 的类方法
        ClassA.class_method_a()

# 使用示例
ClassB.class_method_b()  # 输出: Class Method A from ClassA

------------------------------------------------------------------
# 使用示例
b = ClassB()
b.method_b()  # 输出: Method A from ClassA


练习:

公路(Road)
    属性：公路名称，公路长度
车(car)
    属性:车牌,时速
    方法:
        1.这车牌再这条公路上的时速和行驶了多长
        get_time(self,road)
        2.初始化车属性信息__init__
        3.打印对象显示车的属性信息 __str__

公路和车,这两个类如何交互呢?
"""
import random
class Road:
    def __init__(self,name,len):
        self.name=name
        self.len=len

class Car:
    def __init__(self,brand,speed):
        self.brand=brand
        self.speed=speed
    def get_time(self,road):  #road与r是同一地址空间,意思是,当另外赋值了,换电视机里,整个家里的人都能看到.
        ran_time=random.randint(1,10)
        msg='{}品牌的车在{}上以{}速度行驶了{}小时'.format(self.brand,road.name,self.speed,ran_time)
        print(msg)
    def __str__(self):
        return f'{self.brand}品牌的,速度:{self.speed}'

r=Road('进藏高速',12000)
audi=Car('奥迪',120)
print(audi)

#把r对象当参数传到 动作里
print(r.name)
result=audi.get_time(r)#   把对象r传过去,在函数内取出r的属性  函数定义时定义的是形参road   函数内部就road.name
"""
(继承) is a 和 (包含)has a的区别是?
继承是类继承类   组成是类包含类  
----->举例来说 Person 类包含了Class，Doctor，Teacher  都有共同属于人的特性 这叫继承
----->像本次用到的  车和路的调用相互包含  就是has a   has-a” 关系确实描述了类之间的组合或聚合关系，即一个类包含另一个类的实例作为其属性。这个关系通常用于表示一个对象包含另一个对象。

"""