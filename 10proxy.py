from urllib.request import Request,build_opener,ProxyHandler
from fake_useragent import UserAgent

url = "http://httpbin.org/get"
ua = UserAgent(path='json/fake_useragent_0.1.11.json')
headers = {"User-Agent":ua.random}
request = Request(url,headers=headers)

# 创建一个ProxyHandler控制器，用于设置匿名ip
handler = ProxyHandler({"http":"47.107.128.69:888"})
#如果使用的是独享代理，格式应为："http":"name:password@ip:port"


# 在build_opener方法中使用ProxyHandler控制器
opener = build_opener(handler)

response = opener.open(request)
print(response.read().decode())
