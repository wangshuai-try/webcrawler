import random
from pprint import pp

cookie_txts = [
    'login=flase; ASP.NET_SessionId=f42tzgz154szgehhbl1utyzc;'
    ' Hm_lvt_9007fab6814e892d3020a64454da5a55=1599321338,1599326912;'
    ' codeyzgswso=e58c462d048a533f; gsw2017user=1247631%7c34EE4A20E6A2112E7589439AEAA6080B;'
    ' login=flase; gswZhanghao=15526125070; gswPhone=15526125070; Hm_lpvt_9007fab6814e892d3020a64454da5a55=1599327262'
]


def get_cookie():
    cookie = random.choice(cookie_txts)

    return {(items := c.split('='))[0].strip(): items[1].strip() for c in cookie.split(';')}


if __name__ == '__main__':
    pp(get_cookie())
