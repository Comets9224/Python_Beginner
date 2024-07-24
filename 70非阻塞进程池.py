"""非阻塞进程池"""
import os
import time
from random import random

"""
当需要创建的子进程不多，直接利用，multiprocessing中的Process动态生成多个进程
但如果是生成上百个上千个，手动创建的工作量巨大，就可以利用multiprocessing提供的Pool方法
初始化Pool时，指定一个最大进程数，当有新的请求提交到Pool中，如果池没满，
那么会创建一个新的进程用来执行该请求。
但如果池中进程已经达到指定最大值，那么请求会等待，知道池中有进程结束，才会创建新的进程来执行

池满了，发过来的请求就不被执行了



提供了 ：阻塞式，非阻塞式
阻塞：一个一个加到池中，一个完了才做下一个
非阻塞：一次性，全部添加到，立刻返回，不等待回调,回调，立刻返回，指的是执行下一个等待的进程，返回队列，而并不等其他的池中进程完毕之后才结束，但是回调函数是等待任务完成(一个一个线程完成)之后（return完）后才来调用的
"""
from multiprocessing import Pool
#非阻塞式进程
def task(task_name):
    print('开始做任务啦', task_name)
    start=time.time()
    time.sleep(random()*2)  #随机时间
    end=time.time()
    #print(f'完成任务:{task_name},用时:{end-start},进程id:{os.getpid()}')  #os得到进程id
    return f'完成任务:{task_name},用时:{end-start},进程id:{os.getpid()}'
container=[]
def callback_function(n):#回调方法务必加参数   运行完进程后扔出返回值，才进行回调
    container.append(n)


if __name__ == '__main__':
    pool = Pool(5)   #最多只有五个进程，池子容量
    tasks=['听音乐','吃饭','洗衣服','打游戏','看孩子','散步','做饭']
    for task1 in tasks:#循环创建任务
        pool.apply_async(task, args=(task1,),callback=callback_function)   #async表示异步，非阻塞 执行任务
        # callback是回调方法   callback出来的东西会传给自己写的callback_func(n)  ,n 传入。  callback 传的n是task的返回值，所以要在task里加return
        #上面函数名task  这里apply——async如果传参数还是task，就会运行出错
        """在 Python 中，变量名和函数名共享同一个命名空间。如果你在 apply_async
         中传递参数名为 task，这个参数会覆盖掉外部定义的 task 函数。这样，当你调用
          task 函数时，Python 实际上会尝试调用这个参数，而不是你定义的函数
          ，从而导致错误。
          """
        #异步的申请  apply_async()   每运行一次主进程，就会创建一个进程，池子添加一个任务
        #会发现，没打印就结束了。——————————>因为pool和主进程是同生共死的，要挡住主进程不要进over
    pool.close()   #要加一个close，  表示添加任务结束
    pool.join()   #作用：插队，堵在主进程前，只有join完成，才能主进程继续走到over，否则走不到over
                   # 也就阻塞进程
    for c in container:
        print(c)
    print('over！！！！')  #设置了阻碍，over最后才打印，什么时候墙撤了，当池中任务都运行完了，结束

    """
    这种方式，可以看出，返回值一下进来了五件任务  
    七个任务，但是池只有五个空，进来一个创建一个进程，看着一个一个进 实际也是一起进
    任务五个进去了，开始休眠了，谁先醒不确定，五个平行，各干各的。结束了一个，后面进来一个,取代先前的进程号
    先前进程号被分配了新的任务，id号还是原来的id号
    
    开始做任务啦 听音乐
    开始做任务啦 吃饭
    开始做任务啦 洗衣服
    开始做任务啦 打游戏
    开始做任务啦 看孩子
    完成任务！用时: 0.08467459678649902
    开始做任务啦 吃饭
    完成任务！用时: 0.24828481674194336
    开始做任务啦 做饭
    完成任务！用时: 0.06898236274719238
    完成任务！用时: 0.7298226356506348
    完成任务！用时: 1.1968038082122803
    完成任务！用时: 1.4535129070281982
    完成任务！用时: 1.7067391872406006
    over！！！！
    阻塞式特点：七个都加到队列里，五个满了等空的
    好处：七个任务用了五个池子，节省开销，进程池可以复用
    
    """




