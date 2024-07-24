#死锁----互相要用对方的资源
"""
开发过程中使用线程，在线程间共享多个资源的时候，如果两个线程分别占有一部分资源并且同时等待对方的资源，
就会造成死锁。
尽管死锁很少发生，但一旦发生就会造成应用的停止响应，程序不做任何事情。
胡
"""
import threading
from threading import Thread,Lock
import time
lockA=Lock()
lockB=Lock()
class MyThread(Thread):
    # def __init__(self,name):  系统默认给了name=1  你可以尝试重写
    #     pass   Thread-1获取了A锁
    def run(self):#start()
        if lockA.acquire():#如果获取到锁,就返回True
            print(self.name+'获取了A锁')
            time.sleep(0.1)
            if lockB.acquire():   #参数,一定要避免死锁,解决方式:timeout=0.1
                #解决方法1.重构代码方法
                #       2.添加acquire的参数  当超时  跳过
                print(self.name+'又获取了B锁，原来还有A锁')
                lockB.release()
            lockA.release()
class MyThread1(Thread):
    def run(self):#start()
        if lockB.acquire():#如果获取到锁,就返回True
            print(self.name+'获取了B锁')
            time.sleep(0.1)
            if lockA.acquire(timeout=2):
                print(self.name+'又获取了A锁，原来还有B锁')
                lockA.release()
            lockB.release()


lock=threading.Lock()

if __name__ == '__main__':
    t1=MyThread()
    t2=MyThread1()
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('运行结束!')
    #让大家知道死锁 避免死锁