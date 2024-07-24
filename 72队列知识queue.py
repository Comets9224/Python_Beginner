#多个进程之间  按部就班 互不干扰
#利用队列queue  在进程之间通信
"""队列的特点"""
#队列，先进先出
#栈，一头封着，先进后出，弹栈
from multiprocessing import Queue
q= Queue(5)
q.put('A')
q.put('B')
q.put('C')
q.put('D')
q.put('E')
print(q.qsize())
if not q.full():#判断队列是否已满   q.empty  判断空
    q.put('F',timeout=3)  #堵车了 放不进了  不会停止打印的  等待在这，阻塞住了
#队列满了，则只能等待：除非有‘空位’  否则一直阻塞
#如果多进程就好做了
else:
    print('队列已满！')
  #从队列中取出
print(q.get(timeout=0.5))
print(q.get(timeout=0.5))
print(q.get(timeout=0.5))
print(q.get(timeout=0.5))
print(q.get(timeout=0.5))
  #取啊取全取出，用empty判断是否是空

print(q.get(timeout=0.5))

q.get_nowait()#  不等，不阻塞了