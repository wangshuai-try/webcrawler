# Coding: utf-8
# Author: Wang Shuai
# Author_Email: wangshuai@ximalayaos.com
# Time: 2020/7/30 0030 21:30
# File: toutiao_meitu.py
# Project_Name: webCrawler
# Content:

import requests
from urllib.parse import urlencode

def get_page(offset):
    params = {
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'cur_tab': '1'
    }
    url = 'http:www.toutiao.com/search_content/?' + urlencode(params)
    print(url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        return None


if __name__ == '__main__':
    page = get_page(0)
    print(page)