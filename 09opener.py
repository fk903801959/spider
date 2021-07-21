from urllib.request import Request,build_opener,HTTPHandler
from fake_useragent import UserAgent

url = "http://httpbin.org/get"
ua = UserAgent(path='json/fake_useragent_0.1.11.json')
headers = {"User-Agent":ua.random}
request = Request(url,headers=headers)

#构造HTTP控制器,指定参数可用于调试
handler = HTTPHandler(debuglevel=1)

opener = build_opener(handler)
response = opener.open(request)
# print(response.read().decode())