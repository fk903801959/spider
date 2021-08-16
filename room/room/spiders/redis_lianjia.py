import scrapy
from room.items import RoomItem
from scrapy_redis.spiders import RedisSpider

class LianjiaSpider(RedisSpider):
    name = 'redis_lianjia'
    allowed_domains = ['lianjia.com']

    # 对于RedisSpider对象而言，rdis_key相当于普通Spider对象里的start_urls，是开始爬取的起始地址，应预先存储在redis库中。
    redis_key = "lianjia:start_urls"
    index = 1

    # start_urls = ['https://hui.lianjia.com/ershoufang/']

    def parse(self, response):
        base_url = 'https://hui.lianjia.com/ershoufang/pg{}/'
        all_urls = response.xpath("//div[@class='info clear']/div/a/@href").extract()
        for url in all_urls:
            yield scrapy.Request(url,callback=self.parse_info)

        yield scrapy.Request(base_url.format(self.index+1),callback=self.parse)
        self.index += 1

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

        item = RoomItem()
        item['total'] = total
        item['community_name'] = community_name
        item['areaName'] = areaName
        item['hu_xing'] = hu_xing
        item['mian_ji'] = mian_ji
        item['chao_xiang'] = chao_xiang
        item['zhaung_xiu'] = zhaung_xiu
        item['dian_ti'] = dian_ti
        item['di_ya'] = di_ya
        item['yong_tu'] = yong_tu
        yield item