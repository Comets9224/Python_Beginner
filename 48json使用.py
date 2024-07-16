# json用法
import json

# json类似 python中的字典
"""
1.python--->转json
#将 Python 对象转换为 JSON 字符串
json.dumps()方法,dumps(变量,skipkeys=False, ensure_ascii=False,indent=4)
json.dump()方法  dump(变量,文件,skipkeys=False, ensure_ascii=False,indent=4)
2.json---->转python
json.loads() 将json文件类型转成python类型   注意有无s
"""
data = [{'书名': '水浒', '作者': '施耐庵', 'ISBN': '95535', '出版社信息': '人民教育出版'}]
json_string = json.dumps(data, skipkeys=False, ensure_ascii=False, indent=4)
print(json_string)
python_string = json.loads(json_string)
print(python_string)
# TODO:哪些能放进去?
"""
哪些数据能传?
字典（dict）：转换为 JSON 对象。
列表（list）和元组（tuple）：转换为 JSON 数组。
字符串（str）：转换为 JSON 字符串。
整数（int）和浮点数（float）：转换为 JSON 数值。
布尔值（bool）：转换为 JSON 布尔值。
None：转换为 JSON 的 null。

键必须是字符串：在 JSON 对象中，键必须是字符串，而在 Python 字典中，键可以是任何不可变类型。
类型限制：JSON 不支持 Python 的一些特有类型，如集合（set）、复数（complex）等。如果需要序列化这些类型，需要自定义序列化方法。
数值类型：JSON 只支持有限的数值类型（整数和浮点数），不支持 Python 的 Decimal 或 Fraction 类型。
"""
# TODO:除了w还有哪些?  indent为什么是4
# indent 是缩进,纯粹为了好看
# TODO:保证中文编码

"""
3.写入json文件:(中文还要另外注意写进去的编码)
with open('data.json', 'w') as file:   w应该是write   
    json.dump(data, file, indent=4)
    
4.读取json文件
with open('data.json', 'r') as file:
    data = json.load(file)
"""
# 写入文件
with open('48test_json.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, skipkeys=False, ensure_ascii=False)  # 中文编码
    """
        skipkeys：如果为 True，则会跳过不能作为键的对象（如非字符串、非数字的键）；默认为 False。
        ensure_ascii：如果为 True（默认），所有非 ASCII 字符都会被转义；如果为 False，则会输出原始字符。
      为确保能正确读写 w后再加一项encoding='utf-8'
      with open('data.json', 'w', encoding='utf-8') as file:
      json.dump(data, file, ensure_ascii=False, indent=4)
      
      但是
      处理 JSON 文件时，json.load 和 json.dump 函数的默认行为是处理 
      Unicode 字符，而不是特定的编码（如 UTF-8）。因此，即使没有显式
      地指定编码，Python 也可以正确处理包含中文字符的 JSON 数据。
      这是因为 JSON 本身是基于 Unicode 的格式。
      不加encoding也没关系
    """
# 读取文件
with open('48test_json.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    data.append({'key': 'valuetest'})
print(data)

# TODO:以下不用写了
"""
5.更新json文件
# 读取 JSON 文件
with open('data.json', 'r') as file:
    data = json.load(file)
# 更新数据
data['age'] = 31
data['address']['city'] = 'San Francisco'
# 写回 JSON 文件
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)
6.删除 JSON 数据中的键
# 读取 JSON 文件
with open('data.json', 'r') as file:
    data = json.load(file)
# 删除键
del data['is_student']
# 写回 JSON 文件
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)
"""
# TODO:a,w,r,+区别
"""
+（更新模式）：在读写模式后加上 +，表示可以同时进行读和写操作。例如：
r+：打开文件用于读写。文件必须存在。
w+：打开文件用于读写。如果文件不存在，会创建新文件；如果文件存在，会覆盖原有内容。
a+：打开文件用于读写。如果文件不存在，会创建新文件；如果文件存在，写入的数据会追加到文件末尾。
"""

# 如果放一个列表,再追加一个列表,json中是怎么放的?,再写入读取试试---->会出错,列表格式会被损坏

"""
with open('48test_json.json','a',encoding='utf-8') as file:
    json.dump(data,file,skipkeys=False, ensure_ascii=False)#中文编码
#读取文件
with open('48test_json.json','r',encoding='utf-8')as file:
    data=json.load(file)
    #data.append({'key':'valuetest'})
print(data)
"""

# 新的数据
new_data = [
    {
        "书名": "西游记",
        "作者": "吴承恩",
        "ISBN": "12345",
        "出版社信息": "人民教育出版"
    }
]
"""需要先取出处理,再重写回文件
# 读取现有的 JSON 文件内容
with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 确保 data 是一个列表，然后追加新数据
if isinstance(data, list):
    data.extend(new_data)
else:
    raise ValueError("JSON 文件内容不是一个列表")

# 将更新后的数据写回 JSON 文件
with open('data.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("数据追加成功")
"""

# append 和 extend 的区别
# append 方法将参数作为单个元素添加到列表末尾。
# extend 方法将参数中的所有元素逐个添加到列表末尾。

# json数据不能单独{},{}存在,必须是一整个数组[{},{},{}]
"""
在 JSON 文件中，单独的 {} 对象不能直接追加到文件中。
JSON 格式要求数据结构必须是有效的 JSON 数据类型，
如对象（{}）、数组（[]）、字符串、数值、布尔值或 null。
如果你想在 JSON 文件中存储多个对象，必须将它们包含在一个数组中。
"""
