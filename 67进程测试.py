from multiprocessing import Process
from time import sleep
import os   #getpid方法
def task1(s,name):
    while True:
        sleep(s)
        print('这是任务1,PID:',os.getpid(),'PPID:',os.getppid(),'name:',name)  #ppid是副id

def task2(s,name):
    while True:
        sleep(s)     #休眠过程会把执行权让出去
        print('这是任务2,PID:',os.getpid(),'PPID:',os.getppid(),'name:',name)
number=1
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
        if number==100:
            p.terminate()
            p1.terminate()
            break
        else:
            print('this:',number)
    """进程创建的总结:
    from multiprocessing import Process
    
    
    process = Process(target=函数,name=进程的名字,args=(给函数传递的参数))
    #创建了process对象
    #对象调用方法
    process.start()   启动进程并执行任务
    process.run()    只执行任务,但没有创建进程
    terminate()        终止
    
    
    
    
    """