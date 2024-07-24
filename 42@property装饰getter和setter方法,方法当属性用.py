# 开发中,常用的私有化处理-装饰器   _____将私有的像没私有的一样,而且还能加判断
# 有先后顺序,property装饰  getter方法，  有getter方法才能有setter方法
class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    @property  # property是一个类,把类装成一个装饰器,dir  可以看到底层,把age当成属性用,不用加括号,像使用name一样
    def age(self):  # @property装饰器将age方法变成了一个getter方法，这样我们可以通过s.age来获取年龄，而不是s.age().
        return self.__age  # @property装饰器主要用于将一个方法转换为属性，从而使得我们可以像访问属性一样调用该方法。这通常被称为getter方法，因为它用于获取属性的值。
    # return 是必要的 ，但返回到可以不是self.age   可以是self.age修改后的东西  但是如果没有return  getter返回值是None
    # 没有getter无法定义setter
    @age.setter  # 通过定义setter方法，我们告诉Python该如何处理对属性的赋值操作。   ，需要和上方的getter同名，但可以不是和上面变量__age同名
    def age(self, age):  # setter方法的主要职责是接收一个新值并将其赋给相应的属性。   一般只传一个属性,多的元素可以用元组之类的
        if age > 0 and age < 100:    #上面property def age 是没有参数的,而下面setter是有参数的,这参数是你需要接受值的  也就是接受等号后面的值
            self.__age = age
        else:
            print('不在规定范围内')
            """Getter方法（使用@property装饰器）不需要额外的参数，因为它只是返回属性的当前值。
                    Setter方法（使用@property_name.setter装饰器）需要一个额外的参数，这个参数表示你希望设置的新值。"""

    def __str__(self):
        return '姓名:{},年龄{},考试分数{}'.format(self.name, self.age)


s = Student('xc', 20)
s.name = 'cx'
print(s.name)

# 那能否s.age赋值一下呢
s.age = 30  # 会有问题  一定要先定义一个age(),在定义一个同名的age(),增加装饰器@ 同名.setter 才能给s.age命名,改了就没什么问题了

# 加一层装饰器,让内部私有化和没有私有化是一样的,怎么做呢?加装饰器
print(s.age)  # 正常情况下 调用age要  .age()
#print(s.__dir__())
