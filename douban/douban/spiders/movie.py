import scrapy
from douban.items import DoubanItem

class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250?start={}&filter='.format(num*25) for num in range(0,3)]

    def parse(self, response):
        names = response.xpath("//span[@class='title'][1]/text()").extract()
        stars = response.xpath("//span[@class='rating_num']/text()").extract()
        urls = response.xpath("//div[@class='hd']/a/@href").extract()
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

        for url in urls:
            yield scrapy.Request(url,callback=self.parse_info)

    def parse_info(self,response):
        movie_name = response.xpath("//div[@id='content']/h1/span[1]").extract()
        director = response.xpath("//span[1]/span[@class='attrs']/a").extract()


