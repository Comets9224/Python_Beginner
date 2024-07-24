import hashlib  #md5加密算法  单向的，没法解
import os
# 生成随机盐
def generate_salt():
    return os.urandom(16)
# 计算加盐后的哈希值
def hash_with_salt(message, salt):
    return hashlib.sha256(salt + message.encode('utf-8')).hexdigest()
msg='中午一起吃饭'
md5=hashlib.md5(msg.encode('utf-8')) #md5是加密算法   md5算法不能直接放中文,需要编码
print(md5.hexdigest())  #得到十六进制的值   201a0589ccabcdc8e6f4658eb850a71c
#哈希函数的设计目的是为了验证数据完整性和快速查找，而不是数据加密和解密。
#双向解密算法  base64  ——base64其实是编码方式

sha1=hashlib.sha1(msg.encode('utf-8'))
print(sha1.hexdigest())
sha256=hashlib.sha256(msg.encode('utf-8'))
print(sha256.hexdigest())
salt=generate_salt()
print(hash_with_salt(msg, salt))
print(f"Salt: {salt.hex()}")  #实际上 hexdigest  已经得到是十六进制了
#sha256.update 是 Python hashlib 模块中的一个方法，用于逐步更新哈希对象的内容。这在处理大文件或需要分块处理数据时特别有用。