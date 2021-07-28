from fake_useragent import UserAgent
import  requests
from jsonpath import jsonpath

url = 'https://www.lagou.com/lbs/getAllCitySearchLabels.json'
headers = {'User-Agent':UserAgent().chrome}
resp = requests.get(url,headers=headers)
# print(resp.text)

# 注意：第一个参数为一个json对象，而且Jsonpath语法通常是由$从根节点开始
ids = jsonpath(resp.json(),'$..id')
names = jsonpath(resp.json(),'$..name')

for id,name in zip(ids,names):
    print(id,":",name)