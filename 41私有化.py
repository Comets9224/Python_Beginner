#私有化
#用公有化的方法,去修改私有的属性,将修改的方法封装起来.
#创建的时候还是能修改的
#好处:可以添加判断.
#私有化就要设置专门的函数入口 get set
class Student:
    #__age=18 #类属性
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.__score=59#__私有化以后  外面能打印查看,但是没有权限修改
    def __str__(self):
        return '姓名:{},年龄{},考试分数{}'.format(self.name,self.age,self.__score)
    def fix_score(self,temp):
        self.__score=temp

s=Student('cx',18)
s.age=21
s.score=95  #无法修改,只能在类的对象方法内部进行修改
s.fix_score(95)
print(s)  #私有化后,打印可以打 但是单独要取__age 也是没法取的,打印能打的原因是由于__str__是类内部方法
print(dir(Student))
print(dir(s))  #看不到私有的__name,能看到,就是能调用的,看不到,就没法调用
#print(dir())  dir就是拿到各种函数,和系统自带的Artubute ,为什么访问不到,因为底层自己会进行改名_Student__name,所以私有并不是真的私有
#要访问还是能访问的
#print(s.__Student__age)  可以但不建议
print(__name__)
print(s.__dir__())

