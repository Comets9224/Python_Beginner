#继承 is a, has a
"""
公路(Road)
    属性：公路名称，公路长度
车(car)
    属性:车牌,时速
    方法:
        1.这车牌再这条公路上的时速和行驶了多长
        get_time(self,road)
        2.初始化车属性信息__init__
        3.打印对象显示车的属性信息 __str__

公路和车两个类如何交互呢?
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
        return '{}品牌的,速度:{}'.format(self.brand,self.speed)

r=Road('进藏高速',12000)
audi=Car('奥迪',120)
print(audi)

#把r对象当参数传到 动作里
print(r.name)
result=audi.get_time(r)
#(继承) is a 和 (组成)has a的区别是?
#继承是类继承类   组成是类包含类