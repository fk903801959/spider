# -*- coding:utf-8 -*-
# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface


from scrapy.http import HtmlResponse


class SeleniumMiddleware:
  def process_request(self, request, spider):
      spider.driver.get(request.url)  # 使用浏览器驱动打开指定页面，其中url参数为请求包中的url
      html = spider.driver.page_source # 获取网页的源代码

      # 返回响应的html请求，这一步的目的是阻止请求包被交给下载器，让下载器下载。
      return HtmlResponse(url=request.url,body=html,request=request,encoding='utf-8')

