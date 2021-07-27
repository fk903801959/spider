import requests
from fake_useragent import UserAgent
import re

url = 'https://www.qiushibaike.com/text/'
headers = {'User-Agent':UserAgent().chrome}
requests.packages.urllib3.disable_warnings()
response = requests.get(url,headers=headers,verify = False)
# print(response.text)

contents = re.findall(r'<div class="content">\n*<span>\n*(.+)',response.text)
for info in contents:
    print(info)