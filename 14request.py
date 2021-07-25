import requests
from fake_useragent import UserAgent

url = "https://www.baidu.com/s"

args ={
    "wd":"尚学堂"
}
headers = {"User-Agent":UserAgent().chrome}
response = requests.get(url,params=args,headers=headers)
response.encoding = "utf-8"
print(response.text)
