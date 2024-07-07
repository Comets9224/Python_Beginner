class Person:
    name='张三'
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def eat(self,food):
        print('{}正在吃{}!'.format(self.name,food))

    def run(self):
        print('{},今年{}岁,正在跑步'.format(self.name,self.age))

p=Person('张三',15)   #默认会执行init  但是没传参   创建类,默认会传到init中

p.run()#只要创建对象的时候,传了值,就会送到init里去,init是魔术方法,传进来自己会赋值
#魔术方法能传参,那么内部普通方法也能传

p.eat('狮子头')  #直接调eat不行,因为eat在类里,需要通过对象p调用eat