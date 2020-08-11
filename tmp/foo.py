from urllib.request import HTTPHandler, build_opener
from collections import namedtuple


# 有命名的元组类
Response = namedtuple(
    'Response',
    field_names=['headers', 'encoding', 'code', 'text', 'body']
)


def get(url):
    opener = build_opener(HTTPHandler())
    resp = opener.open(url)
    """
    返回某个类对象，其属性包含
    headers-> dict,
    code-> int,
    text-> 文本,
    body-> 字节码等相关属性
    """

    headers = dict(resp.getheaders())
    try:
        encoding = headers['Content-Type'].split('=')[-1]
    except:
        encoding = 'utf-8'
    code = resp.code
    body = resp.read()
    text = body.decode(encoding)

    return Response(headers=headers,
                    encoding=encoding,
                    code=code,
                    body=body,
                    text=text)

if __name__ == '__main__':
    resp: Response = get('http://www.baidu.com')
    print(resp)





