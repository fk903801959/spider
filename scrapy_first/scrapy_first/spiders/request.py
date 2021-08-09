# -*- coding: utf-8 -*-
import scrapy


class RequestSpider(scrapy.Spider):
    name = 'request'
    allowed_domains = ['httpbin.org']
    # start_urls = ['']

    def start_requests(self):
        url = 'http://httpbin.org/get'
        for num in range(3):
            yield scrapy.Request(url, callback=self.parse, dont_filter=True) # dont_filter意为不去重，默认为False即默认去重，若改为True即不去重。

    def parse(self, response):
        print(response.text)
