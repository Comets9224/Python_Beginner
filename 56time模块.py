""""""
import time

"""
sys: sys.path   sys.version   sys.argv
time与datetime
radonm
time模块
"""
#1.时间戳
t=time.time()   #用于求时间差  前后想减    小数点后面是毫秒级别的
#time.sleep(5)   #休眠
t1= time.time()
print(t1-t)

#将时间戳 转成字符串
s=time.ctime(t)
print(s)   #转成字符串的日期  年月日了
#时间戳转元组的形式
t2=time.localtime(t)
print(t2)

#t1=time.strftime("%Y-%m-%d %H:%M:%S", t)
#将元组转成时间戳
t3=time.mktime(t2)
print(t3)
print('---------->')
print(t)
#将当前时间转字符串
s1=time.strftime('%Y-%m-%d',t2)   #t可以省略  t要接受的是元组时间，而不是时间戳
print(s1)

#将字符串时间转元组方式时间
s2=time.strptime(s1,'%Y-%m-%d')
print(s2)

"""
time模块:
重点: time()
     sleep()
     strftime('格式')   %Y  %m  %d  %H  %M  %S
了解:
    t2=localtime(t)    返回的是类似元组属性的，但不是元组，是一种包含时间信息的特殊对象        
    元组--->t.tm_year   t.tm_mon   t.tm_mday   t.tm_hour   t.tm_mday
    返回值可以如何得到:
    # 通过索引访问
    print(t[0])  # 输出年份，例如：2024

    # 通过属性名访问
    print(t.tm_year)  # 输出年份，例如：2024

"""