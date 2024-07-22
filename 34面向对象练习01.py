"""定义一个 Car 类，具有以下属性：

品牌（brand）
颜色（color）
价格（price）
速度（speed）
定义以下方法：

start：打印“车已经启动”。
stop：打印“车已经停止”。
accelerate：接受一个参数，增加当前速度，并打印当前速度。
brake：接受一个参数，减少当前速度，并打印当前速度。
创建两个 Car 对象，分别设置不同的属性值，并调用它们的方法。"""


class Car:
    def __init__(self):   #用上init,那就是给对象初始化了,需要加self
        self.speed = 0
        self.cloro = 'red'
        self.price = 500
        self.brand = 'baoshijie'

    def start(self, init):
        self.speed = init  # 这样是改不了类的初始speed的
        print(f'car was started,init speed is {self.speed}')

    def stop(self):
        print('car was stop')

    def accelrate(self, speeda):  # 这里是形参名
        self.speed += speeda
        self.spee()

    def brake(self, speeda):
        self.speed -= 10
        self.spee()  # 方法之内在类里面调用

    def spee(self):
        print(f'{self.brand} 牌车,颜色为 {self.cloro},价格为 {self.price}, now speed is {self.speed}')

    def user_hoost(self):
        print(f'当前车主是{self.user}')

Car.speed = 50  # 修改类的属性 用类名直接调

car1 = Car()
car2 = Car()
car1.start(30)
#TODO:如果初始化想往里面传这个车牌子呢？
#如果是需要初始化就传参数，必须要通过__init__  ,其他情况可以自由传入 通过调用方法
#方法传参
#如果不用format呢？  用f'a is {speed}'
print('-------------')
car2.spee()
print('-------------')
car1.accelrate(30)

#__init__是动态创建动态分配的,如果初始化了 后续调用 比如 没有user会怎样?
car2.user='zhang'       #没有不会报错,会创建   ,如果要打印的没有,则会报错.
car2.user_hoost()
