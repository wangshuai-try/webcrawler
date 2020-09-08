import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from qcc.items import *

class QySpider(CrawlSpider):
    name = 'qy'
    allowed_domains = ['qcc.com']
    start_urls = ['https://www.qcc.com/g_AH.html']

    rules = (
        Rule(LinkExtractor(allow=r'g_[A-Z]{2,}\.html',
                           deny=r'g_[A-Z]{2,}_\d+\.html'),
            callback='parse_item', follow=True),

        Rule(LinkExtractor(restrict_css=r'.pagination'),
            callback='parse_item', follow=True)
    )

    def parse_item(self, response):
        item = {}
        # item = QccItem()
        trs = response.css('.m_srchList tr')
        for tr in trs:
            item['cover'] = tr.xpath('./td[1]/img/@src').get()
            # item['images'] = []
            item['name'] = tr.xpath('./td[2]/a/text()').get()
            item['legal_representative'] = tr.xpath('./td[2]/p[1]/a/text()').get() # 法定代表人
            item['registered_capital'] = tr.xpath('./td[2]/p[1]/span[1]/text()').get().split('：')[1] # 注册资本
            item['date_of_establishment'] = tr.xpath('./td[2]/p[1]/span[2]/text()').get().split('：')[1] # 成立日期
            item['email'] = tr.xpath('./td[2]/p[2]/text()').get().strip().split('：')[1]
            item['ipone'] = tr.xpath('./td[2]/p[2]/span/text()').get().split('：')[1]
            item['location'] = tr.xpath('./td[2]/p[3]/text()').get().strip().split('：')[1]

            yield item
