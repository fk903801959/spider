from scrapy.cmdline import execute
import os

print('启动爬虫文件检测程序... ...')
spider_list = []
dirs = os.listdir('./spiders')
for file in dirs:
    if os.path.splitext(file)[1] == '.py' and os.path.splitext(file)[0] != '__init__':
        spider_list.append(os.path.splitext(file)[0])

print('已检测到的爬虫：')
for spider in spider_list:
    print(spider)

while True:
    name = input('请输入您想启动的爬虫名称：')
    for spider in spider_list:
        if name == spider:
            execute('scrapy crawl {}'.format(name).split())
            break
    print("\033[1;31mERROR:名称输入有误！\033[0m")

