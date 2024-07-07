booklib = [{'书名': '水浒', '作者': '施耐庵', 'ISBN': '95535', '出版社信息': '人民教育出版', '库存': 2},
           {'书名': '三国', '作者': '罗中汉', 'ISBN': '95536', '出版社信息': '人民教育出版', '库存': 3},
           {'书名': '红楼', '作者': '施耐庵', 'ISBN': '95537', '出版社信息': '人民教育出版', '库存': 10}]
user = [{'username': 'zhang', 'phonenumber': '13586315791', 'password': '1234'},
        {'username': 'cx', 'phonenumber': '13586315792', 'password': '1234'},
        {'username': 'lp', 'phonenumber': '13586315793', 'password': '1234'}]
admin = [{'username': 'admin', 'phonenumber': '18267443446', 'password': '1234'}]
zhang = [{'书名': '水浒', '作者': '施耐庵', 'ISBN': '95535', '出版社信息': '人民教育出版'}]
user_record = ['zhang', 'cx', 'lp']
book_record = [[], [], [], [], []]  # 每有一个人，就新建一个空列表
# TODO：使用 enumerate 方便地获取用户的索引。
# 用户注册与登录
def register_user(user_name, password):
    while True:
        if len(user_name) == 11:
            phone_flag = True
        else:
            phone_flag = False
        temp = {}
        if phone_flag:
            name = input('请输入用户名:')
            temp['name'] = name
            temp['phonenumber'] = user_name
            temp['password'] = password
        else:
            phone = input('请输入手机号:')
            if len(phone) != 11:
                print('手机号长度错误,请检查')
                continue
            temp['name'] = user_name
            temp['phonenumber'] = phone
            temp['password'] = password
        user.append(temp)
        print(user)
        print('恭喜您注册成功！请继续登录')
        break

register_user()
def login_user():
    while True:
        flag = False
        user_name = input('请输入用户名/手机号:')
        password = input('请输入密码:')
        for i in admin:  # user_name 是要传的value     先去管理员账户里找,是不是管理员
            if i.get('username') == user_name or i.get('phonenumber') == user_name:
                flag = True
                if i.get('password') == password:
                    print('登录成功,欢迎管理员进入系统')
                    return '管理员登录'  # 返回登录成功
                else:
                    print('管理员密码输入错误，请重新输入!')
                    break

        for i in user:  # user_name 是value
            if i.get('username') == user_name or i.get('phonenumber') == user_name:
                flag = True
                if i.get('password') == password:
                    print('登录成功,欢迎您进入系统')
                    return '普通用户登录'  # 返回登录成功
                else:
                    print('密码输入错误，请重新输入!')
                    break
        if flag == False:
            reg_flag = input('没有此用户,你可选择注册或重新输入，是否注册？(y/n)')  # 是否注册?
            if reg_flag == 'y' or reg_flag == 'Y':
                register_user(user_name, password)


# 图书管理
def add_bookDir(booklib):  # 虽然传参和直接调用全局变量是一样的  但是  传参更有利于代码的可读性
    while True:
        tempdict = {}
        key_list = ['书名', '作者', 'ISBN', '出版社信息', '库存']
        ISBN_flag = False
        for lists in key_list:
            temp = input(f'请输入需要添加书籍的{lists}:')
            if lists == 'ISBN':
                for book in booklib:
                    if book.get('ISBN') == temp:
                        print('此书可能是盗版')
                        ISBN_flag = True  # True表示确实是盗版
                        break
                if ISBN_flag:
                    print('该书添加失败')
                    break
            tempdict[lists] = temp
        if not ISBN_flag:
            booklib.append(tempdict)
            print('添加成功！')
        ifcontinueadd = input('是否继续添加？(y/n):')
        if ifcontinueadd == 'y' or ifcontinueadd == 'Y':
            pass
        else:
            print('成功退出添加操作')
            # 调试用
            print(booklib)
            break


def view_bookDir(booklib):
    print('当前书库内在册书籍:')
    print('书名:'.center(11), 'ISBN:'.rjust(1), '库存:'.rjust(5))
    for book in booklib:
        name = book.get('书名')
        ISBN = book.get('ISBN')
        store = str(book.get('库存'))
        print(name.center(10), ISBN.rjust(5), store.rjust(5))


def search_booksDir(booklib, bookname):
    while True:
        flag = 0
        for i in booklib:
            if i.get('书名') == bookname or i.get('作者') == bookname:
                flag += 1
                print("找到第{}本书书名为:{},作者为{}".format(flag, i.get('书名'), i.get('作者')))
                return True  # 只会return True  否则判断为False
        if flag == 0:
            print('没找到这本书,请重新试试')
            return False
        # 返回False 表示没有找到  返回ture 表示找到了


def del_bookDir(booklib):  # 对输入进行检测,书名可能会多一个空格导致书名字不对
    view_bookDir(booklib)
    while True:
        flag = False
        name = input('请输入要删除的书籍(书名/ISBN),如果有同名书籍请根据ISBN进行删除:')
        i = -1
        for book in booklib:
            i += 1
            if book.get('书名') == name or book.get('ISBN') == name:
                flag = True
                booklib.pop(i)
        if flag == True:
            view_bookDir(booklib)
            con = input('是否继续删除?(y/n):')
            if con == 'N' or con == 'n':
                print('成功退出删除操作')
                break
        if flag == False:
            print('不存在此书，请重新试试')


# 借还管理
def account_pos(account, user_record):
    user_pos = -1
    for user in user_record:
        user_pos += 1
        if account == user:
            return user_pos


def borrow_book(booklib, account):
    while True:
        view_bookDir(booklib)
        bookname = input('你想借阅什么书？(重名的书用ISBN输入):')
        result = search_booksDir(booklib, bookname)  # 如果找到了  返回是True   #输入isbn会报错
        user_pos = account_pos(account, user_record)
        if result:
            booklib_pos = -1
            for books in booklib:
                booklib_pos += 1
                if bookname == books.get('书名') or bookname == books.get('ISBN'):
                    if books['库存'] > 0:
                        books['库存'] -= 1
                        print('成功借出一本{}'.format(bookname))
                        temp = booklib[booklib_pos].copy()
                        temp.pop('库存')  # pop会返回删除的值   同样的 删除了不需要去接，买了个电视，全家都能看到在这个地址
                        temp['数量'] = 1  # 初始化赋值
                        book_found = False
                        for book in book_record[user_pos]:  # 遍历用户借书记录
                            if book.get('书名') == temp.get('书名'):
                                book['数量'] += 1
                                book_found = True
                                break
                        if not book_found:  # 用标志的方法 搞定了数量新建书目不对的问题
                            book_record[user_pos].append(temp)
                        print(book_record)
                    else:
                        print('库存为0,无法借阅')
                        view_bookDir(booklib)
                        # print(book_record)
        exit_flag = input('是否退出借阅？(y/n):')
        if exit_flag == 'y' or exit_flag == 'Y':
            break


def account_manager(account, mode, user_record, booklib):
    if mode == '1':  # 账户查询已经借了哪些书
        view_borrowed_books(account, user_record, book_record)
    elif mode == '2':  # 账户还书
        borrow_book(booklib, account)
    elif mode == '3':  # 账户借书
        return_book(account, user_record, booklib)


def return_book(account, user_record, booklib):
    view_borrowed_books(account, user_record)
    while True:
        bookname = input('请输入你要还的书(书名/ISBN):')
        user_pos = account_pos(account, user_record)
        for book in book_record[user_pos]:
            if bookname == book.get('书名') or bookname == book.get('ISBN'):
                if book.get('数量') > 0:
                    book['数量'] -= 1
                    if book.get('数量') == 0:
                        book_record[user_pos].remove(book)
                    for books in booklib:
                        if bookname == books.get('书名') or bookname == book.get('ISBN'):
                            books['库存'] += 1
                            print('归还成功！')
                            view_borrowed_books(account, user_record, book_record)
                            view_bookDir(booklib)
                            break
                    break

                else:
                    print('账户内待还的书数量不足，请重新输入')
            else:
                print('输入书名错误，请重新输入')
        exit = input('是否退出还书？(y/n):')
        if exit == 'y' or exit == 'Y':
            break


def view_borrowed_books(account, user_record, book_record):
    user_pos = account_pos(account, user_record)
    if book_record[user_pos] == []:
        print('当前账户没有未归还的书籍！')
    else:
        print('当前账户内未归还书籍如下:')
        print('书名:'.center(11), 'ISBN:'.rjust(1), '库存:'.rjust(5))
        for book in book_record[user_pos]:
            name = book.get('书名')
            ISBN = book.get('ISBN')
            store = str(book.get('数量'))
            print(name.center(10), ISBN.rjust(5), store.rjust(5))


def lib_manager(booklib):
    print('欢迎管理员进入图书管理系统')
    while True:

        work = input("""
        请输入需要进行的操作:
        1.浏览书库
        2.搜索书籍条目
        3.增加书籍条目
        4.删除书籍条目
        请输入:
        """)
        if work == '1':
            view_bookDir(booklib)
        elif work == '2':
            while True:
                name = input('请输入想搜索的书名/ISBN:')
                result = search_booksDir(booklib, name)
                if result == True:
                    con = input('你要找的书存在,是否继续查找?(y/n)')
                    if con == 'N' or con == 'n':
                        break
                else:
                    con = input('你要找的书不存在,是否继续查找?(y/n)')
                    if con == 'N' or con == 'n':
                        print('成功退出搜索操作')
                        break
        elif work == '3':
            add_bookDir(booklib)
        elif work == '4':
            del_bookDir(booklib)
        else:
            print('输入错误请重新输入')
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
    # add_bookDir(booklib)
    # view_bookDir(booklib)
    # del_bookDir(booklib)
    # borrow_book(booklib,user_record,'lp')
    # print(login_user())
    # opration=input('')
    lib_manager(booklib)
    # delete_book(booklib)
    # borrow_book(booklib)
    # account = input('请输入借书人:')
    # while True:
    #     mode = input('请输入操作1查看2借书3还书:')
    #     account_manager(account, mode, user_record, booklib)

    # while True:
    #     # 主菜单
    #     pass
    #
    # save_data('users.json', users)
    # save_data('books.json', books)
    # save_data('borrows.json', borrows)


if __name__ == '__main__':
    main()
"""
数据存储：
所有用户信息和图书信息需要持久化存储到文件中。
每次启动程序时，从文件中读取数据。
数据存储：
使用文件操作将用户信息和图书信息保存到文件中。
使用异常处理处理文件操作中的可能错误。
提示：
退出系统用装饰器写
使用 json 模块进行文件读写操作。
使用异常处理 (try/except) 处理文件操作中的错误。
"""
