# -*- coding: utf-8 -*-
from multiprocessing import Process
from scrapy import cmdline
import time
import logging
import datetime

# 配置参数即可, 爬虫名称，运行频率
confs = [
    {
        "spider_name": "ctripspy",
        "frequency": 120,
    },
]


def start_spider(spider_name, frequency):
    args = ["scrapy", "crawl", spider_name]
    while True:
        time1 = datetime.datetime.now().strftime("%Y%m%d")
        time2 = datetime.datetime.now().strftime("%H")
        time3 = datetime.datetime.now().strftime("%M")
        args += ["-o", f"/root/data/{time1}/{time2}/{time3}.csv", "-t", "csv"]
        start = time.time()
        p = Process(target=cmdline.execute, args=(args,))
        p.start()
        p.join()
        logging.debug("### use time: %s" % (time.time() - start))
        time.sleep(frequency)


if __name__ == '__main__':
    time.sleep(20)
    for conf in confs:
        process = Process(target=start_spider,
                          args=(conf["spider_name"], conf["frequency"]))
        process.start()
        time.sleep(10)
