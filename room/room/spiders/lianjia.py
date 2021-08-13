import scrapy


class LianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    allowed_domains = ['lianjia.com']
    start_urls = ['https://hui.lianjia.com/ershoufang/']

    def parse(self, response):
        all_urls = response.xpath("//div[@class='info clear']/div/a/@href").extract()
        for url in all_urls:
            yield scrapy.Request(url,callback=self.parse_info)

    def parse_info(self,response):
        total = response.xpath("concat(//div[@class='price ']/span[@class='total'],//div[@class='price ']/span[@class='unit'])").extract_first()
        community_name = response.xpath("//div[@class='communityName']/a[1]/text()").extract_first()
        areaName = response.xpath("string(//div[@class='areaName']/span[2])").extract_first()
        base = response.xpath("//div[@class='content']/ul")
        hu_xing = base.xpath("./li[1]/text()").extract_first()
        mian_ji = base.xpath("./li[3]/text()").extract_first()
        chao_xiang = base.xpath("./li[7]/text()").extract_first()
        zhaung_xiu = base.xpath("./li[9]/text()").extract_first()
        dian_ti = base.xpath("./li[last()]/text()").extract_first()

        transaction = response.xpath("//div[@class='transaction']/div[@class='content']/ul")
        di_ya = transaction.xpath("./li[last()-1]/span[2]/text()").extract_first().strip()
        yong_tu = transaction.xpath("./li[4]/span[2]/text()").extract_first()
