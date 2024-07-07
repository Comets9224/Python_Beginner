#追加 a
path=r"D:\Project\PycharmProject\Python_Beginner\file_operation.txt"
s="""你好，欢迎来到澳门博彩赌场

                ,送你一个金币"""
file=open(path,'w')
file.write(s)

#想换行要用readlines
file.writelines(["-----此处是换行\n",'赌侠\n','赌圣\n'])
file.write("僵尸\n")#readlines 是没有换行的，只是lines能加可迭代的 列表往里放
file.close()
#只要是  w mode  每次  （开关一次文件叫一次）都会将原来的清空 再写当前的内容

file=open(path,'a')
file.write("这是追加模式\n")
file.write("这是追加模式\n")
file.write("这是追加模式\n")
file.close()

#读写 是两个不同的管道   一般带lines的都是只有文本模式才涉及到行  写字节 直接是写write的


