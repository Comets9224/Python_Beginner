""""""
import time
import datetime
"""
datetime模块:  datetime是date的升级版
    datetime.time  表示时间   
    datetime.date  表示日期   （data是数据）
    datetime.datetime 日期时间   now() 当前时间
    datetime.timedelta  时间差   timedelta(days='', hours='', minutes='', seconds='')
    
datetime 模块提供了更全面的日期和时间处理功能，包括时间、日期时间、时间差异和时区处理。
date 模块主要用于简单的日期操作。
"""
import datetime
print(str(datetime.time.hour) ) #这是一个类，得创建一个对象才行
print(str(time.localtime().tm_hour))
#time.localtime()：获取当前本地时间，返回一个 struct_time 对象。
#.tm_hour：访问 struct_time 对象的 tm_hour 属性，获取当前时间的小时部分。
#因为date是类，所以要求创建对象

#datetime.timedelta()  允许两个时间不同 返回差值
timedel=datetime.timedelta(hours=2)#(weeks=3)  没有month的  最多只有week，可以封装一个 days 判断月份 有几天
print(timedel)

receive=datetime.datetime.now()
print(receive)#返回当前时区的时间
result=receive-timedel
print(result)   #时间差结合datetime.now()来使用
#缓存：数据库 redis或者mysql做缓存  缓存的数据  redis.set(key,value,时间差)  放三天，就在三天后自动清除
#用时间差 主要是做缓存 到期清除


