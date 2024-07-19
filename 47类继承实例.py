"""编写一个简单的工资管理程序，系统可以管理以下四类人：工人（worker）、销售员（salesman）、经理（manager）、销售经理（salemanager）。所有的员工都具有员工号、姓名、工资等级属性，有设置姓名、获取员工号、计算工资等方法。

工人：工人具有工作小时数和时薪的属性，工资计算方法为每天的小时数*时薪。
销售员：具有销售额和提成比例的属性，工资计算方法为销售额*提成比例。
经理：具有固定月薪的属性，工资计算方法为固定月薪。
销售经理：工资计算方法为销售额销售额提成比例+固定月薪。
请根据以上要求设计合理的类，完成以下功能：

添加所有类型的人员
计算月薪
显示所有人工资情况
"""
class Person:
    def __init__(self,no,name,salary):
        self.no=no
        self.name=name
        self.salary=salary

class worker:
    def __init__(self,hour,per_money):
        self.hour=hour
        self.per_money=per_money

    def get_salary(self):
        result=self.hour*self.per_money
        return result

class seller:
    def __init__(self, total, properation):
        self.total_sell = total
        self.properation = properation

    def get_salary(self):
        result = self.total_sell * self.properation
        return result
class manager:
    def __init__(self,money):
        self.money=money
    def get_salary(self):
        result = self.money
        return result

class seller_manager:
    def __init__(self, total, properation,money):
        self.total_sell = total
        self.properation = properation
        self.money=money

    def get_salary(self):
        result = self.total_sell * self.properation+self.money
        return result
w=worker(200,20)
s=seller(20000,0.3)
m=manager(5000)
sm = seller_manager(10000,0.2,4000)
print(w.get_salary())
print(s.get_salary())
print(m.get_salary())
print(sm.get_salary())