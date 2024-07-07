import json
import os
"""
借阅管理：
用户可以借阅图书。
用户可以归还图书。
用户可以查看自己借阅的图书列表。
数据存储：

所有用户信息和图书信息需要持久化存储到文件中。
每次启动程序时，从文件中读取数据。
具体要求：
用户注册与登录：
借了什么书也要添加进去 到个人信息里

借阅管理：

使用字典存储借阅信息，用户名为键，借阅的书籍列表为值。
借阅图书时，检查图书是否已被借出。
归还图书时，从用户的借阅列表中移除图书。
数据存储：

使用文件操作将用户信息和图书信息保存到文件中。
使用异常处理处理文件操作中的可能错误。

提示：
退出系统用装饰器写
图书管理：

使用循环和条件语句实现搜索功能。
借阅管理：

使用字典的 setdefault() 方法管理借阅信息。
使用列表的 append() 和 remove() 方法管理借阅和归还。
数据存储：

使用 json 模块进行文件读写操作。
使用异常处理 (try/except) 处理文件操作中的错误。
当前登录的账户是谁的 传进去 ，从账户记录账户里去
"""
booklib=[{'书名':'水浒','作者':'施耐庵','ISBN':'95535','出版社信息':'人民教育出版','库存':2},{'书名':'三国','作者':'罗中汉','ISBN':'95536','出版社信息':'人民教育出版','库存':3},{'书名':'红楼','作者':'施耐庵','ISBN':'95537','出版社信息':'人民教育出版','库存':10}]
user=[{'username':'zhang','phonenumber':'13586315791','password':'1234','总借阅':0},{'username':'cx','phonenumber':'13586315792','password':'1234','总借阅':0},{'username':'lp','phonenumber':'13586315793','password':'1234','总借阅':0}]
admin=[{'username':'admin','phonenumber':'18267443446','password':'1234','总借阅':0}]
user_record=['zhang']
book_record=[{'水浒':1,'三国':2}]

# 用户注册与登录
def register_user(name,password):
    temp={}
    phone=input('确保您输入的是用户名情况下，请输入你的电话:')
    temp['name']=name
    temp['phonenumber']=phone
    temp['password']=password
    user.append(temp)
    print('恭喜您注册成功！请继续登录')
def login_user():
    while True:
        login_choice=''
        flag=False
        user_name = input('请输入用户名/手机号:')
        password = input('请输入密码:')
        for i in admin:  # user_name 是value
            if i.get('username') == user_name or i.get('phonenumber') == user_name:
                login_choice='管理员登录'
                if i.get('password') == password:
                    print('登录成功,欢迎管理员进入系统')
                    flag=True
                    return '管理员登录'  # 返回登录成功
                else:
                    print('管理员密码输入错误，请重新输入!')
        if login_choice !='管理员登录':
            for i in user:   #user_name 是value
                if i.get('username')==user_name or i.get('phonenumber')==user_name:
                    if i.get('password')==password:
                        print('登录成功,欢迎您进入系统')
                        flag=True
                        return '普通用户登录'   #返回登录成功
                    else:
                        print('密码输入错误，请重新输入!')
        if flag==False:
            ifregister=input('没有此用户,你可选择注册或重新输入，是否注册？(y/n)')
            if ifregister=='y'or ifregister=='Y':
                register_user(user_name,password)
            else:
                pass

# 图书管理
def add_book(booklib):#虽然传参和直接调用全局变量是一样的  但是  传参更有利于代码的可读性
    tempdict={}
    key_list=['书名','作者','ISBN','出版社信息','库存']
    for lists in key_list:
        temp=input(f'请输入{lists}:')
        if lists == 'ISBN':
            ISBN_flag=False
            for book in booklib:
                if book.get('ISBN')==temp:
                    print('此书可能是盗版')
                    ISBN_flag=True
                    break
            if ISBN_flag:
                print('该书添加失败')
                break
        tempdict[lists]=temp
    if not ISBN_flag:
        booklib.append(tempdict)
        print('添加成功！')
    ifcontinueadd=input('是否继续添加？(y/n):')
    if ifcontinueadd=='y' or ifcontinueadd=='Y':
        add_book(booklib)            #实际情况会用循环代替递归防止溢出
    else:
        print('退出添加操作')
def view_books(booklib):
    print('当前系统登记的所有书籍如下:')
    print('书名:'.center(11),'ISBN:'.rjust(1),'库存:'.rjust(5))
    for book in booklib:
        name=book.get('书名')
        ISBN=book.get('ISBN')
        store=str(book.get('库存'))
        print(name.center(10),ISBN.rjust(5),store.rjust(5))
def search_books(booklib,book):
    while True:
        flag=0
        for i in booklib:
            if i.get('书名')==book or i.get('作者')==book:
                flag+=1
                print("找到第{}本书书名为:{},作者为{}".format(flag,i.get('书名'),i.get('作者')))
                return True
        if flag==0:
            print('没找到这本书,请重新试试')
            return False
def delete_book(booklib):
    view_books(booklib)
    while True:
        flag=0
        name=input('请输入要删除的书籍(书名/ISBN):')
        i=-1
        for book in booklib:
            i+=1
            if book.get('书名')==name or book.get('ISBN')==name:
                flag+=1
                booklib.pop(i)
                view_books(booklib)
                break
        if flag==0:
            print('不存在此书，请重新试试')

# 借阅管理
def borrow_book(booklib):
    while True:
        view_books(booklib)
        name=input('你想借阅什么书？:')
        result=search_books(booklib,name)
        if result:
            for books in booklib:
                if name==books.get('书名'):
                    if books['库存']>0:
                        books['库存']-=1
                        print('成功借出一本')
                        view_books(booklib)
                    else:
                        print('库存为0,无法借阅')
                        view_books(booklib)
"""
借书还书应该是一体的  这边借了 那边就少了
账户多了 书库少了

还要增加  退出函数
"""
def account_manager(account,mode,book,user,Borrow='',reback=''):
    if mode=='1':#账户查询
        pos=-1
        for i in user:
            pos+=1
            if i==account:
                print('当前借阅的书籍有以下:')
                print(book[pos])
    elif mode=='2':#账户还书
        pos=-1
        for i in user:
            pos+=1
            if i==account:
                if book[pos].get(Borrow)!=0:
                    book[pos][Borrow]-=1
                    print('成功还书1本{}'.format(Borrow))
                    print(book[pos])

    elif mode=='3':#账户借书
        pos = -1
        for i in user:
            pos += 1
            if i == account:
                if book[pos].get(reback) == 'Unknow':
                    book[pos][reback] = 1
                else:
                    book[pos][reback]+=1
                    print('成功借书1本{}'.format(reback))
                    print(book[pos])
    else:
        pass



def return_book(users, borrows, current_user):
    pass

def view_borrowed_books(borrows, current_user):
    pass

# 数据存储
def load_data(file_path):
    pass

def save_data(file_path, data):
    pass

def exit_func():
    pass
def main():
    # users = load_data('users.json')
    # books = load_data('books.json')
    # borrows = load_data('borrows.json')

    #print(login_user())
    #opration=input('')
    #add_book(booklib)
    #delete_book(booklib)
    #borrow_book(booklib)
    account=input('请输入借书人')
    mode=input('查询1')
    account_manager(account,mode,book_record,user_record,reback='水浒')
    # while True:
    #     # 主菜单
    #     pass
    #
    # save_data('users.json', users)
    # save_data('books.json', books)
    # save_data('borrows.json', borrows)

if __name__ == '__main__':
    main()
