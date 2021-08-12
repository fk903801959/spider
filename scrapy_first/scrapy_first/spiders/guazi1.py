import scrapy
from scrapy_splash import SplashRequest

class Guazi1Spider(scrapy.Spider):
    name = 'guazi1'
    allowed_domains = ['guazi.com']
    # start_urls = ['http://guazi.com/']

    def start_requests(self):
        url = 'https://www.guazi.com/buy/'
        yield SplashRequest(url,callback=self.parse,args={'wait':2})


    def parse(self, response):
        print(response.text)
