# Coding: utf-8
# Author: Wang Shuai
# Author_Email: wangshuai@ximalayaos.com
# Time: 2020/7/28 0028 23:47
# File: meizi.py
# Project_Name: webCrawler
# Content:


import requests
import os
from lxml import etree
from urllib.parse import urlencode
import json
import urllib.request
import socket





headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
        }


def get_page(self, page):
    """
    获取页面的所有图片地址
    :param url: 页面地址
    :return:
    """
    url = 'https://www.meizitu.com/a/list_1_{}.html'.format(page)
    response = requests.get(url=url, headers=self.headers)
    try:
        if response.status_code == 200:
            response.encoding = 'gb2312'
            return response.text
    except requests.ConnectionError as e:
        return None

def get_base_images(self, html):
    etree1 = etree.HTML(html)
    # 获取每页每个图册的url
    base_urls = etree1.xpath('//*[@id="maincontent"]/div/ul/li/div/div/a')
    list_urls = [base_url.attrib['href'] for base_url in base_urls]
    # 获取每页每个图册的title
    base_titles = etree1.xpath('//*[@id="maincontent"]/div/ul/li/div/div/a/img')
    self.list_titles = [base_title.attrib['alt'] for base_title in base_titles]
    return dict(zip(self.list_titles, list_urls))

def get_images(self, html):
    """
    获取每个图册详细的图片title、url
    :param html: 每页每个图册的title、url字典
    :return: 每个图片的title、url
    """
    n = 0
    list_titles = []
    list_urls = []
    for title, url in html.items():

        try:
            response = requests.get(url, headers=self.headers)
            if response.status_code == 200:
                response.encoding = 'gb2312'
                tree = etree.HTML(response.text)
                images = tree.xpath('//*[@id="picture"]/p/img')
                list_title = [image.attrib['alt'] for image in images]
                list_url = [image.attrib['src'] for image in images]

                title = title.replace('<b>', '')
                title = title.replace('</b>', '')
                yield [title, dict(zip(list_title, list_url))]
        except ConnectionError as e:
            return None

# a:已下载的数据块 b:数据块的大小 c:远程文件的大小
def schedule(a, b, c):
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
    print('%.2f%%' % per)

def save_images(self, images):
    """

    :param images:
    :return:
    """

    for image in images:
        for title, url in image[1].items():
            response = requests.get(url)
            if response.status_code == 200:
                file_path = r'F:\test\webCrawler\meizi\{}'.format(image[0])
                if not os.path.exists(file_path):
                    os.mkdir(file_path)
                try:
                    urllib.request.urlretrieve(url, file_path + r'\{}.jpg'.format(title))
                except socket.timeout:
                    count = 1
                    while count <= 5:
                        try:
                            urllib.request.urlretrieve(url, file_path + r'\{}.jpg'.format(title))
                            break
                        except socket.timeout:
                            err_info = 'Reloading for %d time' % count if count == 1 else 'Reloading for %d times' % count
                            print(err_info)
                            count += 1
                    if count > 5:
                        print("downloading picture fialed!")


def main(page):

    html = get_page(page)
    data = get_base_images(html)
    images = get_images(data)
    m.save_images(images)

if __name__ == '__main__':
    for i in range(1, 11):
        main(i)

