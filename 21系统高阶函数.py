#函数也是一种数据类型  function类型  可以当变量使用
#一个函数可以接收另一个函数作为参数  叫不叫高阶函数 就看函数调用 传的是不是函数
"""
系统高阶函数： 排序 最大最小filter reduce max min  sorted


"""
from functools import reduce
m=max(5,9)
print(m)

m=max([2,4,5,6,9,8,7])
print(m)
list1=[('tom',19),('ross',15),('jack',25),('lily',13)]
m=max(list1,key=lambda x:x[1])  #相当于遍历列表
print(m)

s=sorted(list1,key=lambda x:x[1])
print(s)
s=sorted(list1,key=lambda x:x[1],reverse=True)
print(s)

rr=filter(lambda x:x[1]>20,list1)
print(list(rr))  #返回一个filter 类型的   扔到列表 强转列表


ma=map(lambda x:x[1]+1,list1)  #映射  提取出
print(list(ma))
ma=map(lambda x:x[0].title(),list1)  #映射  提取出
print(list(ma))

r=reduce(lambda x,y:x+y,[1,2,3,4,5])   #第一次会取出两个值   相加
print(r)

#####zip
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

zipped = zip(list1, list2)
print(list(zipped))  # 输出: [(1, 'a'), (2, 'b'), (3, 'c')]
