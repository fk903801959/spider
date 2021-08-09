# -*- coding:utf-8 -*-
# 模拟登录方法实验：（以赶集网登录为例）
# 1、在parse方法中，先访问登录界面，利用正则表达式获取当前页面元素中的用于生成随机验证码的hash值
# 2、利用scrapy中的Request方法访问验证码的url，并callback给下一个方法do_format，同时利用meta参数传递hash值
# 3、在do_format方法中，将验证码网页的body标签保存为二进制图片文件，方便观察和后续输入
# 4、在formdata会话表单中填入基本的键值对（可从原网页中截获请求包来查看）
# 5、利用scrapy中的FormRequest方法,指定url地址为登录界面，同时选择用post方法提交会话表单，并callback给下一个方法after_login
# 6、在after_login中打印响应包中的具体内容（可看到登录状态，用户id，登录成功后下一个url跳转地址等）

import re

import scrapy


class GanjiSpider(scrapy.Spider):
    name = 'ganji'
    allowed_domains = ['ganji.com']
    start_urls = ['https://passport.ganji.com/login.php']

    def parse(self, response):
        hash_code = re.search(r'"__hash__":"(.+)"',response.text).group(1)
        image_url = 'https://passport.ganji.com/ajax.php?dir=captcha&module=login_captcha&nocache=1628514320766'
        yield scrapy.Request(image_url,callback=self.do_format,meta={'hash_code':hash_code})
        # 关于Request中meta参数的补充知识点：meta是一个字典，它的主要作用是用来传递数据的，meta = {‘key1’:value1}，
        # 如果想在下一个函数中取出value1, 只需得到上一个函数的meta[‘key1’]即可， 因为meta是随着Request产生时传递的，
        # 下一个函数得到的Response对象中就会有meta，即response.meta.

    def do_format(self,response):
        hash_code = response.request.meta['hash_code']
        with open('yzm.jpg','wb') as f:
            f.write(response.body)
        code = str(input('请输入验证码：'))
        form_data = {
            'username': 'fk903801959',
            'password': '98224NUMcapSCR',
            'setcookie': '0',
            'checkCode': code,
            'next': '',
            'source': 'passport',
            '__hash__': hash_code,
        }
        login_url = 'https://passport.ganji.com/login.php'
        yield scrapy.FormRequest(login_url,method='POST',formdata=form_data,callback=self.after_login)

    def after_login(self,response):
        print(response.text)