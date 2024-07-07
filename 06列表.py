
list1=['牛奶','面包','火腿','食盐','西瓜']
#获取列表，通过下标
print(list1[2])
#切片
print(list1[:2])  #输出结果是列表  list

for i in list1:   #结合for i in 循环
    print(i)
s='ssa4654sad41c2z146as5d4df1a21'
sum=0
for i in s:
    if i.isdigit():
        sum+=int(i)
print(sum)
list2=[]
list3=[]
#列表的增删改查
# su=0
# while True:
#     print("当前购物车里有:")
#     for i in list2:
#         print(i,end=' ')
#     print(" ")
#     name=input("请输入物品名进行结账:")
#     if name=='-1' :
#         break
#     price=int(input("请输入单价:"))
#     list2.append(name)
#     list3.append(price)
# for i in list3:
#     su+=i
# print("输入结束，总价为%d"%su)
"""
列表里可以放列表 [[],[],[],[]]
for i in list:
    print('{}\t{}\t{}\t'.format(i[0],float(i[1]),int(i[2])))


"""

"""
列表删除：pop  remove clear
pop(index)  根据下标删除元素   默认删除(-1)  最后一个位置  有返回值，返回值是被删除的元素，默认从后往前删除  
要删除的元素不存在就会报错
del(index)删除索引处的元素
remove(内容)  删除列表中匹配到的第一个匹配项，没有返回值。   remove要配合判断，以免报错。
remove()   如果用来删除两个连着的会误删，我猜测是因为下标的原因
"""

#判断是否存在在列表里，先判断再删除免得报错
if "牛奶" in list1:
    print("exit!")
else:
    print("not exit!")

list4=['牛奶','辣条','牛奶','牛奶','番茄']
for k in list4:
    if k == "牛奶":
        list4.remove(k)

print(list4)   #为什么连着的删除会漏掉一部分？  下标  怎么办呢
"""
在遍历列表并删除元素时，直接修改列表会导致遍历行
为不可预测。可以通过创建新列表、倒序遍历或使用whil
e循环等方法来解决这个问题。s
"""

#insert()  function   usage : list.insert(1,'this is want to change thing')
list5=['牛奶','辣条','牛奶','牛奶','番茄']
def change(c,a,b) :
    c.insert(a,b)
    c.pop(a+1)
print(list5)
change(list5,2,'红牛')
print(list5)
list5[2]='土豆'#直接这个位置修改的方式
print(list5)


#如果说元素比较多，难道也一个个去数位置吗？
#list也有index函数，index only find the first object，if find the target will stop search  ，return index position
weizhi =list5.index('土豆')
list5[weizhi]='还是牛奶吧'
print(list5)

list5.clear()
print(list5)


#查找元素是否存在  三种方式
"""
list.index(obj)   找这个元素的第一个下标  --->没有该元素会报错
list.count(obj)  查找这个元素出现的次数--->返回次数
或者  'obj'  in  list  查找  返回布尔类型
"""

list6=['牛奶','辣条','牛奶','牛奶','番茄']

print(list6.index('辣条'))
print(list6.count('牛奶'))
if '番茄' in list6:
    print('exit')
#删除
del list6[2]
print(list6)


#当list6 =list7  实际上是把6的地址给了7  如果在7后面追加一个值，结果会是  6，7后面都追加这个值
list7=list6
list7.append("这是7追加的")
print(list6,list7)

#del函数  删除的是指针，原来的空间不会删除，指针删除后，变量名也会回收
a='hello'
b=a
c=b
del a
print(b,c)


#生成8个20以内随机数 ，保存到列表中
# import random
#
# list8=[]
# for i in range(8):
#     num = random.randrange(0, 20)
#     list8.append(num)
# print(list8)

#对列表进行反向和排序
#排序sort  默认是升序，默认是从小到大，反向 reverse
# list8.sort(reverse=True)   #默认reverse是False
# print(list8)

#list.reverse是对原有列表的前后顺序的反转，但不会排序
#列表操作，没有返回值，就是在原列表上操作的。
"""
生成8个1-100之间的随机整数，保存到列表中
键盘输入一个1-100之间的数，将这个数插入到排序后的列表中

"""
import random

list9 = [5, 17, 2, 65, 42, 1, 98, 32]

inp = int(input("键盘输入一个0-100内的整数: "))

# 生成并添加7个随机数到list9
for i in range(7):
    shu = random.randint(0, 100)
    list9.append(shu)

# 对list9进行排序
list9.sort()
print("排序后的列表: ", list9)

# 将输入的整数插入到排序后的列表中
inserted = False
for j in range(len(list9)):
    if list9[j] > inp:
        list9.insert(j, inp)
        inserted = True
        break

# 如果输入的整数大于列表中所有元素，则将其添加到末尾
if not inserted:
    list9.append(inp)

print("插入后的列表: ", list9)
