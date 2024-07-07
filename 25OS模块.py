#模块:  xxx.py    比如os.py， buildin.py

#OS是操作系统会使用的模块
import os
"""
os常用的

"""
print(os.path.dirname(__file__))  #--------->路径以字符串方式打印出来    这个函数特别有用，可以避免手动拼接路径时可能出现的错误。__file__表示当前文件的意思
#open 只能到文件不能到文件夹  配合join使用  os.path.join(path,'a1.jpg')   在原来文件夹下 接了一个文件名

#stream.name   就是找到名了   然后用切片 切到\  就是文件名了，经常是看不见文件名的，就要从路径上 对文件名进行操作
"""
总结
stream.name 用于获取文件对象的文件名或路径。
os.path.join(path, 'a1.jpg') 用于将路径和文件名连接成一个完整的路径。
print(os.path.dirname(__file__)) 用于获取当前脚本文件所在的目录路径。
每个表达式在不同的场景中都有其特定的用途和作用。希望这些解释能帮助你理解它们之间的区别和使用方法。

#获取当前工作目录
os.getcwd()
返回当前工作目录的路径。

#改变当前工作目录
os.chdir(path)
改变当前工作目录到指定的路径 path。

#列出目录内容
os.listdir(path='.')
返回指定目录 path 中的文件和目录列表。如果未指定 path，则使用当前工作目录。

#创建目录
os.mkdir(path)
创建一个目录，路径为 path。

#递归创建目录
os.makedirs(path)
递归创建目录。可以创建多级目录。

#删除文件
os.remove(path)
删除指定路径 path 的文件。

#删除目录
os.rmdir(path)
删除指定路径 path 的目录。目录必须为空。

#递归删除目录
os.removedirs(path)
递归删除目录。删除多级目录，必须从最深的目录开始。

#重命名文件或目录
os.rename(src, dst)
将文件或目录从 src 重命名为 dst。

#获取文件或目录的状态
os.stat(path)
返回包含文件或目录状态的 os.stat_result 对象。

#分割路径
os.path.split(path)
将路径 path 分割成目录和文件名，返回一个元组 (head, tail)。

#分割扩展名
os.path.splitext(path)
将路径 path 分割成文件名和扩展名，返回一个元组 (root, ext)

#判断路径是否存在
os.path.exists(path)
判断路径 path 是否存在。

#判断是否为目录
os.path.isdir(path)
判断路径 path 是否为目录。

#判断是否为文件
os.path.isfile(path)
判断路径 path 是否为文件。

#判断是否为绝对路径
os.path.isabs(path)
判断路径 path 是否为绝对路径。

#判断路径是否是符号链接
os.path.islink(path)
判断路径 path 是否是符号链接。
"""