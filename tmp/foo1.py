# Coding: utf-8
# Author: Wang Shuai
# Author_Email: wangshuai@ximalayaos.com
# Time: 2020/8/9 0009 0:01
# File: foo1.py
# Project_Name: webCrawler
# Content:
from collections import namedtuple
import requests

Response = namedtuple('Response', field_names=['name', 'age', 'sex'])


def printa():
    name = '王帅'
    age = 18
    sex = 'man'

    return Response(name=name,
                    age=age,
                    sex=sex)


class A():
    def __init__(self)-> int:
        self.name = 'wangshuai1'


    def a(self) -> str:
        name = 'wangshuai'
        age = 18
        return name, age


if __name__ == '__main__':
    # res: Response = printa()
    # print(res._replace(age=17))
    # print(type(res._asdict()))
    # print(res)
    # dict1 = res._asdict()
    # print(dict1['sex'])
    # print(res.name)
    # print('难受  我想放弃了')
    a: A = A()
    print(type(a.name), a.name)
    print(type(a.a()), a.a())
