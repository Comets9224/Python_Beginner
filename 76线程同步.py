"""
共享数据:多个线程共同对某个数据修改,则出现不可预料的结果,
为了保证数据的正确性,需要对多个线程进行
同步:一个个完成,一个做完另一个才能进来.   也就是锁,为了使用多线程又保证数据安全性
效率就会降低.

解释器锁:保证数据安全性,但是解决不了速度和真正的多线程
java能实现真正的同步,多线程

但硬要实现简单线程同步:两个对象都有acquire和release方法,
对于每次只允许一个线程操作的数据,可以将其操作放到acquire和release方法之间

多线程优势:(不能保证数据安全)  在于可同时运行多个任务(至少感觉起来上这样)

但是为了避免数据共享时,数据存在不同步的问题,引入了锁的概念

想用锁,先拿到一个锁对象  lock=threading.Lock()
lock.acquire()  #请求得到锁
lock.release()  # 释放锁
只要释放,其他进程都无法进入运行状态,用了锁会降速


"""

import threading
import time
lock = threading.Lock()   #先得到一把锁
list1=[0]*10  #表示里面10个0
def task1():
    #获取线程锁,如果已经上锁,则等待锁的释放
    lock.acquire()   #如果这把锁被task2用了,那就阻塞了 得等锁释放  申请上锁的语句(这个锁有阻塞的功能)
    for i in range(len(list1)):
        list1[i]=1          #数据处理部分 放到锁里面
        time.sleep(0.5)
    lock.release()

def task2():
    #任务2里 不断往外取
    lock.acquire()#阻塞
    for i in range(len(list1)):
        print('------->',list1[i])
        time.sleep(0.5)
    lock.release()    #把这行去掉 不释放阻塞锁,发现也没有像想象中有0 有1  是因为操作数小,底层有全局解释器锁
if __name__ == '__main__':
    t1=threading.Thread(target=task1)
    t2=threading.Thread(target=task2)
    t1.start()
    t2.start()
    #怎么出来的值?
    t2.join()  #join函数能够使得被调函数在此线程在被调函数结束后才运行主线程
    t1.join()
    print(list1)

#我的程序都是先执行的写1  实际上线程调度所不确定的 可能先调用2  打印出的全是0   还有可能是全局解释器锁的缘故
#别人的程序先运行task2也是很可能的

#同步会带来一些问题?死锁  请看下节