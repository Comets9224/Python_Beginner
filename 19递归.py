# def test(i):
#     if i<10:
#         i+=1
#         print('aaa')
#         test(i)
#
# test(5)

#递归里变量怎么运行   参数i在函数内部是继承的 在i内部是全局的
#递归能实现循环
#遵循  递归必须要有出口    ------>出口就是  到没有递归动作的分支了
# 每次都要往出口靠近

def test2(i):
    if i==5:
        print('结束')
    else:
        print(i)
        i+=1
        test2(i)
test2(0)
"""
斐波那契数列
F(0)=0  F(1)=1  F(2)=F(1)+F(0)


"""
def F(i):
    if i<=0:
        return 0
    elif i==1:
        return 1
    else:
        return F(i-1)+F(i-2)

F(5)




def factorial(n):
    if n==0:
        return 1
    if n>0:
        return n*factorial(n-1)  #不定义n=0  n----减到0  就没值可乘了
v=factorial(5)
print(v)
