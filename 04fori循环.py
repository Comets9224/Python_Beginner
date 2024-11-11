# sum=0
# for i in range(1,51):#range是序列
#     sum+=i
# print(sum)


#输入三次用户名秘密，如果错误三次 锁定，三次以内成功则成功
# name='zhangwenwei9224'
# word='1231'
# flag=0
# for i in range(3):
#     username=input('请输入用户名:')
#     password=input('请输入密码:')
#     if username==name and password==word:
#         flag=1
#         break
#     else:
#         print('账户或密码错误，已输入%d次'% (i+1))
# if flag==1:
#     print('登录成功！欢迎登录')
# else:
#     print('三次输入错误，已锁定')

#老虎机
#葡萄1  苹果3   西瓜5  火龙果10   哈密瓜20
# import random
# flag=1
# coinage=20
# while(flag==1):
#     if coinage>0:
#         ifgame=input('是否开始游戏y/n:')
#         if ifgame=='y':
#             putao=int(input('请输入押注葡萄1的金币数量:'))
#             coinage-=putao
#             pinguo = int(input('请输入押注苹果3的金币数量:'))
#             coinage -= pinguo
#             xigua= int(input('请输入押注西瓜5的金币数量:'))
#             coinage -= xigua
#             huolongguo =int( input('请输入押注火龙果10的金币数量:'))
#             coinage -= huolongguo
#             hamigua= int(input('请输入押注哈密瓜20的金币数量:'))
#             coinage -= hamigua
#             num=random.randint(1,101)
#             if num<=50:
#                 coinage+=putao*1
#                 print('恭喜你押中了，获得了%d个金币,目前你还有%d个金币'%(putao*1,coinage))
#             elif 50<num<=75:
#                 coinage += (pinguo* 3)
#                 print('恭喜你押中了，获得了%d个金币,目前你还有%d个金币' % (pinguo * 3, coinage))
#             elif 75<num<=85:
#                 coinage += (xigua * 5)
#                 print('恭喜你押中了，获得了%d个金币,目前你还有%d个金币' % (xigua * 5, coinage))
#             elif 85<num<=95:
#                 coinage += (huolongguo* 10)
#                 print('恭喜你押中了，获得了%d个金币,目前你还有%d个金币' % (huolongguo * 10, coinage))
#             elif 95<num<=100:
#                 coinage += (hamigua * 20)
#                 print('恭喜你押中了，获得了%d个金币,目前你还有%d个金币' % (hamigua * 10, coinage))
#         else:
#             flag=0
#             print('当前金币%d'% coinage)
#     else:
#         print('金币不足，不能游戏！')
#         flag=0
#只要中断过了就不会进入else
# for i in range(10):
#     print(i)
# else:
#     print("successful")   #当所有的for i 都执行完了，没有出现break等等中断的 就会进入到else中
j=0
while j<5:
    j+=1
    print(j)
    if j==3:
        break
else:
    print("successful")
"""while和for与else的使用(while ...else  和for  else)  和c语言不同全部运行完没break过才会走else"""

