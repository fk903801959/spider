import json
from urllib.request import urlopen,Request
from time import sleep

url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=20"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 Edg/91.0.864.71"}

i = 0
base_url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start={}&limit=20"

def write_info(info):
    with open('douban_movie/movie_list.txt','a',encoding='utf-8') as f:
        f.write(info)

while True:
    request = Request(base_url.format(i*50), headers=headers)
    response = urlopen(request)
    info = response.read().decode()
    if info == '[]':
        print("电影列表已全部读取")
        break
    else:
        i += 1
    write_info(info)
    print("成功写入第{}条数据".format(i))
    sleep(5)


