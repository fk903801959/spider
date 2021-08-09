# -*- coding: utf-8 -*-
# 介于Scrapy引擎和调度之间的中间件，从Scrapy引擎发送到调度的请求和响应
# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
from fake_useragent import UserAgent

class UserAgentMiddleware:
    def process_request(self, request, spider):
        request.headers.setdefault(b'User-Agent', UserAgent().random)

class ProxyMiddleware:
    def process_request(self,request,spider):
        proxy_ip = '222.74.202.229:9999'
        request.meta['proxy'] = 'http://' + proxy_ip