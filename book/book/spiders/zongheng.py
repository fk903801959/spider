import scrapy


class ZonghengSpider(scrapy.Spider):
    name = 'zongheng'
    allowed_domains = ['zongheng.com']
    start_urls = ['http://www.zongheng.com/rank/details.html?rt=1&d=1&i=2']

    def parse(self, response):
        # extract():它返回一个unicode字符串以及所选数据
        booknames = response.xpath("//div[@class='rank_d_b_name']/@title").extract()
        authors = response.xpath("//div[@class='rank_d_b_cate']/@title").extract()
        books = []
        for bookname,author in zip(booknames,authors):
            books.append({
                'bookname':bookname,
                'author':author
            })
        return books
