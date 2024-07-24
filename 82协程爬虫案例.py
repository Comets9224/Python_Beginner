# import gevent
# from gevent import monkey
#
# monkey.patch_all()  #补丁要在后面两个包之前
# from geventhttpclient import HTTPClient   #直接用requests 不太兼容猴子补丁  要用geventhttpclient
# from geventhttpclient.url import URL
# def download(url):
#     url= URL(url)  # 将字符串转换为 URL 对象
#     client = HTTPClient.from_url(url)  # httpclient处理必须是URL类型 而不能是字符串类型
#     response = client.get(url.request_url)
#     content = response.read()
#     print(f'下载了{url}网站的数据, 长度: {len(content)}')
#
# if __name__ == '__main__':
#     urls = ['https://www.baidu.com/', 'https://mail.163.com/', 'https://www.qq.com/']
#     g1 = gevent.spawn(download, urls[0])
#     g2 = gevent.spawn(download, urls[1])
#     g3 = gevent.spawn(download, urls[2])
#     gevent.joinall([g1, g2, g3])
"""直接看没注释的部分代码"""
import gevent
from gevent import monkey
monkey.patch_all()  # 必须在导入其他模块前调用  request是高级包,不用这个可以用urllib


from geventhttpclient import HTTPClient
from geventhttpclient.url import URL

def download(url):
    url_obj = URL(url)  # 将字符串转换为 URL 对象
    client = HTTPClient.from_url(url_obj)
    response = client.get(url_obj.request_uri)
    content = response.read()
    print(f'下载了{url}网站的数据, 长度: {len(content)}')

if __name__ == '__main__':
    urls = ['https://www.baidu.com/', 'https://mail.163.com/', 'https://www.qq.com/']
    g1 = gevent.spawn(download, urls[0])
    g2 = gevent.spawn(download, urls[1])
    g3 = gevent.spawn(download, urls[2])
    gevent.joinall([g1, g2, g3])   #这里记得加中括号
