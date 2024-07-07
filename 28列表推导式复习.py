#列表推导式、集合生成式
#旧的列表------>新的列表
#1.列表推导式 ：格式  [表达式 for 变量 in 旧列表]  或者[表达式 for 变量 in 旧列表 if 条件]
#这个表达式就是一个列表，找result去接即可
names=['tom','lily','abc','jack','steven','bob','ha']
result=[name for name in names if len(name)>3]
print(result)
result=[name.capitalize() for name in names if len(name)>3]   #得到的name 首字母大写
print(result)
#将1-100之间能被3整除的，组成一个新的列表
result=[num for num in range(1,101) if num%3==0 and num%5==0]
print(result)

#构成一个元组列表怎么构成
#0~5偶数 0~10奇数
#[(偶数,奇数),(),(),()]

#双层循环 newlist.append(())
#用列表推导式
result=[(x,y) for x in range(5) if x%2==0 for y in range(10) if y%2!=0]
print(result)

#要得到 list1=[[1,2,3],[4,5,6],[7,8,9],[1,3,5]]---->[3,6,9,5]
list1=[[1,2,3],[4,5,6],[7,8,9],[1,3,5]]
newlist=[i[-1] for i in list1]   #甚至不需要加循环加条件。 不加if条件也是能用的
print(newlist)
dict1={'name':'tom','salaryt':5000}
dict2={'name':'tom','salaryt':8000}
dict3={'name':'tom','salaryt':4500}
dict4={'name':'tom','salaryt':6000}
#if薪资大于5000 加200  if 工资低于5000加500
newlist=[employee['salary']+200 if employee['salary']>5000 else employee['salary']+500 for employee in list1]
print(newlist)   #没有改变原来的数据，只是放了一个新的列表里

#列表生成式  放一个新列表
