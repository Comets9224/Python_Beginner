#猫
class Cat:
    type ='cat'
    #通过__init__进行初始化特征
    def __init__(self,nickname,age,color):
        self.nickname=nickname
        self.age=age
        self.color=color
    def eat(self,food):
        print('{}喜欢吃{}'.format(self.nickname,food))
    def catch_mouse(self,color,weight):
        print('{}抓了一只{}kg的,{}颜色的大老鼠'.format(self.nickname,color,weight))

    def sleep(self,hour):
        if hour<5:
            print('继续睡觉吧')
        else:
            print('赶快起床出去抓老鼠去')

    def show(self):
        print('猫的详细信息:')
        print(self.nickname,self.age,self.color)
#通过对象调用方法
cat1=Cat('huahua',2,'grey')
cat1.catch_mouse(2,'黑色')
cat1.sleep(8)
cat1.eat('小金鱼')
cat1.show()
