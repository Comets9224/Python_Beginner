#is a   base 基类,也称父类
class Person:
    def __init__(self,name):
        self.name=name
        self.age=18
        print('这是父类的init')
    def eat(self):
        print(self.name+'正在吃饭...')
    def run(self):
        print(self.name+'正在跑步...')

class Student(Person):#加括号继承你想继承的父类
    def __init__(self,name):
        print('Student的init')  #报阴影,重写，以重写的为准
        #如何调用父类的init，再调用子类的init？
        super().__init__(name)#super表示找到上层的父类,父类init有参，如果现在不传参，会报错
class Employee(Person):
    pass
class Doctor(Person):
    pass
s=Student('jack')  #  Person继承到object类  __new__ 也都不需要重写
s.run()
e=Employee('tom')
d=Doctor('lily')
d.run()
"""继承后需要怎么去执行：
Student,Employee,Doctor---->都属于人类
相同代码，代码冗余，可读性不高，将相同代码提取出，放到一个person父类
让上述三个类都去继承Person,

class Student(Person)
    pass
如果继承后，子类又定义init，会有什么情况
"""
