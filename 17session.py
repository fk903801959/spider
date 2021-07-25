from fake_useragent import UserAgent
import requests

login_url = "http://127.0.0.1:8000/student/tologin/"
from_data={
    "sname":"zhangsan",
    "spwd":"123456"
}
headers = {"User-Agent":UserAgent().chrome}

# 创建一个session对象，可用来保存cookie值
session = requests.Session()
session.post(login_url, data=from_data, headers=headers)

info_url = 'http://127.0.0.1:8000/student/tologin/stu_index/'
resp = session.get(info_url,headers=headers)
print(resp.text)