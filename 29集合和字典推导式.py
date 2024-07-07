list1=[1,2,1,3,5,2,1]
set2=set(list1)
print(set2)
set1={x for x in list1}
print(set1)
set3={x+1 for x in list1}
print(set3)  #在列表推导式的基础是增加了去重的功能


#字典推导式
dict1={'a':'A','b':'B','c':'C','c':'D'}
#希望进行键值颠倒 用字典推导式
newdict ={value:key for key,value  in dict1.items()}
print(newdict)