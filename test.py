import asyncio
import aiohttp
import time
import sys

try:
    from aiohttp import ClientError
except:
    from aiohttp import ClientProxyConnectionError as ProxyConnectionError
import requests as rq


async def a():
    conn = aiohttp.TCPConnector(verify_ssl=False)
    async with aiohttp.ClientSession(connector=conn) as sess:
        async with sess.get('https://www.baidu.com', proxy="http://" + proxy) as res:
            print(res.status)
            print(res)
if __name__ == '__main__':
    proxy = str(rq.get("http://10.102.6.216:5010/get/").content, encoding="utf-8")
    proxys = {
        'http': 'http://' + '115.159.31.195',
        'https': 'https://' + '8060'
    }
    print(proxys)
    res = rq.get('http://www.ctrip.com',proxies=proxys)
    print(res.text)

    # proxy="http://111.77.22.237:9000"
    #
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(asyncio.wait([a(),a()]))
