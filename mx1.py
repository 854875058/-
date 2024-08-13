import time
import hashlib
import json
import asyncio
import aiohttp
from datetime import datetime, timedelta
from functools import partial
import subprocess
from fake_useragent import UserAgent
import requests
subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
import execjs

# 获取当前时间
hour = datetime.now().hour + (datetime.now().minute >= 15)
# 定时功能设置
target_time_tuple = (hour -1 , 9, 59,500)  # 小时, 分钟, 秒, 毫秒

# 定义文件路径
token_file_path = 'test.txt'
completed_file_path = 'completed_tokens.txt'
invalid_token_file_path = 'invalid_tokens.txt'
# 口令
kouling = "茉莉奶绿 白月光"

# 代理 API 的 URL
#PROXY_API_URL = "http://sd.jghttp.alicloudecs.com/get_ip?num=200&type=1&pro=&city=0&yys=0&port=1&time=6&ts=0&ys=0&cs=0&lb=1&sb=0&pb=5&mr=2&regions="
PROXY_API_URL = "http://d.jghttp.alicloudecs.com/getip?num=500&type=1&pro=&city=0&yys=0&port=1&time=6&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=2&regions="#极光
#PROXY_API_URL="http://webapi.http.zhimacangku.com/getip?neek=321a408a&num=100&type=1&time=4&pro=0&city=0&yys=0&port=1&pack=0&ts=0&ys=0&cs=0&lb=1&sb=&pb=45&mr=2&regions=&cf=0&username=chukou01&spec=1"

# 抢券场次
round_time = f"{hour}:00"

# 抢券延迟
delay_ms = 300

# 抢券次数
cishu = 10

# 循环判断时间间隔
delay_time = 0.01

# 用户设置的线程数(每个账号的线程数)
num_threads_per_account = 1

# 最大重试次数
max_retries = 1

# 是否使用代理
use_proxy = True

# 提前获取代理的时间
get_proxy_seconds_early = 15

# 每个账号的代理数
num_proxies_per_account = max_retries * cishu * num_threads_per_account *2 + 1

# API 请求的 URL
url = "https://mxsa.mxbc.net/api/v1/h5/marketing/secretword/confirm"

# 固定的请求头信息
type__1286 = "muiQ0KAKDvkbDsD7GP0=DO0GOzMucDD=a4D"
REFERER = "https://mxsa-h5.mxbc.net/"
ACCEPT_LANGUAGE = "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"

# 固定的值，用于生成签名
FIXED_VALUE = "c274bac6493544b89d9c4f9d8d542b84"
with open('mx1.js', 'r', encoding='utf-8') as file:
    js_code = file.read()
# 编译JavaScript代码
context = execjs.compile(js_code)
# 调用JavaScript函数
def get_server_time():
    url = "https://mxsa.mxbc.net/api/v1/h5/marketing/secretword/info"
    params = {
        "marketingId": "1816854086004391938",
        "sign": "1e2d49af043b93703987a88a278ce456",
        "s": 2,
        "stamp": 1722600859101
    }
    response = requests.get(url, params=params)
    data = response.json()
    server_time_str = data['data']['serverTime']
    # 将服务器返回的时间字符串转换为datetime对象
    server_time = datetime.strptime(server_time_str, "%Y-%m-%d %H:%M:%S")
    # 转换为毫秒级的时间戳
    server_time_ms = int(server_time.timestamp() * 1000)
    return server_time_ms

def get_time_avgdiff():
    time_diff_sum = 0
    yanchi_num = 0
    num = 20
    for i in range(num):
        local_time1 = int(time.time() * 1000)
        server_time = get_server_time()
        local_time2 = int(time.time() * 1000)
        yanchi = (local_time2 - local_time1) /2
        time_diff = local_time1 + yanchi - server_time
        time_diff_sum += time_diff
        yanchi_num += yanchi
        print(f"第{i+1}次请求，当前系统时间与蜜雪服务器时间差为{time_diff}毫秒,网络延迟为{yanchi}毫秒")
    print(f"当前系统时间比蜜雪服务器平均快 {time_diff_sum / num} 毫秒,网络延迟平均为{yanchi_num /num}毫秒")
    return time_diff_sum / num, yanchi_num /num
def get_token_file(file_path):
    accounts = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            parts = line.split('----')
            if len(parts) == 2:
                remark, token = parts
                accounts[remark] = token.strip()
    return accounts

def save_token_file(file_path, remark, token):
    # 尝试读取文件，检查数据是否存在
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split('----')
                if len(parts) == 2:
                    existing_remark, existing_token = parts
                    if existing_remark == remark and existing_token == token:
                        return  # 数据已存在，直接返回
                else:
                    print(f"Warning: Line '{line}' in file '{file_path}' has an incorrect format.")
    except FileNotFoundError:  # 文件可能不存在
        pass  # 如果文件不存在，就继续执行写入操作
    # 如果数据不存在，则写入文件
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(f"{remark}----{token}\n")

accounts = get_token_file(token_file_path)
print(f"所有token: {accounts}")

completed_tokens = get_token_file(completed_file_path)
print(f"已完成抢券token: {completed_tokens}")

invalid_tokens = get_token_file(invalid_token_file_path)
print(f"失效的token: {invalid_tokens}")

filtered_accounts = {remark: token for remark, token in accounts.items() if remark not in completed_tokens and remark not in invalid_tokens}
print(f"过滤后的token总共有{len(filtered_accounts)} 个有效账号")
for remark, token in filtered_accounts.items():
    print(f"备注: {remark}, token: {token}")

# 抢到免单券的账号及数量
successful_remarks = []
def get_current_timestamp():
    return int(time.time() * 1000)

def create_payload(marketingId, round_time, secretword, s):
    timestamp = get_current_timestamp()
    hash_string = f"marketingId={marketingId}&round={round_time}&s={s}&secretword={secretword}&stamp={timestamp}{FIXED_VALUE}"
    sign = hashlib.md5(hash_string.encode('utf-8')).hexdigest()
    return {
        "marketingId": marketingId,
        "round": round_time,
        "secretword": secretword,
        "sign": sign,
        "s": s,
        "stamp": timestamp
    }

proxy_cache = {}
used_proxies = set()
ua = UserAgent()

def get_proxies(num_proxies):
    all_proxies = []
    proxies_needed = num_proxies

    while len(all_proxies) < proxies_needed:
        response = requests.get(PROXY_API_URL)
        if response.status_code == 200:
            if "请2秒后再试" in response.text:
                time.sleep(2)
                continue
            else:
                proxy_data = response.text.strip()
                new_proxies = proxy_data.split('\r\n')
                all_proxies.extend([{"http": f"http://{proxy}", "https": f"http://{proxy}"} for proxy in new_proxies if proxy not in used_proxies])
                used_proxies.update(new_proxies)
        else:
            print(f"获取代理失败: {response.status_code}, {response.text}")
        if len(all_proxies) >= proxies_needed:
            break

    return all_proxies[:proxies_needed]

def get_proxies_for_accounts(num_proxies_per_account):
    global proxy_cache, used_proxies
    total_proxies_needed = num_proxies_per_account * len(filtered_accounts)
    all_proxies = get_proxies(total_proxies_needed)

    proxy_cache = {remark: [] for remark in filtered_accounts}  # 使用 remark 作为键
    proxy_index = 0
    for remark in filtered_accounts:
        proxy_cache[remark] = all_proxies[proxy_index:proxy_index + num_proxies_per_account]
        proxy_index += num_proxies_per_account

    print(f"提前获取代理: {proxy_cache}")

account_status = {token: False for token in filtered_accounts}
stop_all = False
start_time = None

async def get_proxies_async(num_proxies):
    return await asyncio.to_thread(get_proxies, num_proxies)

async def send_request(session, marketingId, round_time, secretword, s, remark, token):
    global stop_all, proxy_cache, account_status, successful_remarks, start_time

    if account_status[remark] or stop_all:
        print(f"账号 {remark} 已经抢到券或全局停止标志已设置，停止请求")
        return

    payload = create_payload(marketingId, round_time, secretword, s)
    type__1286 = context.call("zz", json.dumps(payload))
    headers = {
        "User-Agent": ua.random,
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json;charset=UTF-8",
        "Referer": REFERER,
        "Accept-Language": ACCEPT_LANGUAGE,
        "Access-Token": token
    }

    for attempt in range(max_retries):
        proxy = None
        proxy_info = "无代理"

        try:
            if use_proxy:
                if not proxy_cache[remark]:
                    proxy_cache[remark] = await get_proxies_async(num_proxies_per_account)
                if proxy_cache[remark]:
                    proxy = proxy_cache[remark].pop(0)  # 直接弹出并使用第一个代理
                    proxy_info = proxy["http"]
            conn = aiohttp.TCPConnector(ssl=False)
            async with aiohttp.ClientSession(connector=conn) as session:
                # 发送请求时间
                post_time=datetime.now()
                async with session.post(url, params=type__1286, data=json.dumps(payload), headers=headers,
                                        proxy=proxy["http"] if proxy else None,timeout=6) as response:
                    response_text = await response.text()
                try:
                    response_json = json.loads(response_text)

                    if response_json.get('code') == 0 or response_json.get('code') == 53161:
                        print(f"账号 {remark} {post_time} 抢到免单券，停止请求,当前代理IP: {proxy_info}")
                        account_status[remark] = True
                        successful_remarks.append(remark)
                        await save_token_file(completed_file_path, remark, token)
                        return
                    elif response_json.get('code') == 5310:
                        print(f"账号 {remark} {post_time} 检测到券包，停止所有请求,当前代理IP: {proxy_info}")
                        stop_all = True
                        return
                    elif response_json.get('code') == 401:
                        print(f"账号 {remark} {post_time} token失效: {token}")
                        account_status[remark] = True
                        await save_token_file(invalid_token_file_path, remark, token)
                        return
                    elif response_json.get('code') == 5308:
                        print(f"账号 {remark} {post_time} 场次未开始或已结束，当前代理IP: {proxy_info}")
                        return
                    elif response_json.get('code') in [429, 5304]:
                        await asyncio.sleep(0.1)
                        raise Exception(f"请求过多或操作频繁")
                    else:
                        raise Exception(f"请求失败: {response.status}, {response_text}")
                        await asyncio.sleep(0.1)
                except json.JSONDecodeError:
                    if response.status == 405 or "您的访问被阻断" in response_text:
                        raise Exception(f"您的访问被阻断")
                    else:
                        raise Exception(f"服务器返回了无效的JSON响应: {response_text}")
        except Exception as e:
            if attempt < max_retries:
                print(f"账号 {remark} {post_time} 请求异常: {e} 正在尝试更换代理，当前是第 {attempt + 1} 次尝试，当前代理IP: {proxy_info}")
                if use_proxy and proxy_cache[remark]:# 移除当前代理并获取新代理
                    proxy_cache[remark].pop(0)
                    if not proxy_cache[remark]:
                        proxy_cache[remark] = get_proxies(num_proxies_per_account)

        else:
            # 如果没有异常，跳出重试循环
            break
    if use_proxy and not proxy_cache[remark]:
        proxy_cache[remark] = await get_proxies_async(num_proxies_per_account)

async def execute_requests_for_account(session, remark, token, num_requests, delay_ms):
    global start_time
    tasks = []
    for _ in range(num_requests):
        if account_status[remark] or stop_all or (datetime.now() - start_time).total_seconds() > 10:
            break
        task = asyncio.create_task(send_request(session, "1816854086004391938", round_time, kouling, 2, remark, token))
        tasks.append(task)
        await asyncio.sleep(delay_ms / 1000)
    await asyncio.gather(*tasks)

async def execute_requests(num_requests, delay_ms, num_threads_per_account):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for remark, token in filtered_accounts.items():
            if stop_all:
                break
            for _ in range(num_threads_per_account):
                if stop_all:
                    break
                task = asyncio.create_task(execute_requests_for_account(session, remark, token, num_requests, delay_ms))
                tasks.append(task)
        await asyncio.gather(*tasks)


async def run_at_specific_time(target_time_tuple):
    global start_time
    hour, minute, second, millisecond = target_time_tuple
    now = datetime.now()
    target_time = now.replace(hour=hour, minute=minute, second=second, microsecond=millisecond * 1000)

    while True:
        current_time = datetime.now()
        if (target_time - current_time).total_seconds() <= get_proxy_seconds_early:
            if use_proxy:
                print("开始提前获取代理:", current_time)
                get_proxies_for_accounts(num_proxies_per_account)
            break
        delta = target_time - current_time
        milliseconds_until_target = delta.total_seconds() * 1000
        print(f"当前时间: {current_time}, 距离目标时间: {milliseconds_until_target:.0f} ms")
        await asyncio.sleep(delay_time * 300)

    print(f"{datetime.now()},提前获取代理结束,准备进行服务器时间校准")
    time_diff, yanchi = get_time_avgdiff()
    target_timestamp = int(target_time.timestamp() * 1000)

    while True:
        current_timestamp = int(time.time() * 1000)
        adjusted_timestamp = current_timestamp - int(time_diff) + int(yanchi)
        print(f"当前时间: {datetime.now()}, 调整后的时间戳: {adjusted_timestamp}, 目标时间戳: {target_timestamp}")
        if adjusted_timestamp >= target_timestamp:
            print("开始抢券时间:", datetime.now())
            start_time = datetime.now()  # 记录请求开始时间
            await execute_requests(cishu, delay_ms, num_threads_per_account)
            break
        await asyncio.sleep(delay_time)
print("当前时间：", datetime.now())
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(run_at_specific_time(target_time_tuple))
print(f"{datetime.now()}抢券结束，本次抢券成功的账号及数量: {len(successful_remarks)}")
for remark in successful_remarks:
    print(remark)