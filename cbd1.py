import asyncio
import aiohttp
import time
import datetime
from concurrent.futures import ThreadPoolExecutor
import warnings

# 忽略 ResourceWarning
warnings.simplefilter("ignore", ResourceWarning)


class CouponGrabber:
    def __init__(self, name, cookie, idtime, password):
        self.name = name
        self.cookie = cookie
        self.idtime = idtime
        self.password = password
        self.session = None
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090b19)XWEB/11177',
            'CSESSION': self.cookie,
            'Host': 'marketing.shuxinyc.com',
            'Referer': 'https://marketing.shuxinyc.com/marketing/minip/activity/join/password/',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }
        self.url = 'https://marketing.shuxinyc.com/marketing/minip/activity/join/password/'

    async def create_session(self):
        self.session = aiohttp.ClientSession(headers=self.headers)

    async def close_session(self):
        if self.session:
            await self.session.close()

    async def post(self):
        if not self.session:
            await self.create_session()

        try:
            now = datetime.datetime.now()
            ip3 = now.strftime("%H:%M:%S.%f")
            json_data = {
                'id': '',
                'businessId': self.idtime,
                'activetype': 4,
                'password': self.password,
                'activityJoinSource': 1,
                'shopId': -1,
            }

            async with self.session.post(self.url, json=json_data, ssl=False, timeout=2) as response:
                if response.status == 200:
                    text = await response.text()
                    print(f"✅[{ip3}]{self.name}----{text}")
                else:
                    print(f"❌[{ip3}]{self.name}----{response.status}")
        except Exception as e:
            print(f"❌[{ip3}]{self.name}----Error: {str(e)}")


async def run_grabber(grabber, num_requests):
    await grabber.create_session()
    tasks = [grabber.post() for _ in range(num_requests)]
    await asyncio.gather(*tasks)
    await grabber.close_session()


def run_in_thread(grabber, num_requests):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(run_grabber(grabber, num_requests))
    loop.close()


def main():
    # 假设我们有多个账号
    grabbers = [
        CouponGrabber("Account1", "1722999164|SZFwsDRFhdG7FluC.I8v0QVbvYYprJIa34ODlru6jyRTkd5qDYuZPzXv7sEmw9m3mdIhERCkdb+sUsjbqnauB3yUjQPi+MjsqY/ElAA==.d763bf9a20743b11", idtime, password),
        CouponGrabber("Account2", "1722999078|MNvDUcvzWXBeFZVN.yOs4W/OehxU7a/P7XFTL6UpmhkLcaaIDt2IKu4uYY3SlfeZo6XIzsnKKUY1i7cdcaC/P6c1NybD+oO/xqZBqiw==.3b2f016b24e78a96", idtime, password),
        # ... 添加更多账号
    ]

    num_requests_per_second = 20
    duration_seconds = 5  # 运行5秒钟作为示例

    with ThreadPoolExecutor(max_workers=len(grabbers)) as executor:
        start_time = time.time()
        while time.time() - start_time < duration_seconds:
            futures = [executor.submit(run_in_thread, grabber, num_requests_per_second) for grabber in grabbers]
            for future in futures:
                future.result()
            time.sleep(max(0, 1 - (time.time() - start_time) % 1))  # 确保每秒只运行一次


if __name__ == "__main__":
    idtime = "N8DRtsLWDPz4"

    password= "A"

    main()