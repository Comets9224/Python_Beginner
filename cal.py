#变量
num=100
name='cal'
#函数

def add(*args):
    if len(args) > 1:
        sum=0
        for i in args:
            sum=sum+i
        return sum
    else:
        print('至少要两个参数')
        return 0

def sub(*args):
    if len(args) > 1:
        minus=0
        for i in args:
            minus-=i
        return minus
    else:
        print('至少要两个参数')
        return 0
def mul(*args):
    if len(args) > 1:
        multi=1
        for i in args:
            multi=multi*i
        return multi
    else:
        print('至少两个参数')
        return 0
#类
class Cal:
    def __init__(self,num,name):
        self.name=name
        self.num=num
    def test(self):
        print('正在使用calculate进行运算...')
    @classmethod
    def test1(cls):
        print('类名能直接调用的方法')
def test():
    print('我是测试')
print(f'__name__:{__name__}')  #在自己模块中  __name__ 就是__main__
if __name__=='__main__':
    #print(__name__)   #打印出来__name__为__main__
    test()