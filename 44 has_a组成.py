#(继承) is a 和 (组成)has a的区别是?
#继承是类继承类   组成是类包含类

class Computer:
    def __init__(self,brand,type,color):
        self.brand=brand
        self.type=type
        self.color=color
    def online(self):
        print('正在使用电脑上网...')
    def __str__(self):
        return self.brand+'---'+self.type+'---'+self.color

class Book:
    def __init__(self,bname,author,number):
        self.bname=bname
        self.author=author
        self.number=number
    def __str__(self):
        return self.bname+'---'+self.author+'---'+str(self.number)

class Student:#has a
    def __init__(self,name,computer,book):
        self.name=name
        self.computer=computer
        self.books=[]
        self.books.append(book)

    def borrow_book(self,book):
        for book1 in self.books:
            if book1.bname== book.bname:
                print('已经借过这本书')
                break
        else:
            #将参数book添加到列表中
            self.books.append(book)
            print('添加到列表成功!')
    def show_book(self):
        for book in self.books:  # book就是一个book对象
            print(book.bname)
    # for i in books:#如何把books 另一个函数里的局部变量拿来用? 上面的列表books里书拿来用?
        # print('成功借了{}'.format(book))
    def __str__(self):
        return self.name+'----'+str(self.computer)+'-----'+str(self.books)#所以,传整形可以转str类型,computer类型的
                              #self.computer 不是字符串,强转  报错的原因是,整形能str类型转,books是列表类型,computer是Computer类型
                              #str转self.computer的过程,相当于print了computer ,就调用到了Computer里的__str__,打印出来computer的信息

#创建对象
computer=Computer('lenovo','y7000p','深灰色')
book=Book('盗墓笔记','南派三叔',10)
stu=Student('songsong',computer,book)#传的computer和传songsong一样,传的是一自定义的computer类型
print(stu)
book1=Book('鬼吹灯','天下霸唱',9)
stu.show_book()
stu.borrow_book(book1)
print('---------------')
stu.show_book()
"""
类型:有int str等自带的类型和自定义类型类,例如Computer类,Book类 
我们能够看到 stu 包含了computer，包含了book
在学生类里包含了computer和book,使用了另外一种自定义的类型,我们称为has a
也就是 Student has a Computer 和Book
算是自定义的类，都可以将其当成一种类型，s=Student(),s是student类型的对象

"""