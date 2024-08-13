import aiohttp
import asyncio
import time
import datetime
import logging
from concurrent.futures import ThreadPoolExecutor
import warnings

logging.basicConfig(level=logging.INFO)

warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=RuntimeWarning)

class CouponGrabber:
    def __init__(self, cookie, idtime, password):
        self.cookie = cookie
        self.idtime = idtime
        self.password = password
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090b19)XWEB/11177',
            'CSESSION': self.cookie,
            'Host': 'marketing.shuxinyc.com',
            'Referer': 'https://marketing.shuxinyc.com/marketing/minip/activity/join/password/',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }
        self.url = 'https://marketing.shuxinyc.com/marketing/minip/activity/join/password/'
        self.json_data = {
            'id': '',
            'businessId': self.idtime,
            'activetype': 4,
            'password': self.password,
            'activityJoinSource': 1,
            'shopId': -1,
        }

    async def post(self, session):
        now = datetime.datetime.now().strftime("%H:%M:%S.%f")
        try:
            async with session.post(self.url, json=self.json_data, ssl=False, timeout=2) as response:

                if response.status == 200:
                    text = await response.text()
                    if "success" in text.lower():
                        logging.info(f"✅[{now}] {self.cookie[:10]}... 抢券成功: {text}")
                        return True
                    else:
                        logging.info(f"❌[{now}] {self.cookie[:10]}... 未抢到: {text}")
                else:
                    logging.warning(f"❗[{now}] {self.cookie[:10]}... 状态码: {response.status}")
        except Exception as e:
            logging.error(f"❗[{now}] {self.cookie[:10]}... 错误: {str(e)}")
        return False

async def run_grabber(grabber):
    connector = aiohttp.TCPConnector(limit=0, ttl_dns_cache=300)
    async with aiohttp.ClientSession(headers=grabber.headers, connector=connector) as session:
        tasks = [grabber.post(session) for _ in range(1000)]  # 创建1000个并发任务
        await asyncio.sleep(0.01)
        results = await asyncio.gather(*tasks)
        if any(results):
            return True
    return False

async def main():
    accounts = [
        {"cookie": "1722999164|SZFwsDRFhdG7FluC.I8v0QVbvYYprJIa34ODlru6jyRTkd5qDYuZPzXv7sEmw9m3mdIhERCkdb+sUsjbqnauB3yUjQPi+MjsqY/ElAA==.d763bf9a20743b11", "idtime": idtime, "password": password},
        {"cookie": "1722999078|MNvDUcvzWXBeFZVN.yOs4W/OehxU7a/P7XFTL6UpmhkLcaaIDt2IKu4uYY3SlfeZo6XIzsnKKUY1i7cdcaC/P6c1NybD+oO/xqZBqiw==.3b2f016b24e78a96", "idtime": idtime, "password": password},
    ]

    grabbers = [CouponGrabber(**account) for account in accounts]

    while True:
        tasks = [run_grabber(grabber) for grabber in grabbers]
        results = await asyncio.gather(*tasks)
        if all(results):
            break
        await asyncio.sleep(0.01)

if __name__ == "__main__":
    idtime = "N8DRtsLWDPz4"
    password= "A"
    asyncio.run(main())