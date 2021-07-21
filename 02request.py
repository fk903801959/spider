from urllib.request import urlopen
from urllib.request import Request
from random import choice

url = "http://www.baidu.com/"
#创建User-Agent列表
user_agents=[
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "AppleWebKit/537.36 (KHTML, like Gecko)"
]

# 从列表中随机选取user-agents
headers = {
    "User-Agent":choice(user_agents)
}



#加入了一个request对象，因为在构造请求时可能还会添加许多内容，通过构建一个request，服务器响应应答的请求，逻辑上更清晰明确
request = Request(url, headers=headers)
# print(request.get_header("User-agent"))

response = urlopen(request)
print(response.read().decode())

