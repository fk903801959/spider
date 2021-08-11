import scrapy


class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3&offset={}'.format(num*30) for num in range(1)]

    def parse(self, response):
        names = response.xpath("//div[@class='channel-detail movie-item-title']/@title").extract()
        stars = [div.xpath('string(.)').extract_first() for div in response.xpath("//div[@class='channel-detail channel-detail-orange']")]
        print(names)
        print(stars)