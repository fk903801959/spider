from urllib.request import urlopen,Request
from fake_useragent import UserAgent
from urllib.error import URLError

url = "http://www.sxt.cn/index/login"
headers = {"User-Agent":UserAgent(path="json/fake_useragent_0.1.11.json").random}
req = Request(url,headers=headers)

#捕获错误的响应信息
try:
    res = urlopen(req)
    print(res.read().decode())
except URLError as e:
    print(e)

print("爬取完成")