# Coding: utf-8
# Author: Wang Shuai
# Author_Email: wangshuai@ximalayaos.com
# Time: 2020/8/12 0012 23:07
# File: gushici.py
# Project_Name: webCrawler
# Content: 爬取古诗词
import time
import uuid

import requests, csv, os
from lxml import etree
from urllib.parse import urlencode
from multiprocessing.pool import Pool
from common.common_mysql import *

is_file_names = False

# url = 'https://so.gushiwen.cn/shiwen/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/84.0.4147.89 Safari/537.36',
    'cookie': 'login=flase; Hm_lvt_04660099568f561a75456483228a9516=1597244990; Hm_lpvt_'
              '04660099568f561a75456483228a9516=1597244990'
}


def parse(html):
    items = {}
    tree = etree.HTML(html)
    divs = tree.xpath('//div[@class="left"]/div[@class="sons"]')
    for div in divs:
        items['id'] = uuid.uuid4().hex
        items['name'] = div.xpath('.//p[1]/a//text()')[0]
        items['author'] = ' '.join(div.xpath('.//p[2]/a/text()'))
        items['content'] = '<br>'.join(div.xpath('.//div[@class="contson"]//text()'))
        items['tag'] = ','.join(div.xpath('.//div[@class="tag"]/a//text()'))

        yield items


def get(page, type):
    url = 'https://so.gushiwen.cn/shiwen/default.aspx?'
    parame = {
        'page': page,
        'type': type,
        'id': 0
    }
    base_url = url + urlencode(parame)
    try:
        resp = requests.get(base_url, headers=headers)
        if resp.status_code == 200:
            return resp.text
    except Exception as e:
        raise print('请求失败', e)


def sava(data):
    global is_file_names
    fieldnames = ('id', 'name', 'author', 'content', 'tag')
    with open('../result/gushici.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if not is_file_names:
            writer.writeheader()
            is_file_names = True
        writer.writerow(data)


def main():
    # start_time = time.time()
    # for page in range(1, 101):
    #     html = get(page)
    #     results = parse(html)
    #     for result in results:
    #         # sava(result)
    #         with Pool(processes=5) as pool:
    #             pool.map(sava, [result for result in results])
    #             pool.close()
    #             pool.join()
    #         end_time = time.time()
    #         all_time = end_time - start_time
    #         print(f'爬取{page}页，总耗时{all_time}')
    start_time = time.time()
    for page in range(1, 21):
        html = get(page, 0)
        results = parse(html)

        for result in results:
            print(result)
            sava(result)
        end_time = time.time()
        all_time = end_time - start_time
        print(f'爬取{page}页，总耗时{all_time}')


if __name__ == '__main__':
    main()

    # create_table.mysql_select()
