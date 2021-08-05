from fake_useragent import UserAgent
import requests
from lxml import etree

# 发送请求(下载器)
class Downloader:
    # 向指定url的服务器发出请求包，并将返回得到的响应包中页面的文本内容以text类型返回
    def do_download(self, url):
        print(url)
        headers = {'User-Agent': UserAgent().chrome}
        resp = requests.get(url, headers=headers)
        if resp.status_code == 200:
            resp.encoding = 'utf-8'
            return resp.text


# 数据解析
class Parser:
    def do_parse(self,html):
        e = etree.HTML(html)
        titles = e.xpath("//h2/a/text()")
        urls = [str(a) for a in e.xpath("//div[@class='pagination']/a/@href")]
        return titles,urls


# 数据保存
class DataOutPut:
    def do_save(self, datas):
        with open('yinfansi_movie/movie_title.txt', 'a', encoding='utf-8') as f:
            for data in datas:
                f.write(data+'\n')


# ulr管理器
class URLManager:
    def __init__(self):
        # set() 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等。
        self.new_url = set()  # 创建一个新的url元素集，用来存储将用来爬取的url字符
        self.old_url = set()  # 创建一个旧的url元素集，用来记录已经被使用过的url字符

    # 在新url元素集中只加入一个url
    def add_new_url(self, url):
        # 当获取到的url不为空值，不为空字符串，且在旧的url元素集中不存在，再将其添加到新的url元素集中。
        if url is not None and url != '' and url not in self.old_url:
            self.new_url.add(url)

    # 在新url元素集中批量加入多个url
    def add_new_urls(self, urls):
        for url in urls:
            if url is not None and url != '' and url not in self.old_url:
                self.new_url.add(url)

    # 从新url元素集中获取一个url，并将其记录到旧url元素集中
    def get_new_url(self):
        url = self.new_url.pop()
        self.old_url.add(url)
        return url

    # 获取还有多少个url要爬取
    def get_new_url_size(self):
        return len(self.new_url)

    # 判断是否还有url要爬取
    def have_new_url(self):
        return self.get_new_url_size() > 0


# 调度器
class Scheduler:
    def __init__(self):
        self.downloader = Downloader()  # 下载器
        self.parser = Parser()  # 解析器
        self.data_out_put = DataOutPut()  # 保存器
        self.url_manager = URLManager()  # url管理器

    def start(self, url):
        # 调用url管理器，将指定url保存至新的url元素集中。
        self.url_manager.add_new_url(url)
        # 循环从新的url列表中爬取数据，当新的url列表中全部爬取完成后（为空），此时跳出循环
        while self.url_manager.have_new_url():
            # 从新的url元素集中取出一个url字符串，同时将其放入到旧的url元素集中。
            url = self.url_manager.get_new_url()
            # 调用下载器，获取指定url的页面信息，以text文本格式返回。
            html = self.downloader.do_download(url)
            # 调用解析器，获取网页文本文件中的具体信息内容，分别赋值给datas(保存页面指定元素)和urls(接下来要跳转的链接列表)。
            datas, urls = self.parser.do_parse(html)
            # 调用保存器，对页面指定元素数据进行保存。
            self.data_out_put.do_save(datas)
            # 调用url管理器，将获取到的准备跳转的链接列表保存到新的url元素集中。
            self.url_manager.add_new_urls(urls)


if __name__ == '__main__':
    scheduler = Scheduler()
    url = 'https://www.yinfans.net'
    scheduler.start(url)
