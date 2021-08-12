import requests
from fake_useragent import UserAgent

url = "https://www.guazi.com/huizhou/buy/"
base_url = "http://localhost:8050/render.html?url={}&wait=2".format(url)
response = requests.get(base_url,headers={'User-Agent':UserAgent().chrome})
response.encoding = 'utf-8'
print(response.text)
