from fake_useragent import UserAgent
import requests

url = "http://httpbin.org/get"
headers = {"User_Agent":UserAgent().chrome}

proxy={
    # "http":"http://ip:port"
    # "http":"name:password@http://ip:prt"
    'http':'http://60.217.64.237:38829'
}

res = requests.get(url,proxies=proxy,headers=headers)
print(res.text)