import os
print('错误和异常处理:')
"""
语法错误和异常
异常:运行会遇到的问题,程序的鲁棒性问题，出现了异常，下面语句都不会进行了
我们要做的是，当异常时，能够避免报错
#异常处理:
    try:
        可能出现异常的代码
    except 报错类型1:
        如果出现异常执行的代码
    except 报错类型2:

    finally:
        finally不是必须的，finally是无论最后有没有出错都会运行的代码


        try能单独使用吗？  用try语句 不会报错，程序能继续进行下去
except 后面接报错的类型
多个except 能够联合使用，因为try内有多个异常，只用一个except 是不能精准定位到异常的
class ERROR  是一个类，错误是一种类。
class ArithmeticError(exception)    object就到头了#括号内是他继承的类
object->BaseException->Exception->其他(包括faildnotfound)分支分下去

写写了好几个error，但是有可能有些error你没办法预知，很多error都是exception过去的，所以可以直接
excep Exception:   就能够包括ERROR包括的很全了

#找except的顺序呢？
Exception 的辈分最大   顺序是从上往下的，  直接进exception了 不会进下面其他ERROR了，所以
辈分最大的，最好是往后放。

#那进了exception了  那我怎么知道exception的具体错误原因呢？
except Exception as err:
print('出错了',err)

如果使用了else,则在try代码中 不能出现return  ，try
                                            xxxxxx
                                            return
                                        else:
                                            xxxx
else到达不了了


#异常情况4
  finally: 里 通常放close()  不管是否报错，都需要执行close()
  else是只要不报错就会进的,
  try里声明的，stream到了finally里 ，就用不了了
    try:
        stream=open(file)
        return 1
    finally:
        stream.close()   #stream定义在stream里，不能在finally里使用
       最好加判断
       finally:
                if stream:
                    stream.close()
                return 3
    如果try里没问题，return 1   finally比较特殊，只有运行完finally中 才，才会停止
    finally存在，优先finally，正常情况下，收到return立刻返回，遇到fannally后才会往外扔
    以上最后程序会return 3
    
    #当try中出现了问题，会继续执行try中后面的程序吗？
    当 try 块中的某一行代码引发异常时，异常会立即被捕获，
    并且控制流会跳转到相应的 except 块。因此，try 块中引发异常之后的代码将不会被执行。
"""


#抛出异常,主动抛出异常  raise 关机子 人为定义的raise
def register():
    username=input('用户名：')
    if len(username)<6:
        raise Exception('用户名长度必须六位以上')   #raise可不是return这些的，
                                                #是相当于系统一样的报错，会被抛出来   抛出来 后面else不进了
                                                #然后程序会进入到  except里  打印出错误的原因
                                               #except 意为 如果出错了怎么办？
    else:
        print('输入的用户名是：',username)


try:
    register()
except Exception as err:
    print(err)
    print('注册失败！')
else:
    print('注册成功！')

    #try里不报异常，正常就会往else里走

