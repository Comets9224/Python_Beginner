#文件的 复制
"""
源文件和目标文件  不是复制文本 是复制文件
比如复制两个图片  以rb打开
"""
origin_path=r'D:\Project\PycharmProject\Python_Beginner\24origin.txt'
target_path=r'D:\Project\PycharmProject\Python_Beginner\24target.txt'
origin=open(origin_path,encoding='utf-8')
target=open(target_path,'w')
while True:
    temp=origin.readlines()    # readlines 方法一次性读取整个文件，
                               # 并将每一行作为一个元素存储在列表中。
    target.writelines(temp)   #------>返回值是NONE
    if temp:
        break

target.close()
origin.close()

pic=open(r'24copy_test.jpg','rb')
pic_copy=open(r'24copy_target.jpg','wb')
while True:
    temp=pic.read()    #图片文件一般以二进制  不用readlines对于文本文件，返回一个字符串；对于二进制文件，返回一个字节对象
    pic_copy.write(temp)  #------>返回值是NONE
    if temp:
        break
"""
其实可以不用加while循环  
origin = open(origin_path, encoding='utf-8')
target = open(target_path, 'w')

temp = origin.readlines()  # 一次性读取整个文件内容
target.writelines(temp)    # 一次性写入整个文件内容

origin.close()
target.close()

"""

"""
为了对文件处理更加高效，有一个with结构  
with open() as pic   #使用with 可以自动帮我们释放资源
"""
with open(r'24copy_test.jpg','rb') as pic:
    temp= temp=pic.read()
    with open(r'24copy_target2.jpg','wb') as pic_copy:
        pic_copy.write(temp)

"""
open  必须是文件，而不是文件夹
需要打开或者复制文件夹，就要用OS模块

"""

