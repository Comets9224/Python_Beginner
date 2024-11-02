"""图书管理
借书---->查询 书
换书---->查询 书
函数1.无参数 2.多个参数
默认值，在函数定义内，传了参数默认填了def sum(a,b,islogin=False,d=‘qianfeng’)  默认填好就不会报错  islogin 默认值参数，可以不填
普通参数只能放在默认值参数的前面  默认参数一般都放在最后
当中间隔了一个参数  比如我想改第四个参数。隔着第三个islogin，怎么办？
使用关键字参数   第三个空位 d=‘beike’   叫出他的名赋值，默认参数顺序都是固定的。

#参数是列表类型怎么传？

#可变参数 *args
**kwards
"""
#可变参数  -------参数个数可变的参数 *args   可以是*a  不固定
def get_sum(*a):  #*格式是不能变的
    s=0
    for i in a:
        s+=i   #元组能遍历
    print(s)  #打印出来是元组   所以用的时候就是元组调用
get_sum(1,2,3,5)  #打印出来 a 是元组
#打包
a,b,*c=1,2,3,4,5
print(a,b,c)
#拆包
a,b,c=(1,2,3)
print(a,b,c)  #a=1  ,b=2,  c=3
#参数过多怎么拆包
a,b,*c=(1,2,3,4,5,6)
print(a,b,c)    #可见既有拆包，又有装包
#列表怎么拆包赋值进去   *定义时候是装包  *调用时候是拆包  我本来还想转元组呢
#拆包是指将一个序列（如元组、列表、字典等）中的元素解开并分别赋值给多个变量。
#装包是传参数过程，传的都是分散的，自动会装成一个包放到元组里
#拆装包不能是字典
ran_list=[1,2,3,4,5,6,7,8,9]
get_sum(*ran_list)

#可变参数**kwargs   也用了装包 但是产生的包是字典，**kwargs  是关键字参数 ，必须接bookname='西游记'这样才能接
#才能封装到字典中
def show_book(**k):
    print(k)
    for k,v in k.items():
        print(k,v)
show_book(bookname='西游记')
#拆包怎么拆
book={'bookname1':'西游记','bookname2':'攻楼','bookname3':'三国'}
#show_book(**book)

#两个同时存在咋整？  既有*args 又有**kwargs
def show_bk(*a,**k):
    print(a)
    print(k)
show_bk('龙少','小芳',**book)

                        
#只要能放在for in 循环的 都是可迭代的 itreable
result="#".join(['a','b','c'])    #将a，b，c 用#链接起来
print(result)

#返回值  返回值有俩  return min max  如果return返回不是一个值，返回元组
a,b=(1,2)  #返回值是元组可以这么接
#a,b=return


#函数间的相互调用
"""

"""


"""
全局和局部变量
先找自身内部的变量，局部变量
全局变量 看能看全局 ，要调了用，改全局，没这个权限
任何函数都能读到全局，但改不了,要用global  才有权限改
"""
a=100
def test():
    global a   #让a有权限修改全局
    a-=10
    print(a)
test()

#那nonlocal的作用是？
#nonlocal 关键字
#nonlocal关键字用于在嵌套函数中声明一个变量，
#该变量存在于最近的封闭作用域中（但不是全局作用域）。
#这样做的目的是在内部函数中修改外部（但非全局）作用域中的变量。
def outer():
    x = "outer x"

    def middle():
        x = "middle x"

        def inner():
            nonlocal x
            x = "inner x"
            print("inner:", x)

        inner()
        print("middle:", x)

    middle()
    print("outer:", x)


outer()
#使用 nonlocal x 声明 x，这意味着
# inner 函数将使用最近
# 封闭作用域中的 x，而不是创建一个新的局部变量 x。

#停车场收费系统   停车时间 用随机数  进入时间0
#[{'车牌':[进入时间，出去时间]},{},.....]  1小时十块  超时五分钟内免费 超时五分钟按一小时算
#停车场变量  ----->全局变量

#list={'a':'123','b',456}
#if 'a' in list:          #是可以这样把键，key 这样遍历循环 看是否在里面的


#函数的注释
def a():
    """

    :return:
    """
#局部变量  内部声明的，每次都会用完被回收走


#多个return怎么写
def creat_nums():
    print('1')
    return 1
    print('2')
    return 2
    print('3')
    return 3
#return 的特点 ，只会返回1  return有结束的作用，return 了 函数就自动结束了 后面的函数体也就没用了
#如果函数有多个默认值，默认值要放在*args后面  **kwargs放最后面


#可变类型和不可变类型：
#可变类型是修改数据，内存地址不发生变化  ：列表，字典，集合
#不可变类型是,修改数据，内存地址，必定变化：数字，字符串，元组
