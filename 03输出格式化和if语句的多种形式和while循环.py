# #格式化输出
# name='蔡徐坤'
# age=26
# print("我喜欢听"+str(age)+'岁的'+name+'唱歌！')
# print("我喜欢听%d岁的%s唱歌"%(age,name))  #%(age,name)
# money=99.95
# print("%d岁的%s一首歌挣了%.2f块钱"%(age,name,money))   #格式化输出同C
# print("{}岁的{}一首歌挣了{}块钱".format(age,name,money))  #第三种方法格式化
#

#进制转换
#十转二
# a=16
# print(bin(a))
# #十转八
# print(oct(a))
# print(hex(a))
# print(int(a))
# #别的进制转10
# b=0o30
# print(hex(b))
#
# #带符号的二进制的求十进制
# c=input('请输入一个随意一个binary数:')
# if c[0]=='0':
#     print("is active")
#     print(c)
#     print(int(c,2))
# else :
#     print("is negtive")
#     print(c)
#     #如果为负数
#     # 负数的情况，使用补码表示法
#     # 将二进制数转换为十进制数，然后减去 2 的 (len(c) - 1) 次方
#     print('-',end='')
#     print(int(c, 2) - (1 << (len(c) - 1)))

#-9 的表示 00001001 补码等于原码取反加一   包括符号位又要取反

#if 条件：
    #条件成立执行的语句
#随机数
# import random
# r=random.randint(1,5)
# a=int(input('请输入一个1~10内的整数:'))
# if(r==a):
#     print(r)
#     print('猜对了！')
# else:
#     print(r)
#     print('猜错啦！')

'''
循环 while for
'''
#石头剪刀布 决战到天亮
account=0
print('进入游戏，十分就结束')
import random
while(account<3):
    gamer=input('请输入石头、剪刀、布:')
    machine = random.randint(1, 3)
    if  machine==1:
        if gamer=='石头':
            print('电脑为石头')
            print('平局，当前分数%d'%account)
        elif gamer=='剪刀':
            print('电脑为石头')
            print('你输了,当前分数%d'%account)
        else :
            account+=1
            print('电脑为石头')
            print('你赢了，加一分，当前分数为%d'%account)
    if  machine == 2:
        if gamer == '剪刀':
            print('电脑为剪刀')
            print('平局，当前分数%d' % account)
        elif gamer == '布':
            print('电脑为剪刀')
            print('你输了,当前分数%d' % account)
        else:
            account += 1
            print('电脑为剪刀')
            print('你赢了，加一分，当前分数为%d' % account)
    if  machine == 3:
        if gamer == '布':
            print('电脑为布')
            print('平局，当前分数%d' % account)
        elif gamer == '石头':
            print('电脑为布')
            print('你输了,当前分数%d' % account)
        else:
            account += 1
            print('电脑为布')
            print('你赢了，加一分，当前分数为%d' % account)


print('积分达到%d  游戏结束'%account)