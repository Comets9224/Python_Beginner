import random
import time
booklib=[{'bookname':'xiyou','number':2},{'bookname':'honglou','number':3},{'bookname':'shuihu','number':1},{'bookname':'sanguo','number':5}]
user=[{'username':'admin','password':'1234','phone':'18267443446'},{'username':'lp','password':'5678','phone':'18612345678'}]
def generata_code():
    code=''
    s='zxcvbnmasdfghjklqwertyuiopZXCVBNMASDFGHJKLQWERTYUIOP123456789'
    for i in range(1,5):
        code+=s[random.randint(0,len(s)-1)]
    return code
def check_book_have(book):
    check_flag=False
    postion=0
    while not check_flag:
        for i in booklib:
            postion+=1
            if i.get('bookname')==book and i.get('number')>0:
                check_flag=True
                return True,postion-1
                break
        if not check_flag:
            return False,postion-1

def user_is_login():
    while True:
        user_name=input('please input your user name:')
        for i in user:
            if i.get('username')==user_name:
                user_password=input('please input your password:')
                if i.get('password')==user_password:
                    code=generata_code()
                    print(code)
                    user_code=input('please accord above code input the verify code:')
                    if user_code==code:
                        return True
                    else:
                        print('verif code error please renew input!')
                        break
                else:
                    print('password error please renew input!')
                    break
        else:
            print('no user,please renew input!')
def print_book_info(postion):
    print('book:{}'.format(booklib[postion].get('bookname')))
    print('number is :{} in the lib'.format(booklib[postion].get('number')))

print('welcome into book manage system')
# if user_is_login()==True:
#     login_flag=True
#     print('login successful,into system,please wait...')
#     time.sleep(1)
#
# while login_flag:
while True:
    book_operation=input('please input operation what you want:(1.check 2.borrow 3.return)')
    if book_operation=='1':
        book_check_name=input('please input book what you want:')
        ishave,pos=check_book_have(book_check_name)
        if ishave:
           print_book_info(pos)
        else:
            print('this book not exist!')
    elif book_operation=='2':
        book_borrow_name=input('please input book what you want:')
        ishave,pos=check_book_have(book_borrow_name)
        if ishave:
            booklib[pos]['number']-=1
            print('borrow is successful!')
            print_book_info(pos)
        else:
            print('borrow is failed!')
            print('this book not exist!')
    elif book_operation=='3':
        book_return_name = input('please input book what you want:')
    else:
        print("please renew input!")

