#列表推导式基本格式 最终得到一个列表
#格式： [i for i in 可迭代的]

list1=[i for i in range(1,21)]
print(list1)

list2=[i+2 for i in range(1,10)]
print(list2)

#1~100之间的所有偶数存放到列表中
list3=[i for i in range(0,101,2)]
print(list3)


#列表推导式格式2：  [i for i in 可迭代的 if 条件]
list5=[i for i in range(0,101) if i%2==0]
print(list5)

#把一个列表中所有的英文单词取出
list6=['hello','world','65','58','lucky','high']
list7=[word for word in list6 if word.isalpha()]
print(list7)
#格式3  [结果1 if 条件 else 结果2 for i in 可迭代的]
#把H开头的 首字母大写，不是h开头的，全部大写   列表推导，既有if 也要有else  if就要换位置了
list8=[word.title() if word.startswith('h') else word.upper() for word in list6 ]
print(list8)

#格式4，5  两个for循环 三个for循环的都有
#两个for循环的
a=[(x,y)for x in range(1,3) for y in range(3)]
print(a)

#三个循环的
a=[(x,y,z)for x in range(1,3) for y in range(3) for z in range (1,3)]
print(a)

#请写一段代码实现分组一个列表的元素  1~100[[1,2,3],[],[]]  使用列表推导式