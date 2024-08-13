import hashlib
import time
from hashlib import md5 as md5Encode
import execjs
import requests
import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
token = ''
round = '11:00'
secretword = '茉莉奶绿 白月光'
stamp = int(time.time()*1000)
marketingId = '1816854086004391938'






headers = headers = {
    'Access-Token': token,
    'Origin': 'https://mxsa-h5.mxbc.net',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'no-cache',
    'dnt': '1',
    'pragma': 'no-cache',
    'sec-ch-ua': '"Chromium";v="118", "Microsoft Edge";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.46',
}


base_url = 'https://mxsa.mxbc.net/api/v1/h5/marketing/secretword/confirm'


def getMd5(md):
    md5 = hashlib.md5()
    md5.update(md.encode('utf-8'))
    return md5.hexdigest()
def get_type1286(url,time_):
    with open('mx.js', 'r', encoding='UTF-8') as f:
        js_code = f.read()
    context = execjs.compile(js_code)

    return context.call("get_sig", url,time_)



def run():
    sign = getMd5(f"marketingId={marketingId}&round={round}&s=2&secretword={secretword}&stamp={stamp}c274bac6493544b89d9c4f9d8d542b84")
    data = {
        "marketingId": marketingId,
        "round": round,
        "secretword": secretword,
        "sign": sign,
        "s": 2,
        "stamp": stamp
    }
    type1286 = get_type1286(base_url+'{"marketingId":"'+marketingId+'","round":"'+round+'","secretword":"'+secretword+'","sign":"'+sign+'","s":2,"stamp":'+str(stamp)+'}',str(stamp))
    return requests.post(base_url+"?type__1286="+type1286, headers=headers, json=data,impersonate="chrome110").text

print(run())



