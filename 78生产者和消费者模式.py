"""
生产者与消费者:两个线程之间的通信
线程之间通信也是队列，但线程中称作：生产者与消费者
Python的queue模块中提供了同步的、线程安全的队列类，包括FIFO
（先入先出）队列Queue、LIFO（后入先出）队列LifoQueue、
和优先级队列PriorityQueue。
这些队列都实现了锁原理（可以理解为原子操作，即要么不做，要么就做完），
能够在多线程中直接使用。可以使用队列来实现线程间的同步。

FIFO先进先出  first in first out
LIFO后进先出  last in last out


"""
import threading
import queue
import random
import time
def produce(q):
    i=0
    while i<10:
        num=random.randint(1,100)
        q.put('生产者产生数据:%d'%num)  #往队列里放
        print("生产者产生的数据:%d"%num)
        time.sleep(1)
        i+=1

    q.put(None)   #放完了放None
     #done标识队列任务完成  用在队列的消费者看的
def consume(q):
    while True:
        item = q.get()   #队列的两头是put和get
        if item is None:
            break
        print("消费者获取到:%s"%item)#注意这里是%s  不是%d
        time.sleep(4)
        q.task_done()
#从结果上可观察到  产生了4个  才读取一个   这时候 先进先出的原则,  四秒后  生产者取到的是四秒前最先产生的
#发现,产生5个或四个情况都有  因为这时候四个产生 ,消费者即使已经不睡眠了,但是不是能叫到消费者 还是未知的 ,第五次叫可能还是生产者
#消费者醒了,也还是得排队

"""
消费者获取到的数据格式化问题：消费者获取到的item是字符串，而不是整数，所以 % d会导致错误。
q.task_done()的位置：q.task_done()应该在consume函数的循环内，每次成功处理完一个item后调用，而不是在循环外。
队列的task_done用法：q.task_done()
是用来告诉队列，某个项目已经被处理完了，应该在每次q.get()后调用。
"""
if __name__=="__main__":
    q=queue.Queue(10)  #队列有是个空
    arr=[]
    #创建生产者
    th=threading.Thread(target=produce,args=(q,))
    th.start()
    #创建消费者
    tc=threading.Thread(target=consume,args=(q,))
    tc.start()

    th.join()
    tc.join()
    print("END")


"""
总结:  线程Thread
1.创建线程
    A.Thread(target=func,name='',args=()).start()   创建并且启动  进入就绪状态
        run()
        join()  让主线程让步
    B.自定义线程
    class MyThread(threading.Thread):
        def __init__(self,name):
            super(MyThread,self).__init__()
            self.name=name
        
         def run(self):
            任务写到这里
    t=MyThread('name')
    t.start()
2.数据共享
        线程数据共享和进程是不一样的,是共用数据的,互不干扰
        线程是共有一个数据----->数据安全性问题
        所以Python就加了一个GIL ---->伪线程
        如果想加锁怎么加?
        lock=Lock()
        lock.acquire()
        .....
        lock.release()
        -------->只要用到锁: 死锁的问题
        避免死锁(锁多了 有锁的顺序问题,就考虑死锁了)
3.线程间的通信:生产者与消费者
    生产者是一个线程,消费者也是一个线程
    import Queue
    q=queue.Queue(10)
    #创建生产者
    th=threading.Thread(target=produce,args=(q,))
    th.start()
    #创建消费者
    tc=threading.Thread(target=consume,args=(q,))
    tc.start()
    q.put()
    q.get()
    
    扩展:GIL问题
    
"""
