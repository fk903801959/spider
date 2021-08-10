# -*- coding:utf-8 -*-
# 赶集网登录的另一种方式：使用cookies值进行登录
# 原理：收集已登录用户界面的cookies值信息，利用其实现直接对用户个人主页的访问
# 1、由于start_urls对地址的访问不携带任何参数，故需重新定义start_requests()方法，并配置相关的请求参数
# 2、由于从页面直接拷贝的cookies字符串格式无法直接使用，故需通过split()方法进行切片操作，并将对应的键值对存储在新的cookies字典对象中。
# 3、调用Request方法，配置cookies参数，callback给parse()方法
# 4、parse()方法负责将响应得到的个人页面存储为html网页文件

import scrapy


class LogincookiesSpider(scrapy.Spider):
    name = 'logincookies'
    allowed_domains = ['ganji.com']
    # start_urls = ['http://www.ganji.com/vip/?_rid=0.10755585851648264']

    def start_requests(self):
        url = 'http://www.ganji.com/vip/?_rid=0.10755585851648264'
        str = 'ganji_uuid=4803615162776955069508; _gl_tracker={"ca_source":"www.baidu.com","ca_name":"se","ca_kw":"%E8%B5%B6%E9%9B%86%E7%BD%91|utf8","ca_id":"-","ca_s":"seo_baidu","ca_n":"-","ca_i":"-","sid":32106351055}; ganji_xuuid=c505f03c-f415-4f88-b3bb-26ce4050d3ce.1628556906362; GANJISESSID=m25mi7fq438pbv1in423rvn0au; lg=1; __utma=32156897.1519304637.1628556910.1628556910.1628556910.1; __utmc=32156897; __utmz=32156897.1628556910.1.1.utmcsr=bj.ganji.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmt=1; xxzl_deviceid=4HaxDEX6GmJQfoh4KjfJqitE+SiyGxLYOE7wfXsRzwlYJilOowepVW24EkHfnjJm; sscode=ISEj2iCbVmO0lj/mISbWpIGH; GanjiUserName=fk903801959; GanjiUserInfo={"user_id":814216789,"email":"","username":"fk903801959","user_name":"fk903801959","nickname":""}; bizs=[]; supercookie=BQR0ZwR2Amt5WQN1LwqxMwVkBJIzMTSxZzHkATRlAmqwZQV5AQOyATD2MzL5AwV0ATD=; username_login_n=fk903801959; GanjiLoginType=0; ganji_login_act=1628556937359; __utmb=32156897.3.10.1628556910; nTalk_CACHE_DATA={uid:kf_10111_ISME9754_814216789}; NTKF_T2D_CLIENTID=guest265595A5-53C4-7AB2-EF43-2D8ECAEF2748; xxzl_smartid=cb221a43e4c14cf7708dc6b047157b2c'
        cookies = {}
        for cookie in str.split(';'):
            key, value = cookie.split('=', 1)
            cookies[key] = value
        yield scrapy.Request(url,cookies=cookies,callback=self.parse)

    def parse(self, response):
        with open('UserPage.html','w',encoding='utf-8') as f:
            f.write(response.text)
