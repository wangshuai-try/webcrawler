# Coding: utf-8
# Author: Wang Shuai
# Author_Email: wangshuai@ximalayaos.com
# Time: 2020/8/8 0008 20:50
# File: fanyi.py
# Project_Name: webCrawler
# Content:

from urllib.request import Request, urlopen
from urllib.parse import urlencode
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://www.baidu.com/s?'

headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Cookie': 'BAIDUID=FCAEC6AAC0586EFB23A35B04BD9A5309:FG=1; BIDUPSID=FCAEC6AAC0586EFB23A35B04BD9A5309; PSTM=1569507337; __cfduid=daa0a69fe6b29bcfedabcc7a105da42c11571561009; BD_UPN=12314753; BDUSS=y1KVzhHUW9DeGwxS212WmlGS1RTMXl0Q0JRNHR-SkpwOFBwOVV-Unk5UFN3cUZlRVFBQUFBJCQAAAAAAAAAAAEAAAD1Y5nFd3NmZzYwMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANI1el7SNXpeZ; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDUSS_BFESS=y1KVzhHUW9DeGwxS212WmlGS1RTMXl0Q0JRNHR-SkpwOFBwOVV-Unk5UFN3cUZlRVFBQUFBJCQAAAAAAAAAAAEAAAD1Y5nFd3NmZzYwMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANI1el7SNXpeZ; delPer=0; PSINO=6; BD_HOME=1; BD_CK_SAM=1; BDRCVFR[feWj1Vr5u3D]=mk3SLVN4HKm; COOKIE_SESSION=81_0_4_4_7_6_0_1_4_2_10_2_890_0_0_0_1596812884_0_1596894550%7C9%23386_13_1596385123%7C7; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; __yjsv5_shitong=1.0_7_bbeec20817ba9178e7c75208345c8f344fa7_300_1596895174736_112.97.48.79_31ac8e36; yjs_js_security_passport=4897da11b52474e23a3b0d332545dc8e12b656d7_1596895175_js; H_PS_PSSID=32294_1468_32438_32355_31254_32352_32046_32393_32117_26350_32505_32482; sugstore=1; H_PS_645EC=cd5bU1XEbYRop%2B72LkTamComqfujequ%2BZvkZgjewb5LUWYBEsu84acHM6Fc'
        }



def paras(pages, wd):

    for page in range(pages):
        params = {
            'wd': wd,
            'pn': page
        }
        params['wd'] = wd
        params['pn'] = page*10


        page_url = url + urlencode(params)
        print(page_url)
        res = Request(page_url, headers=headers)
        resp = urlopen(res)
        assert resp.code == 200
        file_name = f'F:\\test\webCrawler\\tmp\\{wd}——{page+1}'

        with open(file_name + '.html', 'wb') as f:
            f.write(resp.read())
            print(file_name.split('\\')[-1]+ '写入成功')



if __name__ == '__main__':
    paras(100, '妹子图')