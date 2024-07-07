"""

闭包
1.是嵌套函数
2.内部函数引用了外部函数的变量
3.返回值是内部函数  返回是一个函数
"""
def outer(n):
    a=10
    def inner():
        b=a+n
        print('内部函数',b )
    return inner  #没括号的
print(outer(5)) #返回值是一串地址  因为返回值是函数的地址   地址加括号可以调用这个rinner了
r=outer(5)    #当我还不想调用内部函数，外部函数运行时，先扔出去做一些其他操作
r()