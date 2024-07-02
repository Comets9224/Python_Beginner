print("helloworld")
#变量
#只能是字母数字下划线,数字不能开头,不能使用关键字,严格区分大小写,不能使用关键字
name='zhangwenwei'
age=19.5
print("name:",age)
print(type(name))

#字符串 单双三引号   单双引号是为了交叉使用 "他说:'吃的好饱'"
message='''李白
床前明月光,
疑是地上霜.
'''  #三引号 保留输出的格式
print(message)

#布尔类型 判断是否登录成功
islogin=True #真  蓝色,说明是关键字
print(islogin)
print(type(islogin))

#类型转换
age=20
name=input('请输入用户名:')  #input输入的都是字符串类型  内部是提示词
print('当前用户为',name,'年龄',age)

