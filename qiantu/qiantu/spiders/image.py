import scrapy
import pypinyin

def pinyin(word):
    s = ""
    for i in pypinyin.pinyin(word,style=pypinyin.NORMAL):
        s += "".join(i)
    return s

search_CN = str(input('请输入搜索信息：'))
search = pinyin(search_CN)

class ImageSpider(scrapy.Spider):
    name = 'image'
    allowed_domains = ['58pic.com']

    start_urls = ['https://www.58pic.com/tupian/{}-0-0-{}.html'.format(search,num) for num in range(1,4)]

    def parse(self, response):
        urls = response.xpath('//div[@class="qtw-card normalCard"]/a/@href').extract()
        for url in urls:
            yield scrapy.Request(response.urljoin(url),callback=self.parse_img)

    def parse_img(self,response):
        id = response.xpath('string(//p[@class="pic-code"]/span/@data-val)').extract_first()
        name = response.xpath('string(//div[@class="main"]/img[3]/@title)').extract_first()
        image_name = id + "-" + name
        image_urls = 'https:' + response.xpath('string(//div[@class="main"]/img[3]/@src)').extract_first()

        yield {
            'image_name': image_name,
            'image_urls': [image_urls]
        }

