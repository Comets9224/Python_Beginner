"""
字典  {}
元素是键值对的方式存在的
键:值    键是唯一的
dict={'张文伟':18267443446,'陈欣123456789'}
Python 字典是无序的数据结构，所以它们不支持下标或切片操作，这与列表
和元组等有序的数据结构不同。字典的元素是通过唯一的键来
访问的，而不是通过它们在字典中的位置。
"""
import time

dict={'张文伟':'18267443446','CX':'123654','lp':'54678894'}
print(dict['张文伟'])  #类似是下标  键就是下标 查起来方便

# 添加元素 字典名[key]=value
# 注意 key是唯一的  添加时出现同名的，值会覆盖

dict1={}
print(dict1)
name=input('输入姓名:')
number=input("请输入电话号码:")
dict1[name]=number
print(dict1)

# 修改元素  只要键 进去了  就没法修改了，只能是值改变
# 键可以添加或者删除  值可以修改

# dict1[name]='123456'   #所以这种方式既可以添加，也可以修改  没有的时候  添加，有了则作修改
# print(dict1)

# 字典删除  1.删除键值对(元素)  2.删除整个字典
# .pop('key')  删除 ，根据键对进行删除，有返回值，返回值是对应的value
# popitem()   删除，返回值是元组,默认从后往前删除   返回值是删除的(k,v)   不需要任何传参  删除字典里的从后往前的键值对
# clear()是清空 ，没有remove

# .get(key)  操作，通过键能够返回 key对应的value   get和[]对比 当get的键不存在，返回None  而book['书名']  会报错
# 获取推荐用get值  而且get('key','default')  如果前面key不存在，返回后面的参数，默认是None  可以自己更改

# 遍历列表和遍历字典不同   直接for in遍历出的不是键值对，而是key
# 获取所有值用.value()
# 和get有什么区别呢？    values获取的是 字典中的所有值  并把所有的值放到一个列表里了
#以遍历方式，可以遍历列表的所有值   values出来的是列表结构
#for v in book.values
#对应的有values 也有keys   .keys()  获取所有的键 放到列表里
#拿一个键值对就用items()   items的返回值是一个带有键值对的元组

# for k,v in book.items()
#     print(k,v)     快捷的方式赋值   遍历的时候既想拿到key 又想拿到value 就更灵活了
#其他
#setdefault('key','value')   类似增加键值对 book['key']='value '   只能添加，不能修改
#添加完了就不能修改了

#.update(dict2)  将  括号内的加到原字典上  字典不支持使用加号拼贴
#.fromkeys()   创建一个新的字典，用你给定的键  ，如果要赋值 dict.fromkeys(['a','b'],10)  括号内放的要可迭代的对象，列表可迭代
#fromkeys只能传一个参数  默认赋值给所有你给的键，此处dict可以是固定的 而不是你的字典名
"""
练习

book2={}
book3={}
booklib=[book1,book2,book3]
书名，价格，作者，出版社
促销，价格八折
打印最终字典内的内容

"""


print("~~~~~~~~~~~~~~~~欢迎进入图书管理系统~~~~~~~~~~~~~~~~~~~~~~~~~~")
book1={'书名':'水浒','价格':54,'作者':'施耐庵','出版社':'人民教育出版社'}
book2={'书名':'三国','价格':68,'作者':'罗贯中','出版社':'科学教育出版社'}
book3={'书名':'红楼','价格':108,'作者':'曹雪芹','出版社':'中央教育出版社'}
booklib=[book1,book2,book3]
#字典更重要的是添加字段  {}  增加新的键值对

while True:
    f=input("请输入你想要进行的操作:(1查询指定书籍信息 2添加书籍  3更改书籍信息  4删除书籍信息 5显示书库中所有书籍信息 6退出管理系统)")
    if  f=='1':
        book_search_flag=False
        book_search_name=input("请输入你需要查询的书籍名称:")
        for book in booklib:
            if book.get('书名')==book_search_name:  #get方式也可以  get('书名')
                book_search_flag=True
                print('{}  价格为{}   作者是{}   出版社为{}'.format(book['书名'],book['价格'],book['作者'],book['出版社']))
                break
        if not book_search_flag:
             print("查无此书，请重新输入！")
    elif f=='2':
        book_add_name=input('请输入需要添加到书籍库的书籍名称:')
        book_add_price=input('价格是?:')
        book_add_author=input('作者是?')
        book_add_press=input('出版社是?')
        booklib.append({'书名':book_add_name,'价格':book_add_price,'作者':book_add_author,'出版社':book_add_press})
        print('添加成功,请继续其他操作!')
        print(booklib)
    elif f=='3':
        book_change_flag=False
        book_change_name=input('请属于要更改书籍信息的书名:')
        book_change_key=input('需要更改的信息字段名是？:')
        book_change_info=input('改为什么？:')
        for book in booklib:
            if book.get('书名')==book_change_name:
                book_change_flag=True
                book[book_change_key]=book_change_info
                print(book)
                break
        if not book_change_flag:
            print('查无此书，请重新输入！')

    elif f=='4':
        book_del_name=input('请输入要删除的书籍名称:')
        book_del_flag=False
        count=0
        for book in booklib:
            count+=1
            if book['书名']==book_del_name:
                book_del_flag=True
                del booklib[count-1]
                print(booklib)
                break
        if not book_del_flag:
            print('查无此书，请重新输入！')
    elif f=='5':
        pass
    elif f=='6':
        print('正在退出系统，请稍后...')
        time.sleep(1)
        print('成功退出系统:')
        break
    else:
        print("输入错误请重新输入！")


#字典能转列表吗？
dict2={'a':'b','c':'d'}

#字典由于键值对的原因，其他三种不能转   字典转列表 元组 集合 只会把键拿出放到元组里
#列表转字典  特殊要求 list=[('a',10),('b',20)]  这种情况能够列表转字典
#里面不限元组还是列表   但是要有这个结构
