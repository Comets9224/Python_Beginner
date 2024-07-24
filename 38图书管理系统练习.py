class Book:
    def __init__(self, name, quantity):
        # 初始化书籍属性
        self.name = name
        self.quantity = int(quantity)

    def __str__(self):
        return f'书名:{self.name}-库存:{self.quantity}'

    def update_quantity(self, amount):
        self.quantity += amount


class User:
    def __init__(self, user_id, password):
        self.user_id = user_id
        self.name = password

    def __str__(self):
        return f'欢迎{self.user_id}登录！'


class Admin():
    def add_book(self):
        # 添加图书到图书馆
        name = input('输入书名:')
        quantity = input('输入库存:')
        b = Book(name, quantity)
        booklist.append({'bookname': b.name, 'quantity': b.quantity})

    def remove_book(self):
        while True:
            name = input('输入书名:')
            flag = False
            for bookname in booklist:
                if bookname.get('bookname') == name:
                    flag = True
                    booklist.remove(bookname)
                    break
            if flag == False:
                print('该书不在书库中，请重新输入一本书名:')

    def update_book(self):
        while True:
            name = input('输入书名:')
            flag = False
            for book in booklist:
                if book.get('bookname') == name:
                    flag = True
                    b = Book(name, book.get('quantity'))
                    num = int(input('请输入你要增减的数量:'))
                    b.update_quantity(num)
                    book['quantity'] = b.quantity
                    break
            if flag == False:
                print('该书不在书库中，请重新输入一本书名:')

    def register_user(self):
        id = input('请输入新建的id:')
        pswd = input('请输入密码：')
        userlist.append({'id': id, 'pswd': pswd})


def Admin_work():
    while True:
        a = Admin()
        oper = input('请输入你需要进行的操作(1添加书,2删除书,3更新书,4注册用户5退出登录):')
        if oper == '1':
            a.add_book()
        elif oper == '2':
            a.remove_book()
        elif oper == '3':
            a.update_book()
        elif oper == '4':
            a.register_user()
        elif oper == '5':
            print('退出管理员登录！')
            break
        else:
            print('请重新输入数字:')


def login():
    userin_flag = False
    id = input('请输入您的id：')
    pswd = input('请输入您的密码：')
    if id == '12315' and pswd == '12345':
        userin_flag = True
        print('欢迎管理员登录')
        return '管理员登录'
    elif userin_flag == False:
        for username in userlist:
            if username.get('user_id') == id and username.get('pswd') == pswd:
                userin_flag = True
                print('欢迎用户登录！')
                return '用户登录'


userlist = [{'user_id': '11234', 'pswd': '123456'}]
booklist = []

if __name__ == '__main__':
    print('欢迎进入图书馆管理系统')
    log = login()
    while True:
        if log == '管理员登录':
            Admin_work()
        else:  # (非管理员登录)
            break
