# 对于进程:自定义
from multiprocessing import Process
class MyProcess(Process):    #这个就是自定义进程,怎么写 就重写run和init 并且要继承父类的程序
    # 只要是进程线程,都要重写run
    def __init__(self, name):

        super(MyProcess, self).__init__()
        self.name = name
    def run(self):  # 只要调start,就会默认进run
        n = 1
        while True:
            print(f'I am a child process自定义进程:{self.name}\n')


if __name__ == '__main__':
    p1 = MyProcess('小明')   #底层process:必须为空   基础用父类,就应该传父类所有的参数
    p1.start()

    p2 = MyProcess('小红')
    p2.start()
# 1.开新进程
# 2.run()
#没准 调100下1  才调100下2  都是CPU说了算
