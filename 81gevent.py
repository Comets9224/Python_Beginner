#虽然greenlet实现了协程,但仍然需要人工切换,太麻烦了
#python还有一个gevent模块,原理是,当greenlet遇到IO  指的input output输入输出
#比如网络或者文件操作等情况时，自动会切换到其他的greenlet，等到IO完成，再适当的时候切换回来继续执行
#由于IO操作很耗时，经常使得程序处于等待状态，有了gevent，我们自动切换协程，就保证总有greenlet在运行，而不是等到IO
#而不需要手动switch切换
#什么是猴子补丁  monkypatch
from datetime import time
import gevent
from gevent import monkey
import time
#monkey.patch_all()  #打一个猴子补丁,那为什么要加猴子补丁呢?
#打了补丁 实现了ABC之间的自动切换
#gevent.sleep()#time里的sleep 对于gevent来说 是否是耗时操作是没感知到  猴子补丁就是底层切换了gevent.sleep()

def a():
    for i in range(15):
        print('A'+str(i))
        #time.sleep(0.1)
        gevent.sleep(0.1)

def b():
    for i in range(15):
        print('B' + str(i))
        #time.sleep(0.1)
        gevent.sleep(0.1)   #只要有sleep被gevent检测到,就会自动切换

def c():
    for i in range(15):
        print('C' + str(i))
        #time.sleep(0.1)
        gevent.sleep(0.1)
if __name__ == '__main__':
    g1=gevent.spawn(a)
    g2=gevent.spawn(b)
    g3=gevent.spawn(c)
    #gevent有一个特点,主进程完事了  gevent都不工作了,需要加塞
    g1.join()
    g2.join()
    g3.join()
    print('-------------')
