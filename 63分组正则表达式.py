import re
#分组
#匹配数字0-100数字
n='09'
result=re.match('[1-9]?\d',n)   #1-9 可有可无,所以拿后面数字\d匹配,输入09匹配到0,就停止匹配了 返回就是0
print(result)
n='1000'
result=re.match(r'[1-9]+\d*',n)   #1-9 可有可无,所以拿后面数字\d匹配,输入09匹配到0,就停止匹配了 返回就是0
print(result)
#改进版
n='1000'
result=re.match(r'[1-9]?\d?|100$',n)   #1-9 可有可无,所以拿后面数字\d匹配,输入09匹配到0,就停止匹配了 返回就是0
print(result)      #| 竖杠 表示或者     而且要求从头匹配到尾  匹配到10 两位数 但是如果输入100还是匹配不到
#继续改
n='100'
result=re.match(r'[1-9]?\d?$|100$',n)
print(result)      #| 竖杠 表示或者     而且要求从头匹配到尾 现在100能匹配到了  主要是用了或者|  正则

#验证输入的邮箱 163  126 qq
email='738542485@qq.com'
result=re.match(r'\w{5,10}@(163|126|qq)\.com$',email)  #小括号,可以是整体的字母组成  区别于[abc]   [abc]是一个字母,而不是一个单词
print(result)                         #点有特殊意思,要用 \.   一定记得加$  整体去比较
print('------不是以4 7 结尾的手机号码(11位)-------')
#不是以4 7 结尾的手机号码(11位)
phone='12345678901'
result=re.match(r'1\d{9}[0-35-68-9]$',phone)
print(result)

#爬虫
phone='010-12345678'
result=re.match(r'(\d{3}|\d{4})-(\d{8})$',phone)
print(result)
#分别提取  分组提取
print(result.group(1))   #第一个括号是第一组,第二个括号是第二组
print(result.group(2))  #组跟组怎么区分?  一个括号就是一个组
print('-----------爬虫html-------------')
# 爬虫html
msg='<html>abc</html>'  #提取标签内的内容
msg1='<h1>hello</h1>'
result=re.match(r'<\w+>(\w+)</\w+>$',msg)   #. 点是任意字母
print(result)
print(result.group(1))  #把经过过滤掉  再提取出来
print('----------爬虫html----------')
result=re.match(r'<\w+>(\w+)</\w+>$',msg1)   #+ 号表示贪婪模式 有匹配的 还会继续往下找

print(result)
print(result.group(1))
print('---------匹配正好成对的html中间的值--引用第一组-----------')
#number
result=re.match(r'<(\w+)>(.+)</\1>$',msg1)#  里面的\1, 表示 跟第一组 匹配的内容一直,表示引用第一组
#返回是None  原因是  msg1里<h1>  <h2>  并不相同  ,改回h1,没问题
print(result)
print(result.group(1))
print(result.group(2))
#上文一共两个组  因为两个括号
print('------------------------------------------------')
msg='<html><h1>abc</html></h1>'   #注意  尖尖括号内有'/'   \1 是表示取第一组   引用的不能算组  所以只有三组
result=re.match(r'<(\w+)><(\w+)>(.+)</\1></\2>$',msg)
print(result)
print(result.group(1))
print(result.group(2))
print(result.group(3))
#print(result.group(4))只有三组

