import scrapy
from novel.items import bookinfo,bookcontent

class ZonghengSpider(scrapy.Spider):
    name = 'zongheng'
    allowed_domains = ['zongheng.com']
    start_urls = ['http://book.zongheng.com/showchapter/1038447.html']

    def parse(self, response):
        bookname = response.xpath("//h1//text()").extract_first()
        charpters = response.xpath("//li[@class=' col-4']/a/text()").extract()
        urls = response.xpath("//li[@class=' col-4']/a/@href").extract()

        item = bookinfo()
        item['bookname'] = bookname
        item['charpters'] = charpters
        yield item

        for url in urls:
            yield scrapy.Request(url,callback=self.book_content)

    def book_content(self,response):
        title = response.xpath("//div[@class='title_txtbox']/text()").extract_first()
        content = response.xpath("//div[@class='content']/p/text()").extract()

        item = bookcontent()
        item['title'] = title
        item['content'] = content
        yield item
