#PyQuery是一个类似于jQuery的解析网页工具，使用lxml操作xml和html文档，它的语法和jQuery很像。
# 和XPATH，Beautiful Soup比起来，PyQuery更加灵活，提供增加节点的class信息，移除某个节点，提取文本信息等功能。
# html文档的所有操作都需要PyQuery对象来完成，初始化PyQuery对象主要有三种方式，分别是通过网址、字符串和文件名创建。

from fake_useragent import UserAgent
import requests
# import PyQuery类，然后将字符串传递给PyQuery类，这样就生成了一个PyQuery对象
from pyquery import PyQuery as pq

url = 'http://www.zongheng.com/rank/details.html?rt=3&d=1'
headers = {'User-Agent':UserAgent().chrome}
resp = requests.get(url,headers=headers)

doc = pq(resp.text)
names = [a.text for a in doc('.rank_d_b_name a')]
authors_a = doc('.rank_d_b_cate a')

# 定义一个用于存储作者姓名的列表
author_list=[]

for num in range(len(authors_a)):
    if num % 3 == 0:
       author_list.append(authors_a[num].text)

for i, name, author in zip(range(len(authors_a)),names,author_list):
    print(i+1,".","《",name,"》"," ","作者：",author)
