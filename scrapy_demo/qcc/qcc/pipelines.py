# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import os
from csv import DictWriter
from itemadapter import ItemAdapter
from qcc.items import *
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request


class QccPipeline:
    # 处理企业所有信息管道
    def __init__(self):
        self.qiye_list = 'qiye_list.csv'

    def save_csv(self, item, filename):
        is_hander = os.path.exists(filename)
        with open(filename, 'a', encoding='utf-8', newline='') as f:
            writer = DictWriter(f, fieldnames=item.keys())
            if not is_hander:
                writer.writeheader()
            writer.writerow(item)

    def process_item(self, item, spider):
        if isinstance(item, QccItem):
            self.save_csv(item, self.qiye_list)
        return item


class QiYeImagesPipeline(ImagesPipeline):
    # 处理图片管道
    DEFAULT_IMAGES_URLS_FIELD = 'cover'
    DEFAULT_IMAGES_RESULT_FIELD = 'path'

    # def get_media_requests(self, item, info):
    #     return [Request(item.get('cover'),
    #                     meta={'name': item.get('name')})]
    #
    # def item_completed(self, results, item, info):
    #     item['path'] = [v['path'] for ok, v in results if ok]
    #     return item
    #
    # def file_path(self, request, response=None, info=None):
    #     # 返回图片的路径
    #     name = request.meta['name']
    #     return f'{name}.jpg'

    def get_media_requests(self, item, info):
        return Request(
            item.get('cover'),
            meta={
                'name': item.get('name')
            }
        )

    def item_completed(self, results, item, info):
        item['path'] = [v['path'] for ok, v in results if ok]
        return item

    def file_path(self, request, response=None, info=None):
        url_name = request.meta['name']
        return f'{url_name}.jpg'
