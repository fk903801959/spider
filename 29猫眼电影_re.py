from fake_useragent import UserAgent
import requests
from re import findall
from time import sleep

# 获取指定url地址的页面信息
def get_html(url):
    headers = {'User-Agent':UserAgent().chrome}
    resp = requests.get(url,headers=headers)
    sleep(3)
    # 如果状态码为200，即页面信息返回成功
    if resp.status_code == 200:
        # 返回的是中文页面，页面信息使用utf-8编码
        resp.encoding = 'utf-8'
        return resp.text
    else:
        print("页面信息获取失败！")
        return None

# 获取页面信息中关于电影列表的url信息
def parse_list(html):
    if html:
        a_list = findall(r'<div class="channel-detail movie-item-title".+>\s+<a href="(/films/\d+)"',html)
        # 由于每次获得的电影地址为相对路径，故需要在每条相对路径前加上'https://maoyan.com'形成网页的绝对路径
        list_url = ['https://maoyan.com{}'.format(url) for url in a_list]
        return list_url

# 获取每个电影的具体信息，包括电影名称、类型、导演和演员
def parse_index(html):
    # 电影名称
    name = findall(r'<h1 class="name">(.+)</h1>',html)[0]
    # 电影类型
    type = findall(r'<a class="text-link".+target="_blank">(.+)</a>',html)
    # 演员列表
    actors_a = findall(r'<li class="celebrity actor".+>\s+<a.+>\s+<img.+>\s+</a>\s+<div.+>\s+<a.+>\s+(.+)\s+',html)
    actors = format_data(actors_a)
    return{"name":name,"type":type,"actors":actors}


# 由于得到的演员信息存在重复，需进行去重处理，用到了set()方法
def format_data(actors):
    # set() 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等。
    actor_set = set()
    for actor in actors:
        actor_set.add(actor.strip())
    return actor_set

def main():
    num = int(input("请输入你要获取的页数："))
    for page in range(num):
        url = 'https://maoyan.com/films?showType=3&offset={}'.format(page*30)
        list_html = get_html(url)
        list_url = parse_list(list_html)
        for url in list_url:
            info_html = get_html(url)
            movie = parse_index(info_html)
            print(movie)

if __name__ == '__main__':
    main()