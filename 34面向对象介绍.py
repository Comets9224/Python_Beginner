"""
面向对象:
程序        现实
对象-------->现实中具体事物
现实中的事物------>转成电脑程序

世间万物皆为对象

面向对象的好处：

面向对象:
    类
    对象
    方法
    属性

    对象：
        zww的手机
        lp的手机
        cx的手机


        可见对象是一个集合   --->共同特征：有品牌，有颜色，有大小，有价格              动作: (打电话/发短信/上网/)
        类别：手机类
             学生类:
                zww lp cx hct
                特征：姓名，年龄，性别，身高，血型，婚否   ----->属性
                动作：刷抖音  敲代码  看书...           ----->方法
                多个对象----->提取对象的共同特征和动作------>封装到一个类中、
                程序开发--->先定义类

"""
#所有类名要求首字母大写，多个单词使用驼峰式命名  ----->此为约定俗成
"""
格式:
    class 类名[(父类)]:
        属性：特征
        方法：动作
    

"""
class Phone:  #python3 object
    # object 可以省略，默认都是继承到object

    #属性
    brand='xiaomi'   #类里有  之后每个Phone都会有brand   算是默认
    price=4999
    type='mate14'
    note='self----->'
    #类中方法：动作
                #种类  普通方法   类方法  静态方法  魔术方法 （系统自带，可以改写）
    #类里称def为方法名
    #def 方法名(self[参数,参数])
    def call(self):
        print('正在访问通讯录:')
        for person in self.address_book:
            print(person.items())
        print('self--------->',self.note)#<__main__.Phone object at 0x000001EC72418590>  可见是obj而不是class
                                    # self是当前对象本身,不是类地址和类地址有区别。对象本身指的是phone1 或者phone2
                                    #不同对象  传的对象地址是不同的
        print('{}正在打电话....'.format(self))

#python 特点，给一个空类都没问题
print(Phone)
cx=Phone()   #使用类，创建对象
print(cx)   #创建了一个cx对象在地址上<__main__.Phone object at 0x000002875DEFFB10>  利用Phone这个模子，产生一块新空间

#调用
print(cx.brand)

#如果手机是苹果  改
cx.brand='iPhone'
print(cx.brand)

#定义类和属性  （刚才只有属性）
class Student:
    #类属性
    name='cx'
    age=18
#使用类创建对象   对象=类名()

lp=Student()
lp.name='lp'    #------->先去自己类内部有没有属性，没有的话就去类里找
print(lp.name,lp.age)#对象属性不存在会报错
lp.gender='男'   #增加对象属性     赋值操作 动态改变对象属性
print(lp.gender)#对象属性不存在会报错

#单纯属性 还不能表示是一个手机的功能 还有有方法  要添加动作  -------->此处回到手机class添加

phone1=Phone()
print(phone1.brand)
phone1.note='this is phone1'
phone1.address_book=[{'159':'xiaowei'},{'138':'xiaowei'}]
phone1.call()
phone2=Phone()
phone2.note='this is phone2'
phone2.call()   #phone2调call,call里会把自己phone2扔进去
