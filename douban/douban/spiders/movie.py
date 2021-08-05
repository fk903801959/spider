import scrapy
from douban.items import MovieListItem,MovieInfoItem

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

        item = MovieListItem()
        for name,star in zip(names,stars):
             item['name'] = name
             item['star'] = star
             yield item

        for url in urls:
            yield scrapy.Request(url,callback=self.parse_info)

    def parse_info(self,response):
        movie_names = response.xpath("//h1/span[1]/text()").extract()
        directors = response.xpath("//span[1]/span[@class='attrs']/a").extract()
        types = response.xpath("//span[@property='v:genre']").extract()

        item = MovieInfoItem()
        for movie_name,director,type in zip(movie_names,directors,types):
            item['movie_name'] = movie_name
            item['director'] = director
            item['type'] = type
            yield item




