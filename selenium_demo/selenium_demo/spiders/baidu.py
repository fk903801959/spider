import scrapy
from scrapy import signals
from selenium import webdriver
from time import sleep

class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    start_urls = ['http://www.baidu.com/']

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(BaiduSpider, cls).from_crawler(crawler, *args, **kwargs) # 初始化当前爬虫对象
        spider.driver = webdriver.Chrome()  # 在当前爬虫对象上创建一个谷歌浏览器驱动实例
        crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)
        return spider

    def spider_closed(self, spider):
        sleep(3)
        spider.driver.close()

    def parse(self, response):
        print(response.text)
