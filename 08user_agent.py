from urllib.request import urlopen,Request
from fake_useragent import UserAgent

url = "http://httpbin.org/get"
ua = UserAgent(path='json/fake_useragent_0.1.11.json')
headers = {"User-Agent":ua.random}
request = Request(url,headers=headers)
response = urlopen(request)
print(response.read().decode())