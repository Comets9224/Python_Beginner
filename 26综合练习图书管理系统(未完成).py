import json

admin = None
book_record = None
booklib = None
user = None
user_record = None
# TODO:根据输入的用户名或手机号，返回手机号，手机号作为唯一id，避免同名
# TODO:没有修改密码等等的操作,管理员也没有注销普通用户账户等操作
"""用户注册与登录部分函数"""


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


def login_user():
    print('欢迎进入图书管理系统,请先登录:')
    while True:
        flag = False
        user_name = input('请输入用户名/手机号:')
        password = input('请输入密码:')
        for i in admin:  # user_name 是要传的value     先去管理员账户里找,是不是管理员
            if i.get('username') == user_name or i.get('phonenumber') == user_name:
                flag = True
                if i.get('password') == password:
                    print('登录成功,欢迎管理员进入系统')
                    return '管理员登录', user_name  # 返回登录成功
                else:
                    print('管理员密码输入错误，请重新输入!')
                    break
        for i in user:  # user_name 是value
            if i.get('username') == user_name or i.get('phonenumber') == user_name:
                flag = True
                if i.get('password') == password:
                    print('登录成功,欢迎您进入系统')
                    return '普通用户登录', user_name  # 返回登录成功
                else:
                    print('密码输入错误，请重新输入!')
                    break
        if flag == False:
            reg_flag = input('没有此用户,你可选择注册或重新输入，是否注册？(y/n)')  # 是否注册?
            if reg_flag == 'y' or reg_flag == 'Y':
                register_user(user_name, password)


"""一些小的组件函数"""


def exit_func(func):
    def wrapper(*address, **kwargs):
        while True:
            func(*address, **kwargs)  # 需要修饰的f
            work = input('是否需要退出当前操作？(y/n)')
            if work == 'y' or work == 'Y':
                break
            else:
                pass

    return wrapper


def account_pos(account, user_record):
    user_pos = -1
    for user in user_record:
        user_pos += 1
        if account == user:
            return user_pos


"""管理员操作部分"""


def lib_manager(booklib):
    print('欢迎管理员进入图书管理系统')
    while True:
        work = input("""
        请输入需要进行的操作:
        1.浏览书库
        2.搜索书籍条目
        3.增加书籍条目
        4.删除书籍条目
        5.注销管理员
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
                        print('成功退出搜索操作')
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
        elif work == '5':
            fini_save(admin, book_record, booklib, user, user_record)
            break
        else:
            print('输入错误请重新输入')


@exit_func  # 装饰器没括号
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


decorator_search = exit_func(search_booksDir)  # 单独的搜书功能


@exit_func  # 如果函数里本来就要循环的，给一个break出口
def del_bookDir(booklib):  # TODO:对输入进行检测,书名可能会多一个空格导致书名字不对
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
            break
        if flag == False:
            print('不存在此书，请重新试试')


"""普通用户登录操作部分"""


def account_manager(account, user_record, booklib, book_record, admin, user):
    while True:
        mode = input("""
欢迎登录
请输入你想进行的操作:
1.查询借了哪些书
2.账户还书
3.账户借书 
4.注销登录
(请输入数字1,2,3,4)
""")
        if mode == '1':  # 账户查询已经借了哪些书
            view_borrowed_books(account, user_record, book_record)
        elif mode == '2':  # 账户还书
            borrow_book(booklib, account)
        elif mode == '3':  # 账户借书
            return_book(account, user_record, booklib)
        elif mode == '4':
            fini_save(admin, book_record, booklib, user, user_record)
            break


@exit_func
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
        break


@exit_func
def return_book(account, user_record, booklib):
    view_borrowed_books(account, user_record, book_record)
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


# TODO:库存等等字段，输入要进行判断，判断是否是数字,是否只有字母,电话号码长度是否足够
"""数据存储部分函数"""


def load_data(file_path):
    with open(file_path, 'r') as file:
        date = json.load(file)
        return date


def save_data(file_path, date):
    with open(file_path, 'w') as file:
        json.dump(date, file, skipkeys=False, ensure_ascii=False, indent=4)  # 缩进四个空格


def initload():
    global admin, book_record, booklib, user, user_record
    admin = load_data('26admin.json')
    book_record = load_data('26book_record.json')
    booklib = load_data('26booklib.json')
    user = load_data('26user.json')
    user_record = load_data('26user_record.json')
    user_record_create()
    return admin, book_record, booklib, user, user_record


def fini_save(admi, book_recor, bookli, use, user_recor):
    save_data('26admin.json', admi)
    save_data('26book_record.json', book_recor)
    save_data('26booklib.json', bookli)
    save_data('26user.json', use)
    save_data('26user_record.json', user_recor)


def user_record_create():
    pos = -1
    for i in user_record:
        pos += 1
    while True:
        if len(book_record) < pos + 1:
            book_record.append([])
        else:
            break


"""主函数"""


def main():
    # 初始化读取json文件数据
    admin, book_record, booklib, user, user_record = initload()  # 初始化加载数据
    while True:
        temp, username = login_user()
        if temp == '管理员登录':
            lib_manager(booklib)
        elif temp == '普通用户登录':
            account_manager(username, user_record, booklib, book_record, admin, user)


# TODO:报错部分

if __name__ == '__main__':
    main()
