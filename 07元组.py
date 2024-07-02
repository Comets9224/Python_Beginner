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
#元组定死了  一开始就固定了  要添加的内容都是固定好了  非要改，把元组转成列表，强制类型转换
#强制转列表，其实已经不是原来的元组了

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


"""
王者荣耀角色管理系统
角色包含：姓名，性别，职业
修改角色属性
删除角色
查询单个角色
显示所有角色
退出系统
"""
# def changehero():
#     name=input('请输入需要修改的英雄名称:')
#     for inner in hero:
#         for name in inner:
#             print("")
#



import time
print('~~~~~~~~~~~~欢迎进入王者荣耀英雄管理系统~~~~~~~~~~~~~~')
hero=[['赵云','男','刺客'],['蔡文姬','女','辅助'],['姜子牙','男','法师'],['后裔','男','射手']]
while True:
    func=input('请输入你需要的操作(1修改角色属性/2删除角色信息/3查询单个角色信息/4显示所有角色信息/5退出系统):')
    if func=='1':
        heroname=input('请输入需要修改的英雄名:')
        modifyContent=input('请输入需要修改的内容1性别/2职业:')
        temp=input('请输入要修改成什么:')
        if modifyContent=='1':
            for i in hero:
                if i.count(heroname) !=0:
                    i[1]=temp
                    print(hero)
        if modifyContent=='2':
            for i in hero:
                if i.count(heroname) != 0:
                    i[2] = temp
                    print(hero)
    elif func=='2':
        herodel=input('请输入你要删除的角色信息:')
        if herodel=='-1':
            continue
        for i in hero:
            if i.count(herodel)!=0:
                hero.remove(i)
                print(hero)
    elif func=='3':
        herofind=input("请输入你要查找的角色信息:")
        for i in hero:
            if i.count(herofind) != 0:
                print("角色名：{} "
                      "性别: {}  职业:{}".format(i[0],i[1],i[2]))
    elif func=='4':
        for i in hero:
            for j in i:
                print(j,end=' ')
            print()
    elif func=='5':
        print('正在退出...')
        time.sleep(2)#需要导入time库   单位为秒
        print('已成功退出王者荣耀管理系统！')
        break
    else:
        print('输入错误，请重新输入')

