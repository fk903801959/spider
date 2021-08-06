import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from novel.items import bookcontent2


class Zongheng2Spider(CrawlSpider):
    name = 'zongheng2'
    allowed_domains = ['zongheng.com']
    start_urls = ['http://book.zongheng.com/showchapter/917017.html']

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//div/ul/li[@class=" col-4"][1]/a'), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths='//div[@class="chap_btnbox"]/a[3]'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = bookcontent2()
        item['title'] = response.xpath('//div[@class="title_txtbox"]/text()').extract_first().strip()
        item['content'] = response.xpath('//div[@class="content"]/p/text()').extract()
        yield item
