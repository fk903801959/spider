import scrapy

class ZolSpider(scrapy.Spider):
    name = 'zol'
    allowed_domains = ['zol.com.cn']
    start_urls = ['https://desk.zol.com.cn/bizhi/9720_117444_2.html']

    def parse(self, response):
        # 获取图片名称和地址标签
        image_name = response.xpath('string(//h3)').extract_first().strip()
        image_url = response.xpath('//img[@id="bigImg"]/@src').extract()

        yield {
            'image_name' : image_name,
            'image_urls' : image_url
        }
        # 获取下一页图片的url相对路径
        next_url = response.xpath("//a[@id='pageNext']/@href").extract_first()
        # 利用urljoin()方法，将获取到的url相对路径与基地址形成绝对路径，并使用callback进行回调
        yield scrapy.Request(response.urljoin(next_url),callback=self.parse)

