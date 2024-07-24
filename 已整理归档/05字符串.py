#（python的字符串赋值比C简单太多了）
# s1='hello'
# s2=s1
# s3='hello'
# s4='hello1'
# print(s1,s2,s3,s4)
# print(id(s1))
# print(id(s2))
# print(id(s3))
# print(id(s4))
# s1='world'#改变了hello，和原地址的连接间断了，s2赋的是最开始的地址。
# print(s1,s2,s3,s4)

#字符串切片
s1='abcdefg'   #index 是索引
print(s1[0:7:2])#0 1 2 包左不包右
print(s1[:5])#0 1 2 包左不包右
s2='https://www.msbd123.com/sites/1694.html'   #index 是索引
print(s2[-1:-3])#0 1 2 包左不包右
print(s2[-4:])#0 1 2 包左不包右  (到结尾，也可以省略，同样包前不包后)
"""
#两个机制
正向0~len(s)-1
反向-len(s)~-1
从前边截取可以省略0
直接print(s[:5])
"""
print(id(s1[:]))
print(id(s1))   #地址是同一个
#取abcdef的中间 不要两头
s3='ABCDEFG'
print(s3[1:-1])
print(s2[-5:])
print(s3[::-1])#从头到尾倒着取
print(s3[-1::-1])#从头到尾倒着取

#-1 表示方向是负着走  那么也要注意 从哪到哪  现在是倒着走了 如果从哪到哪不改  就取不到任何值
#倒着走  [0,-1]     A  就是0   倒着走 ，根本数不到-1  应该是-1数到0

#字符串的查找  find index rfind rindex   find 从左往右找，找到一个符合的，就返回位置，没有找到任何符合要求的则返回-1
path='https://www.msbd123.com/sites/1694.html'
i=path.rfind('.')
print('thisis',i)
if i!=-1:
    print(path[i+1:])
#找一个字符串 有几个点的符号  count函数
j=path.count('.')
print(j)
#find和index的区别  index如果没找到 会报错，不会返回-1
#find查一个词也可以  可以查一个词，但是返回值是第一个字母的位置
i=path.find('msb')
print(i)

"""模拟文件上传，键盘输入文件名 判断文件名是否大于6位以上，拓展名为jpg，gif，png格式
如果不是，则提示上传失败。如果名字不满足条件，而拓展名满足条件则随机生成一个六位数的数字文件名，打印成功上传xxxxxx.png
判断名字

"""
import random
# i=random.randint(100000,999999)
# file=input("请输入文件全称:")    #直接用endwith可以判断
# pospot=file.find(".")
# if pospot!=-1:
#     filename=file[:pospot]
#     if file.endswith('jpg') or file.endswith("png") or file.endswith("gif"):
#         if len(filename)<6 :
#             filename=str(i)+'.'+file[pospot+1:]
#             print(filename)
#         else:
#             print(filename+'.'+file[pospot+1:])
#     else:
#         print("文件上传失败")


#验证码产生字母和数字的组合
# ku="zxcvbnmasdfghjklqwertyuiop123456789ZXCVBNMASDFGHJKLQWERTYUIOP"
# for j in range(6):
#     i=random.randint(0,len(ku)-1)
#     print(ku[i],end="")

"""
用户名或手机号码登录+密码
号码admin123   18267443446  200325
用户名：全部小写，首字母不能是数字，长度必须6位以上
手机号码：纯数字  长度11
符合 则登录成功，否则登录失败
"""

# username='admin123'
# password='200325'
# phonenum='18267443446'
# user=input('请输入用户名/电话号码:')
# if user== username or user==phonenum :
#     if user.lower():
#         userword = input('请输入密码:')
#         if password=='200325' :
#             print('登录成功！')
#         else:
#             print("密码错误登录失败!")
#     else:
#         print("用户名必须全部为小写，请重新输入！")
# else:
#     print("不存在该用户,请重新输入！")


#字符串替换   replace(old,new,count) 默认全部替换   #返回值是替换后的字符串，原字符串没有改变
s="cc说xx你来唱歌吧！"
result =s.replace('cc','***')#返回值是替换后的字符串，原字符串没有改变
print(result)

#字符串切割  split('分隔符',最多切几刀)  返回值是一个列表，切割完了后的列表。sep默认使用空白字符（空格、制表符等）作为分隔符。
#s.title  把每个单词的首字母都转成大写

#空格处理
s='admin    '
print(len(s))
print(len(s.strip()))  #strip就是用来去除空格的
print(s.center(30))  #在30个字符中放到最中央的部分   rjust  ljust  分别是左右对其
#字符串拼接  join
s5='hello'
s6='world'
result=s5.join(s6)
print(result)
