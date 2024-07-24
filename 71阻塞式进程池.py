from multiprocessing import Pool
import os
import time
from random import random


# 阻塞式进程池
def task(task_name):
    print('开始做任务啦', task_name)
    start = time.time()
    time.sleep(random() * 2)  # 随机时间
    end = time.time()
    print(f'完成任务:{task_name},用时:{end-start},进程id:{os.getpid()}')  #os得到进程id
    #return f'完成任务:{task_name},用时:{end - start},进程id:{os.getpid()}'

if __name__ == '__main__':
    pool = Pool(5)
    tasks = ['听音乐', '吃饭', '洗衣服', '打游戏', '看孩子', '散步', '做饭']
    for task1 in tasks:
        pool.apply(task, args=(task1,))  #阻塞式，用apply,且不需要回调，不需要callback函数
    print('over!!!!!')   #可见阻塞式进程优点没显示出来，如果阻塞，就没必要进程池了  有id的复用
    """
    解释:仅仅省去了手动创建的的时间，跟队列无关了，没有队列所以没有callback等，也不需要join 和close
    阻在了函数添加的过程  添加到进程池的过程
    依次001  002  003  但实际上这个id都是空着的  每次进来都新建，直到进程池满了(5个)，才复用
    特点，添加一个，执行一个，如果一个任务不结束，另一个就进不来
    
    
    进程池：
    pool=Pool(max)  创建进程池对象
    pool.apply_async(task, args=(task1,))
    pool.apply()
    
    pool.close()
    pool.join()   让主进程让步，主进程别做了，资源给我
    
    
    
    """