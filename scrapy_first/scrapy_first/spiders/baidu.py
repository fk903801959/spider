# -*- coding: utf-8 -*-
import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'baidu' # 爬虫名称
    allowed_domains = ['baidu.com'] # 允许爬取的域名
    start_urls = ['http://www.baidu.com/'] # 开始爬取信息的url地址

    # 解析器，用来接收响应回来的数据，并做相应的处理
    def parse(self, response):
        print(response.text)
