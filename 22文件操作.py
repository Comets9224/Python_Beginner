#文件操作：
"""
文件上传  保存log
系统函数：
open()   --------------->返回值是流
open(file,mode,buffreing,encoding)------------>mode'r'
输入输出 都是在pycahrm立场上
不存在会自己生成一个  +是更新的方式

with open('example.txt', 'r+', encoding='utf-8') as file:
    content = file.read()
    print(content)
    file.write('\nAdding new content.')


    追加 a  追加在文件后面
    写 写了会清楚原有内容
    写读和读写不一样  写读 会先清除文件内的内容
"""
path=r"D:\Project\PycharmProject\Python_Beginner\file_operation.txt"
stream=open(path,'w')  #------------>返回值是流 读取全部
# print(stream.read())

while True:
    line=stream.readline()   #readline 每次一读 会自动换行符  每次读都会在读出来的内容后加一个换行，打印出来一串空格
    print(line)     #r是模式，不等于操作   ，加循环一行一行读
#上述已经读取完了，再调用readline也读不到任何东西了
# ，已经读过了，就读不到任何东西了

    if not line:
        break
 #.readlines()   一次读取多行------------------>  读出来是一个列表['sasdada\n','gsajhghj\n0']
 #能读图片 但是读不出文字内容   默认是rt，文本文档  ，应该要rb  二进制方式读
 #如果是图片，则不能使用默认的读取方式  mode=‘rb’
"""  还得拿line接才行  还是有区别的
读取次数:

方法一: 每次循环中读取两次，导致文件指针移动两行，并且只打印奇数行。
方法二: 每次循环中读取一次，文件指针移动一行，打印所有行。
代码逻辑:

方法一: 因为读取两次，第二次读取的结果用于判断文件结尾，但这会导致每次打印时跳过一行。
方法二: 读取一次并存储在变量中，然后打印和判断文件结尾，逻辑更清晰且不会跳过行。


"""
"""
显式指定模式: open(path, 'r') 明确
地表示你要以读取模式打开文件。这种方式更清晰，推荐使用。
默认模式: open(path) 使用了默认
的读取模式 'r'。虽然效果相同，但显式指定模式会使代
码更具可读性和可维护性。
文件存在性:

不同模式对文件是否存在有不同的要求。例如
，'r' 模式要求文件必须存在，否则会抛
出 FileNotFoundError；而 'w' 模式会在文
件不存在时创建一个新文件。
文件指针位置:
不同模式会影响文件指针的初始位置。
例如，'r' 模式和 'w' 模式下文件指针都在文件开头，
而 'a' 模式下文件指针在文件末尾。
"""


