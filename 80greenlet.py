#为了更好的完成协程任务,python中greenlet,还有gevent
from greenlet import greenlet
import time

def a():
    for i in range(15):
        print('A'+str(i))
        gb.switch()
        time.sleep(0.1)


def b():
    for i in range(15):
        print('B' + str(i))
        gc.switch()
        time.sleep(0.1)


def c():
    for i in range(15):
        print('C' + str(i))
        ga.switch()
        time.sleep(0.1)
if __name__ == '__main__':
    ga = greenlet(a)  #括号一定记得不要添加
    gb = greenlet(b)
    gc = greenlet(c)
    ga.switch()   #a放到greenlet还没启动  要用ga.switch才启动   如果a没启动 a就会启动


