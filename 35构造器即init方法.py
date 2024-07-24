#函数  和 类里面定义的成为方法  方法和函数用法是完全一样的
def func(name):
    print('name----->',name)

#方法里的self  在外面调用时候不用传参数,系统自己会把self传入

class Phone:
    #魔术方法之一  :魔术方法名 __名字__()
    def __init__(self):#初始化     只要创建对象 系统自动就会执行
        #那么创建时机如何呢?
        self.brand='xiaomi'   #和之前之间赋值到模板不同 init是针对对象  各自self调的  先前那个直接赋值的方法是直接存在模板,如果找不到想要的brand
                              #会去模板找,现在是直接在开辟的对象地址内 初始化创建brand 和price属性.现在打印Phone.price是打印不出的,因为没有单独配price
        self.price=4999
        print('init---------->')
        #动态的给self空间内添加两个属性brand,price
    def call(self):
        print('call--------->')
        print('价格:',self.price)
p=Phone()  #自动执行init
p1=Phone()
"""
1.找有没有一块空间Phone
2.利用Phone类，向内存申请一块Phone一样的空间
3.造完空间了，立马回到类里看，是否提供魔术方法 __init__ 
 如果没有,则执行下面动作,将开辟的内存给对象名p
 如果有__init__进入init,执行init内动作,此时init内的(self),创建的空间传给init了
4.再将内存地址赋值给对象p  init是在赋值给p之前的动作,此时此地址还不是p
"""

