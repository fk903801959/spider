import requests
from fake_useragent import UserAgent

url ="http://127.0.0.1:8000/stu/tologin/"
headers = {"User-Agent":UserAgent().chrome}
data = {
    "sname":"张三",
    "spwd":"123456"
}
resp = requests.post(url,headers=headers,data=data)
resp.encoding = "utf-8"
print(resp.text)