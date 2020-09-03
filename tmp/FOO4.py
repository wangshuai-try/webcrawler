# Coding: utf-8
# Author: Wang Shuai
# Author_Email: wangshuai@ximalayaos.com
# Time: 2020/8/23 0023 21:48
# File: FOO4.py
# Project_Name: webCrawler
# Content:
import requests
import re
from lxml import etree
from urllib.request import urlretrieve


# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
#                   ' Chrome/84.0.4147.89 Safari/537.36'
# }
# url = 'https://book.qidian.com/info/1011449273'
# url1 = 'https://book.qidian.com/ajax/book/category?_csrfToken=23OtBIDKLSx52X27bjoVWm5AGtFeIM0OEUm72SJx&bookId=1010868264'
# resp = requests.get(url1, headers=headers)
# resp.encoding = 'gzip'
# # print(resp.url, type(resp.text))
# tree = etree.HTML(resp.text)
# a = tree.xpath('//div[@class="volume-wrap"]/div/ul/li')
# # print(a)
# # print(resp.text)
# book_url = re.findall('"cU":"(.*?)"', resp.text)
# # print(book_url)
#
# for i in book_url:
#     book_urls = 'https://read.qidian.com/chapter/' + i
#     # res = requests.get(book_urls)
#     print(urlretrieve(book_urls, 'xiao.txt'))
#     # with open('xiaoshuo.txt', 'a', encoding='utf-8') as f:
#     #     f.write(urlretrieve(book_urls))
aaa
urlretrieve('https://read.qidian.com/chapter/3Q__bQt6cZEVDwQbBL_r1g2/GSlTBhSdiqP4p8iEw--PPw2', 'xiaoshuo.txt')