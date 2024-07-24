#协程--->微线程
#进程>线程>协程
#进程：Process 线程：Thread 协程没有类，通过生长器完成
#协程的用处  耗时操作才用到协程   耗时操作：网络请求（下载和上传）p爬虫  其他IO操作——本地文件的读写  阻塞——Sleep也是耗时操作
#阻塞时赶紧切换
#所谓协程,只要耗时,里面进行切换   _当网不好,有延迟时候  这时候不能再等着,就要切换其他协程去 不让CPU闲着
#生成器 ：yield  只要一阻塞,就生成另一个yield
import time


def taskA():
    for i in range(3):#电影切3份
        print('A'+str(i))
        yield
        time.sleep(1)
def taskB():
    for i in range(3):#电影切3份
        print('B'+str(i))
        yield
        time.sleep(2)


#如果多任务 next一个个运行 有点困难  下一节使用greenlet
if __name__=='__main__':
    gA=taskA()
    gB=taskB()
    while True:
        try:#一直用next,只要生成不了就会报错 所以加上Try
            next(gA)   #生成器必须交替执行  不算严格的异步
            next(gB)
        except:
            break
