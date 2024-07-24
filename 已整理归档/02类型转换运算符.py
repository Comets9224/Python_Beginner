# def convert_input(user_input):
#     try:
#         # 尝试将输入转换为整数
#         return int(user_input)
#     except ValueError:
#         try:
#             # 如果不能转换为整数，尝试转换为浮点数
#             return float(user_input)
#         except ValueError:    #ValueError是关键字
#             # 如果既不能转换为整数也不能转换为浮点数，返回原始字符串
#             return user_input
# account=100.1
# #hostname=input('please input hostname:')
# #hostFirstname=input('please input hostFirstname:')
# money=input('please input money:')
# #print(type(money))
# #print(type(int(money)))#输入money为带小数点的字符串'12.3' 能否转成int?   答:会返回错误值
# money=convert_input(money)
# #name=hostFirstname+hostname
#
# #print('Now hostname:',name,'Now account :',account+money)
# #print('Now account :',account+money)
#
# #留下了一个问题: 输出结果后带有众多位数的小数.留到后面学到输出格式控制解决
#
# #字符串带浮点 转不了int ,但是float转int是没问题的.
#
# intnum=10
# floatnum=9.9     #强制转换会进行截断
# print(float(intnum))
# print(int(floatnum))
#
# #进制转换  print(int(num),8)  8进制   表示8进制数  转int
# # 使用int()函数进行类型转换时，还可以传入两个参数，第二个参数用来表示进制。
# print(int("21",8))  # 输出的结果是17.八进制的21,对应的十进制数字是17
# print(int("F0",16)) # 输出的结果是240.十六进制的F0,对应的十进制数字是240
# #print(float("F0.F",16)) # 会报错  因为int支持基数转换,int函数能够写两个参数,但是float不支持两个参数
# #基数转换是将一个数从一种数制（基数）表示转换为另一种数制表示的过程。

# 转布尔类型
'''在Python中，只有空字符串****`'',""`，数字0，空字典{}，空列表[]，空元组()，和空数据None会被转换成为False，
其他的都会被转换成为True'''

# #键盘输入一个三位数的整数打印个十百位数
# num=int(input('请输入一个三位数:'))
# print("个:",num%10,"十:",num//100%10,"百:",num//100)#需要用到整除  / 会返回浮点
#
# #赋值运算符
# #+=，-= //= **=
# #关系运算符 > < <= >=  != is

# 输入考试成绩判断优秀   浮点数和int能比较吗  答：能
score = float(input("please input the score:"))
if score >= 90 :
    print('优秀')
elif 90>score>=60 :
    print('及格')
else:
    print('不及格')

# #逻辑运算符
# a=1
# b=3
# print(a and b)#and两边如果都是数值，都非0，输出为数字值