import scrapy
from scrapy_splash import SplashRequest

class Guazi2Spider(scrapy.Spider):
    name = 'guazi2'
    allowed_domains = ['guazi.com']
    # start_urls = ['http://guazi.com/']

    def start_requests(self):
        url = 'https://guazi.com/buy/'
        lua_script = '''
        function main(splash, args)
              assert(splash:go(args.url))
              assert(splash:wait(0.5))
              return splash:html()
            end
        '''
        yield SplashRequest(url,callback=self.parse,endpoint='execute',args={'lua_source':lua_script})


    def parse(self, response):
        print(response.text)
