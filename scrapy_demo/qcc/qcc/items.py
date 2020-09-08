# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QccItem(scrapy.Item):
    cover = scrapy.Field()
    name = scrapy.Field()
    legal_representative = scrapy.Field()
    registered_capital = scrapy.Field()
    date_of_establishment = scrapy.Field()
    email = scrapy.Field()
    ipone = scrapy.Field()
    location = scrapy.Field()