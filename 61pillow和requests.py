#第三方  pillow  之前的都是官方的
#request就是浏览器
import requests
from PIL import Image
im = Image.open('61pic.jpeg')
#im.show()
response = requests.get('https://www.12306.cn/index/')  #https 是做了安全处理的
print(response)  #打印的是响应码
# 打印响应的状态码
print(f"Status Code: {response.status_code}")

# 打印响应的文本内容
print(f"Response Text: {response.text}")#响应码还得解读处理

# 如果需要处理二进制内容，可以使用 response.content
# print(f"Response Content: {response.content}")