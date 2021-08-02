from threading import Thread
import requests
from lxml import etree
from fake_useragent import UserAgent
from queue import Queue
import time

# 封装一个Thread子类Spider
class Spider(Thread):
    def __init__(self,url_queue):
        Thread.__init__(self) # 初始化父类方法
        self.url_queue = url_queue
    def run(self):
        while not self.url_queue.empty(): # 当url队列不为空时，持续获取队列中的url
            url = self.url_queue.get() # 获取队列
            print(url)
            headers = {'User-Agent':UserAgent().chrome}
            resp = requests.get(url,headers=headers)
            e = etree.HTML(resp.text)
            texts = [div.xpath('string(.)').strip() for div in  e.xpath("//div[@class='content']")]
            with open('duanzi/qiushibaike(Thread).txt','a',encoding='utf-8')as f:
                for text in texts:
                    f.write(text+'\n\n')

if __name__ == '__main__':
    base_url = "https://www.qiushibaike.com/text/page/{}/"
    # 将要爬去的url放在一个队列中，这里使用标准库Queue。
    url_queue = Queue() # 首先初始化一个Queue对象
    # 根据想获取的页数范围，利用for循环将1-5页的url地址依次添加到队列中
    for num in range(1,6):
        url_queue.put(base_url.format(num))

    for num in range(3): #同时开启三个线程
        # 在线程类参数中添加url队列对象
        spider = Spider(url_queue)
        # 启动当前线程
        spider.start()
