import sys


def a():
    for i in range(10):
        return #或者break 都会停止  如果有循环，结束了循环也结束了函数，return 可以单独使用
        print(i)
a()

def func():
    a=90
    a+=x   #x定义在func外面 但不会报错，因为这时候只是在加载，实际没调用

    print('--------->',a)
x=100
list=[]  #定义的全局变量
func()   #调用时候x必须在之前
print(globals())#查看全局变量   查看得到是一个字典，分成系统和自定义的全局变量


#可变和不可变 值和地址的关系
#不可变 int str tuple float bool
#可变 list dict set

#地址的引用:
#1.普通的赋值关系
#sys.getrefcount(object)   查看有几个指针指向object
#2.函数参数 看函数参数类型是可变还是不可变
#3.  传的如果是不可变类型 出了函数就会消除 ，如果传的是列表，列表修改 函数里对其修改，打印出来会改变
#函数嵌套
#闭包  1.必须是嵌套  2.内部调用了外部的变量  3.返回值是内部函数，装饰器用
