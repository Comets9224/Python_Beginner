#正则表达式
"""基础"""
"""
基础:
. 任意符号
[] 范围
|或
()一组
量词:
* >=0
+ >=1
? 0 ,1
{m} =m
{m,}
{m,n}

预定义:
\s  space
\S not space
\d digit
\D not digit
\w word  包含下划线
\W not word
\b
\B not 边界

方法：
findall
等

分组:
()---->group(1)  有匹配才返回,没匹配会异常
number  (\w+)(\d*)  ----> group(1) group(2)
引用:
(\w+)(\d*)  ----> \1   \2   表示引用前面的内容
name起名
(?P<name>\w+)   (?P=name)
python里量词默认是贪婪的，少数语言中默认是非贪婪的，总是尝试去匹配更多字符
非贪婪则相反，尝试匹配更少尽可能少的字符
在"*,?,+,{m,n}"后加上?,使贪婪变成非贪婪.
"""
import re
#默认是贪婪的,无限的去找符合条件的,而不是取到ok就不取了,现在要由贪婪的变成非贪婪
msg='abc123abc'
result=re.match(r'abc(\d+?)',msg)#加上问号变非贪婪  模式切换
print(result)   #因为没有量词的情况下，正则表达式只能匹配一个固定数量的字符。

#虽然在简单的例子中，固定数量的匹配和非贪婪匹配可能产生相同的结果，
# 但它们的应用场景和行为在更复杂的正则表达式中会有所不同。
# 理解这两者的区别有助于编写更准确和高效的正则表达式。

path='<img img_width="3840" img_height="2160" src="//p4.itc.cn/q_70/images03/20230910/c5bb927917f54d49895186753353dd81.jpeg">'


result=re.search(r'src="(.*)\.jpeg"',path)
print(result.group(1))
"""以下演示爬虫
image_path=result.group(1)
import requests
response = requests.get(image_path) 

whit open response.content('aa.jpg','wb') as wstream:
      wstream.write(response.content)     #获取图片,不是文本 文本用.text
"""
