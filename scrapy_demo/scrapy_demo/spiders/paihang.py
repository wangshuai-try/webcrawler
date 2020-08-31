import scrapy
from scrapy.http import Request, Response


class PaihangSpider(scrapy.Spider):
    name = 'paihang'
    allowed_domains = ['www.qidian.com']
    start_urls = ['https://www.qidian.com/rank/yuepiao']

    def parse(self, response: Response):
        # rank_header = response.css('.rank-header h3::text')
        # timeup = response.css('.rank-header h3').xpath('./span/em/text()')
        lis = response.css('.book-img-text ul li')
        for li in lis:
            book_name = li.xpath('./div/h4/a/text()')
            book_author, *book_tag = li.xpath('./div[2]/p[1]/a/text()|./div[2]/p[1]/span/text()')
            book_description = li.xpath

