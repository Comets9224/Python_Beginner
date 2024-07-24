__all__=['Article']  #仅仅针对from 包.模块 import *
class Article:
    def __init__(self,author,title):
        self.author = author
        self.title = title
    def show(self):
        print(f'文章作者:{self.author}文章名字:{self.title}')
class Tag:
    def __init__(self,name):
        self.name = name
