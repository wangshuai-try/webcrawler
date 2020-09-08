import uuid

import scrapy
from scrapy.http import Response, HtmlResponse, Request
from scrapy_demo.items import *


class WanbenSpider(scrapy.Spider):
    name = 'wanben'
    allowed_domains = ['qidian.com', 'book.qidian.com', 'read.qidian.com', 'vipreader.qidian.com']
    start_urls = ['https://www.qidian.com/finish']

    def parse(self, response: Response):
        """获取小说信息"""
        items = BookItem()
        if response.status == 200:
            # print(response.text)
            lis = response.css('.all-img-list li')
            for li in lis:
                items['book_id'] = uuid.uuid4().hex
                items['book_url'] = li.xpath('./div/a/@href').get()
                items['book_name'] = li.xpath('./div/h4//text()').get()
                items['author'], *items['tags'] = li.css('.author a::text').extract()
                items['description'] = li.xpath('./div/p[2]//text()').get()
                items['img'] = li.css('.book-img-box img::attr("src")').get()

                yield Request('https://' + items['book_url'] + '#Catalog',
                              callback=self.parse_info,
                              priority=100,
                              meta={'book_id': items['book_id']})

                yield items

            # 获取下一页的链接
            next_url = response.css(
                '.lbf-pagination-item-list').xpath('./li[last()]/a/@href').get()

            if next_url.find('javascript') == -1:
                # priority高的优先执行
                yield Request('https:' + next_url, priority=1)

    def parse_info(self, response: Response):
        """获取章节信息"""
        book_id = response.meta['book_id']
        seg_as = response.xpath('//div[@class="volume-wrap"]/div').css('.cf  li>a')
        for a in seg_as:
            item = SegItem()
            item['seg_id'] = uuid.uuid4().hex
            item['book_id'] = book_id
            item['seg_title'] = a.css('::text').get()
            item['url'] = 'https:' + a.css('::attr("href")').get()

            # 下载章节内容
            yield Request(item['url'],
                          callback=self.parse_seg,
                          priority=10,
                          meta={'book_id': book_id,
                                'seg_id': item['seg_id']})

            yield item

    def parse_seg(self, response: Response):
        """获取章节内容"""

        item = SegDetailItem()
        item['book_id'] = response.meta['book_id']
        item['seg_id'] = response.meta['seg_id']
        content = '<br>'.join(response.css('.read-content p::text').extract())
        item['content'] = content.replace('\u3000', '').replace('\n', '')

        yield item
