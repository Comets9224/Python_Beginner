import re
#起名的方式:(?P<名字>正则)  (?P=名字)
msg='<html><h1>abc</h1></html>'
result=re.match(r'<(?P<name1>\w+)><(?P<name2>\w+)>(.+)</(?P=name2)></(?P=name1)>',msg)
print(result)  #P里是你起的名字  实际上给(\w+)起了一个名字 name1  写法?P<name1>
#后面?P=name2 就是对前面name2处的引用
print(result.group(1))  #起名是写的时候 方便引用  实际上调用的时候 还是 分的一组一组 用group可以调
#标签需要前面和后面要一致,那么 用引用的方式\n  表示引用第n组的数据
#在分组的时候,还可以结合| 杠,表示或者
"""
总结re模块:
match   从头开始匹配
search  只匹配一次
findall  查找所有
sub  替换  sub('正则表达式','新内容',string) 替换
对后面string 进行正则表达式要求的查找 找到是数字,替换成新内容
替换的新内容可以是函数

split   result=re.split(r'[,:]','java:100,python:100')  在字符串中搜索遇到  逗号或者冒号(这里是逗号冒号)
就分割,将分割的内容都保存到列表中了
"""
print('---sub-----------')
def func(temp):   #这个函数得是传参数的,因为匹配的内容会作为参数穿进去   传进入到参数是  正则的类型,要.group取
    num=temp.group()
    num1=int(num)+10
    return str(num1)  #返回str进行替换 所以要return str
result=re.sub(r'\d+',func,'java:100,python:100')
print(result)
print('---split----------')
result=re.split(r'[,:]','java:100,python:100')
print(result)   #将分割的放到一个列表里
