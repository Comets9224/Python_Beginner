#元组相比列表，元组的元素不能修改包括（增删改）
#元组使用小括号()
#元组tuple的定义：  名=()   如果是一个元素，必须加逗号，才表示是一个元组
#不管是一个字符串 还是一个数字，这些情况加逗号才是元组
#以下三个元组的定义
import time

t1=()
t2=('a',)
t3=('a','b','c','d','a')
print(type(t1),type(t2),type(t3))
#下标和切片  -->注意下标不要越界   t1 是空的元组 就不能挑t1(0)
#逆序输出
print(t3[::-1])
#t3.index()  t3.index()   只有计数这两个操作，索引下标
#index 可以查找 也可以添加起始结束位置来查找
index=t3.index('a',1,5)  #如果不在区间内 index会报错，而且包左不包右的 这个区间
print(index)
#元组定死了  一开始就固定了

"""
list()-->转列表
tuple()--->转元组
"""

# t3=list(t3)
# t3.append('f')
# t3=tuple(t3)
# print(t3)
#如果你需要使用一个序列类型的
#数据作为字典的键，必须使用元组，因为字典的键必须是不可变的。


