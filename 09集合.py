"""
集合:底层是字典封装的 key不允许重复
set
特点:没有重复，无序的  每次顺序是变化的，不是固定不变的，不能用下标索引
定义集合

"""
# set1={'zhangsan'}#当里面元素不是键值对时，此时为集合类型
# print(type(set1))
#
# list1=[1,3,6,8,9,1,9,5]
# print(set(list1))   #强制转换  转完了还是{}    如果单独的一个元素，那么则是集合的符号  否则是键值对，就是字典了
#集合怎么声明空集合呢?  只能这样set声明
#set3=set()      注意是空集合这么定义  非空直接花括号就能定义了

#集合怎么添加元素.add函数
# set3.add("三体")
# print(set3)
# set3.add("三体2")
# print(set3)
# set3.add("三体")  #重复元素加不进去的
# print(set3)
#append  extend --->list
#add update ---->set   update 合并
#集合的移除  remove()  和discard
"""
产生字母数字验证码4位 5组，不允许重复
"""
import random
code=set()
lib='zxcvbnmasdfghjklqwertyuiopZXCVBNMASDFGHJKLQWERTYUIOP1234567890'
str=''
for k in range(5):
    for i in range(4):
        pos = random.randint(0,len(lib))
        str+=lib[pos]
        if len(str)==4:
            code.add(str)
            str=''
print(code)

#移除   remove 和discad     remove 如果不存在会报错   和discard如果不存在则什么都不做
set4={'a','b','c','d'}
print(type(set4))
set4.remove('a')
print(set4)
set4.discard('b')
print(set4)

#del删除能删除整个容器，但是删除不了里面的元素 因为没有下标没有key  而且又是随机的，根本不知道怎么变
#还有清空 clear
#set4.pop()   随机删除集合内的元素  我的理解为 pop删除最后一个，但是由于集合是随机的，所以展示出是随机删除

#集合还提供交集并集差集  交集intersection  并集union  差集difference

set5={1,2,3,4,5}
set6={3,4,5,6,7,8,9}
set5.intersection(set6)

#+ - *  集合能用吗？   不能
#能用 |并     &交      -差
