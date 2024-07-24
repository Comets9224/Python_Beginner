#进程,线程:
""""""
"""
Process类
创建进程:
def func(n):
    pass
p=Process(target=func,name='',args=(),kwargs='')
p.start()  #进程开始,不能调run,run只是调进程,但是没开始

Class MyProcess(Process):  #要写自定义进程必须要继承Process

    def run(self):
        pass
p=MyProcess(target=func,name='',args=(),kwargs='')
p.start()

进程数据共享:

n=0

进程池:Pool

pool = Pool(4)    4是最大容量
阻塞式：apply(func,args,kwargs)
非阻塞式：apply_async(func,args,kwargs,callback=函数)   #图片下载,交给进程  ,但是图片渲染子进程做不了  渲染放到callback做但是没法访问到全局的,因为会单独开出一块空间
进程间通信:
Queue()
q=Queue(4)
q.put()
q.get()
q.size()
q.empty()
q.full()

线程:
包含关系
进程里放着多个线程,多个线程共用进程资源.

t=Thread(target=func,name='',args=(),kwargs='')
t.start()
GIL:全局解释器锁
python的线程是伪线程,并未真正实现快速切换,用python做线程,其实还是一样排着队

耗时:用线程
计算:用进程





"""
