from fake_useragent import UserAgent
import requests

url = "https://www.12306.cn/index/"
headers = {"User_Agent":UserAgent().chrome}

# 禁用安全请求警告
requests.packages.urllib3.disable_warnings()
# verify=False，即表示不进行证书认证
resp = requests.get(url,verify=False,headers=headers)

resp.encoding='utf-8'
print(resp.text)
