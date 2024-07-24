#random模块
import random
ran=random.random()#回复0-1之间的随机小数
print(ran)
ran=random.randrange(0,101,3) #范围内选一给整数  可选步长
print(ran)
# while True:
ran=random.randrange(0,1)  #不包含1
print(ran)
list1=['z','y','x']
ran=random.choice(list1)
print(ran)   #返回列表的元素
random.shuffle(list1)  #打乱顺序  洗牌  没有返回值，将原来的列表乱序
print(list1)  #返回的是乱序的列表元素
def verify_code():
    code=''
    for i in range(4):
        ran1=str(random.randint(0,9))   #randomint 是包左包右的
        ran2=chr(random.randint(65,90))
        ran3=chr(random.randint(97,122))
        r=random.choice([ran1,ran2,ran3])
        code += r
    print(code)
verify_code()
