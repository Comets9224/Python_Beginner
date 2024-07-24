""""""
"""
is a   base 基类,也称父类
继承父类的方式1.整个继承---后续要修改只能是重写对应部分的__init__或者eat()   不光属性继承,所有动作也继承
            2.要用父类,但还要在父类里加点 是父类的拓展  super()
            3.super 不仅能调用父类中的属性,还能调用父类中的方法  super().eat
"""

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print('这是父类的init')
    def eat(self):
        print(self.name+'正在吃饭...')
    def run(self):
        print(self.name+'正在跑步...')

class Student(Person):#加括号继承你想继承的父类
    def __init__(self,name,age,clazz):
        super().__init__(name,age)#如何调用父类的init，再调用子类的init？#super表示找到上层的父类,父类init有参，如果现在不传参，会报错
        self.clazz=clazz
        print('------------')
        Person.eat(self)
        print('------------')
        #super().eat()
    def study(self,course):
        print('学生{}正在学{}课程'.format(self.name,course))
class Employee(Person):
    def __init__(self,name,age,salary,manager):
        super().__init__(name,age)
        self.salary=salary
        self.manager=manager
class Doctor(Person):
    def __init__(self, name, age, patient, patients):
        super().__init__(name, age)
        self.patient=patient
        self.patients=patients
s=Student('jack',18,'python111')  #  Person继承到object类  __new__ 也都不需要重写
s.run()
# e=Employee('tom',18,5000,'z')
# d=Doctor('lily',18,'zs','zz')
# d.run()
# s.study('python')
"""
super支持有参数 super(Doctor,self)  (类型,对象)  只不过底层,加了判断,判断是不是这个类型的
super().__init__()  和super(Doctor,self).__init__ 实际上是等同的,加了判断而已
往上找父类是按方法名找的,找到了就不再往上找了
1.如果类中不定义__init__,调用父类 super class的__init__
2.如果继承父类,也需要定义自己的__init__,调用super().__init__()去继承父类
3.如果父类有eat(),子类也定义了eat方法,默认搜索原则:先找当前类,再找父类
s.eat()
4.override:重写,覆盖,父类提供的不能满足子类需求,就需要在子类中,定义同名方法.这种行为称为重写
5.如果还需要父类的代码super().eat  能调过来    
6.子类的方法也可以调用父类的方法来帮忙 ,用super()函数   简单继承用  对象.eat()调用没问题,但是多重继承会存在问题

"""

