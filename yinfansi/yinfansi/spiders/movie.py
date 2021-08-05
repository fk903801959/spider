import scrapy
from yinfansi.items import MovieListItem,MovieInfoItem

class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['yinfans.net']
    n = int(input("请输入你要获取的页数："))
    start_urls = ['https://www.yinfans.net/page/{}'.format(i) for i in range(1,n+1)]

    def parse(self, response):
        names = response.xpath("//h2/a/text()").extract()
        urls = response.xpath("//h2/a/@href").extract()
        item = MovieListItem()
        for name in names:
            item['name'] = name
            yield item

        for url in urls:
            yield scrapy.Request(url,callback=self.parse_info)


    def parse_info(self,response):
        movie_name = response.xpath("//h1/text()").extract()
        tags = response.xpath("//div[@class='tagcloud']/a[@rel]/text()").extract()
        str_movie_name = ''.join(movie_name)
        str_tags = ','.join(tags)

        item = MovieInfoItem()
        item['movie_name'] = str_movie_name
        item['tag'] = str_tags
        yield item

