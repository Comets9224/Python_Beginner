from multiprocessing import Process
from time import sleep
import os   #getpid方法
m=1   #看多进程是否能 共享公共变量   主进程和子进程是平行的
#运行后发现  当子进程运行起来 自己单独有个自己的地址放m  输出的m都是不同步的
#跟m是不是不可变对象无关 ,都会再进程造一份
"""
#运算类拿进程做,下载用线程做
#两个任务都在跑 ---->谁先谁后没意义   知道轮询即可
#代码的加载 都是主进程运行的   创建了不代表有进程了  start才能算有进程了
#两个进程是争夺一个CPU的，是由CPU处理的
"""
def task1(s,name):
    global m
    while True:
        sleep(s)

        m=m+1
        print('这是任务1,PID:',os.getpid(),'PPID:',os.getppid(),'name:',name,'m value:',m)  #ppid是副id

def task2(s,name):
    global m
    while True:
        sleep(s)     #休眠过程会把执行权让出去
        m=m+1
        print('这是任务2,PID:',os.getpid(),'PPID:',os.getppid(),'name:',name,'m value:',m)
number=1   #主进程启动两个子进程,两个子进程来访问公共变量
if __name__ == '__main__':   #从上往下运行 是主进程  task1和task2都是子进程
    #所以都是先运行完了主进程,再运行子进程  先打印了两个任务的名,再进到子进程里打印 这是任务1  这是任务2
    p = Process(target=task1,name='任务1',args=(1,'aa'))   #创建一个进程    name 给进程起名用的
    #进程有参数怎么传?  要传可迭代的  ,传两个参数
    p.start()       #run只是让你做这个函数而已 想开辟进程,就要用start
    print(p.name)
    p1 = Process(target=task2,name='任务2',args=(2,'bb'))
    p1.start()
    print(p1.name)
    #由ppid相同,可见,任务1和任务2的线程都是由同一个副进程创建的
    while True:
        number=number+1    #通过主进程 次数,控制子进程关闭  通过主进程,终止子进程
        sleep(0.2)
        m=m+1
        print('main:',m)
        if number==100:
            p.terminate()
            p1.terminate()
            break
        else:
            print('number is now:',number)