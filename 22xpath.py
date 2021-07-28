# XPath 是一门在 XML 文档中查找信息的语言。XPath 可用来在 XML 文档中对元素和属性进行遍历。XPath 是 W3C XSLT 标准的主要元素，
# 并且 XQuery 和 XPointer 都构建于 XPath 表达之上.
from fake_useragent import UserAgent
import requests
from lxml import etree

headers = {"User-Agent":UserAgent().chrome}

def Print_List(resp,i):
    # 首先我们使用 lxml 的 etree 库，然后利用 etree.HTML 初始化，然后我们将其打印出来。
    # lxml 的一个非常实用的功能就是自动修正 html 代码
    e= etree.HTML(resp.text)
    list_name = e.xpath('//div[@class="rank_i_title_name fl"]/a/text()')
    book_names = e.xpath('//div[@class="rank_d_b_name"]/a/text()')
    authors = e.xpath('//div[@class="rank_d_b_cate"]/a[@href]/text()')

    if i == 0:
        print(list_name[0])
    for book_name,author in zip(book_names, authors):
        i += 1
        print(i,".","《",book_name,"》"," ","作者：",author)


for i in range(1,10):
    url = 'http://www.zongheng.com/rank/details.html?rt=1&d=1&i=2&p={}'.format(i)
    resp = requests.get(url, headers=headers)
    Print_List(resp,(i-1)*20)





