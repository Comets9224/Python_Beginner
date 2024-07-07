#装饰器 装饰带有返回值的函数
"""
原函数有返回值，装饰器的内部函数wrapper也要有返回值

"""
def decorate(func):
    def wrapper(*args,**kwargs):
        r=func(*args,**kwargs)
        print('预计装修费用是{}元'.format(r))
        print('刷油漆')
        print('铺地板')
        print('买家具')
        print('精装修房子')
        return 60000
    return wrapper

@decorate
def house():
    print('我是一个毛坯房...')
    return 50000
r=house()    #记清楚 house就是wrapper  返回值是wrapper的返回值，所以根本返回不出来
print(r)     #想要把60000返回出来，可以在wrapper上return r

#装饰器带有参数的情况  仅了解 不要求
# 定义带参数的装饰器生成器
def outer_check(time):
    print('---------->1')
    def check_time(action):
        print('--------------->3')
        def do_action():
            if time<22:
                return action()
            else:
                return "对不起，您不具有该权限"
        print('---------------->4')
        return do_action()
    print('------------------>2')
    return check_time

@outer_check(23)
def play_game():
    return '玩游戏'

"""
当带参数时，进行了两次调用，第一
次调用传了参数23，第二次才
把paly_game函数扔进去do action
赋值给了paly_game
r=out_check(23)
r=check_time------>check_time(play_game)=do_action
---------->带参多了一轮调用而已  比不带参多执行了一轮而已
"""