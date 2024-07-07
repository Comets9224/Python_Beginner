# def foo():
#     print('foo')
# def func():
#     print('func')
# foo=func
# foo()  #realisty is func  because function has a verb also

#开放封闭 原则  封闭：原来的代码不要动   开放：还要能往上加

#闭包
def w1(func):
    def inner():
        #验证1
        #验证2
        #验证3
        func()
    return inner()
"""
@w1   #这就是装饰器  理解为毛坯房装修
def f1():
    print('f1')
"""
#定义装饰器
def decorater(func):  #装饰器必须传参数  装饰器的名字
    print('--------->1')
    def wrapper():
        func()
        print('刷油漆')
        print("铺地板")
        print("买家具")
        print("精装修房子")
        print('--------->2')
    return wrapper   #加括号是调用了 不能加括号扔出去

@decorater  #装修这个函数就 放到这个函数前面  发现并没有传参数  如果直接调用decorate，需要传参数
def house():
    print('毛坯房....')

#不能在原函数上修改
house()      #装饰器会在原函数后面进行执行

#装饰器的运行顺序是怎样的 ？
"""
1.走@decorate  ，但他的参数是什么呢？  把house----->func
2.print(----------1)    这时候没进到wrapper里  return回wrapper ，返回的是wrapper的地址
@让这个地址直接成函数调用  wrapper()   走到里面的func  func=先前的house  
3.print“毛坯房”
4.往下走，然后返回------2

装饰器是把要装饰的函数作为参数往 装饰器里扔  ，装饰完了，
实际house的地址发生了改变 不是原来定义的house了
 而是wrapper的地址返回给house了  house一括号house()  等于wrapper(),所以实际调用的是wrapper()   有无括号是不一样的
 所以 @decorate   等价于 house=decorate(house)
 装饰器的作用：调用一次装饰器，就能够记录在日志 调用过函数的记录
            函数执行时间统计:函数执行前记录下时间，执行后记录下时间
            执行函数前的预备处理
            权限校验等场景
            缓存
            在不改变原函数的情况下，拓展了函数的功能
            定义装饰器
            def xxx(yyyfunc):
                def zzz():
                    ....
                    yyyfunc()
                    ....
                    return aaa    #这里是返回值
                return zzz
                
                
                装饰：
                @装饰器函数名xxx  ---->  原函数zzz=装饰器xxx(原函数zzz)
                def zzz原函数():
                    pass
"""

#带参数的装饰器
def decorate(func):
    def wappe(*address,**kwargs): #传过来是元组  调用得拆包啊
        func(*address,**kwargs)#这里的*不是装包，是拆包。    #此时func是house  house里有参数，
        # 所以func也该有 不然会报错，
        # 但是house调用时候如果传了参数  wapper又没有参数
        # 又会报错  所以wapper参数 address   wapper(address)
        #那么func也该有address
        #三个地方都要有address  如果原函数有参数，装饰器内部也要有参数


        print('刷油漆')
        print("精装修房子")
    return wappe


@decorate
def house2(address):
    print('房子的地址在{}是一个毛坯房'.format(address))

house2('北京四合院')

#被装饰的函数如果有两个 参数呢   我估计要用到之前的*args
@decorate
def changfang(address,area):
    print('厂房在{}，面积有{}'.format(address,area))


changfang('东大街','1000')

@decorate
def hotel(name,address,area=40):
    print('酒店的名字是{}酒店地址在{}每个房间的面积是{}'.format(name,address,area))

hotel(name='十足',address='北京国贸')  #如果这样，name=‘value’的  不用**kwargs没法接的
hotel('十足','北京国贸')#如果这样，是可以接的

