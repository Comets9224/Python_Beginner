#进程之间的通信   进程负责放东西，另一个取东西。
from multiprocessing import Process
from multiprocessing import Queue
from time import sleep


def download(q):
    imges=['girl.jpg','boy.jpg','man.jpg']  #平行进程，图片怎么传过去getfile()中？
    for image in imges:
        print('正在下载:',image)
        sleep(0.5)
        q.put(image)


def getfile(q):
    while True:
        try:
            file=q.get(timeout=3)  #往里面放了能立马取出，不放 那我就是阻塞的在这  可以传timeout等待
            print(f'{file}保存成功!') # getfile(file)进程只启动了一次就关闭了  一个进程结束q不用了 自动把q回收了，第二次还没等到打印，q就被回收了，想办法让进程等待
        except:
            print('全部保存完毕！')
            break
if __name__ == '__main__':
    #两个进程也别自定义了
    q=Queue(5)
    p1=Process(target=download,args=(q,))#传的是函数名，而不是调用的结果，不要加括号
    p2=Process(target=getfile,args=(q,))   #共用一个队列
    p1.start()
    p1.join()  #加join是为了阻塞   但加join变单线程了，所以改加while true 也能实现阻塞
    p2.start()
    p2.join()

    print('00000')  #000一直没打印
    """如何通信，通过队列拿取，引用同一个队列"""
