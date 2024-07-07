"""
匿名函数表达式
匿名函数名=lambda 参数列表:运算表达式
def test(a):
    return a+1

r=lambda a: a+1

r()   有参数a的  参数列表有a
返回值是 后面的运算表达式
"""

add=lambda x,y: x+y
print(add(1,2))

#匿名结合高阶函数 使用场合 作为参数使用 会用到
#这个函数平常也不会用到 只在这个高阶函数中用到的情况 就省略def
"""
hanshu(8,lambda x,y:x+y)    #与r=lambda x,y:x+y  hanshu(8,r)等价
"""
