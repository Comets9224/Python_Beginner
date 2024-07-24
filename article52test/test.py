def publish(obj):
    print('Publishing...{boj.name}')

from user52test.models import User
from article52test.models import Article
#from .models import User
user=User('admin','123456')
article=Article('zzz2','论星星之火可以燎原')
user.publish(article)

#如果  包内要调用包外的模块怎么办?  如何导入
list1=[1,2,3,4,5]
from cal import add
result=add(*list1)
print(result)