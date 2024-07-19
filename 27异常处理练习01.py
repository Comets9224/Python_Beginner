"""
练习描述
编写一个Python程序，该程序将从用户那里获取两个数字，并尝试进行除法运算。你的任务是处理以下可能的异常：

用户输入的不是数字（ValueError）。
除数为零（ZeroDivisionError）。
代码框架
以下是你可以使用的代码框架：

"""

def divide():
    while True:
        try:
            num1 = float(input("请输入第一个数字: "))
            num2 = float(input("请输入第二个数字: "))
            result = num1 / num2
            print(f"结果是: {result}")
            break
        except ValueError:
            # 处理用户输入的不是数字的情况
            print("输入无效，请输入数字。")

    # except ZeroDivisionError:
    #     # 处理除数为零的情况
    #     print("除数不能为零。")
    #
    # else:
    #     # 如果没有发生异常，打印结果
    #     print(f"结果是: {result}")
    #
    # finally:
    #     # 无论是否发生异常，都会执行的代码
    #     print("感谢使用我们的除法计算器。")


# 调用函数以运行程序
divide()
