import scrapy
from douban.items import DoubanItem

class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        names = response.xpath("//span[@class='title'][1]/text()").extract()
        stars = response.xpath("//span[@class='rating_num']/text()").extract()

        # for name,star in zip(names,stars):
        #    # 通过yield方式将数据推送到piplines中
        #     yield {
        #         'name':name,
        #         'star':star
        #     }

        item = DoubanItem()
        for name,star in zip(names,stars):
             item['name'] = name
             item['star'] = star
             yield item

