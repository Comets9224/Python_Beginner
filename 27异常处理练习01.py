"""
练习描述
编写一个Python程序，该程序将从用户那里获取两个数字，并尝试进行除法运算。你的任务是处理以下可能的异常：

用户输入的不是数字（ValueError）。
除数为零（ZeroDivisionError）。
异常处理 的语句：
try:
    可能会报错的语句
else:
    如果没报错会执行的语句
except Exception as e:                  as e 能将错误返回出来
    如果报错了后的语句
finally:
    无论是否异常都会执行的语句


如果使用了else,则在try代码中 不能出现return  ，try
                                            xxxxxx
                                            return
                                        else:
                                            xxxx
else到达不了了
"""
def devide():
    flag=True
    while flag:
        try:
            x=float(input('请输入除数:'))
            y=float(input('请输入被除数'))
            result=x/y

        except ValueError as e:
            print('请重新输入，不要输入非数字类型字符'+',错误类型:',e)
        except ZeroDivisionError as e:
            print('请重新输入，分母不能为0'+',错误类型:',e)
        else:
            print(f'结果为{result:.3f}')
            flag=False
        finally:
            print('欢迎您下次继续使用本计算器！')
# 调用函数以运行程序
if __name__ == '__main__':
    devide()
