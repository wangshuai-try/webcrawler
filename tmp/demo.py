# Coding: utf-8
# Author: Wang Shuai
# Author_Email: wangshuai@ximalayaos.com
# Time: 2020/7/26 0026 20:19
# File: demo.py
# Project_Name: webCrawler
# Content: 爬取微博信息

import requests
from lxml import etree
from urllib.parse import urlencode
import csv

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
}
base_url = 'https://m.weibo.cn/api/container/getIndex?'

def get_page(page):
    params = {
        'type': "uid",
        'value': '283067847',
        'containerid': '1076032830678474',
        'page': page
    }
    url = base_url + urlencode(params)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            # print(response.json())
            # print(type(response.json()))
            return response.json(), page
    except requests.ConnectionError as e:
        print('Error', e.args)

def parse_page(json, page: int):
    if json:
        items = json.get('data').get('cards')
        for index, item in enumerate(items):
            if page == 1 and index == 1:
                continue
            else:
                item = item.get('mblog', {})
                weibo = {}
                weibo['id'] = item.get('id')
                weibo['text'] = item.get('text')
                weibo['attitudes'] = item.get('attitudes_count')
                weibo['comments'] = item.get('comments_count')
                weibo['reposts'] = item.get('reposts_count')
                yield weibo

def save_csv(results):
    with open('weibo.csv', 'a', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['id', 'text', 'attitudes', 'comments', 'reposts'])
        writer.writeheader()
        for result in results:
            writer.writerow(result)
    print('写入完成！！！')

if __name__ == '__main__':
    for page in range(1, 11):
        json = get_page(page)
        results = parse_page(*json)
        save_csv(results)




