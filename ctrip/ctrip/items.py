# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CtripItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    company = scrapy.Field()  # 公司
    flight_number = scrapy.Field()  # 航班号
    aircraft_model = scrapy.Field()  # 型号
    flight_time_away = scrapy.Field()  # 起飞时间
    flight_airport_away = scrapy.Field()  # 起飞机场
    flight_time_arrive = scrapy.Field()  # 起飞时间
    flight_airport_arrive = scrapy.Field()  # 起飞机场
    on_time_rate = scrapy.Field()  # 准点率
    # passtime = scrapy.Field()
    price = scrapy.Field()  # 价格
    refund_fee = scrapy.Field()  # 退改信息
    discount = scrapy.Field()  # 折扣
    status = scrapy.Field()  # 余票状态
    flight_type = scrapy.Field()  # 直飞或转动车
    flight_transfer = scrapy.Field()  # 中转信息

    version = scrapy.Field()  # 数据版本
    url = scrapy.Field()
    # project = scrapy.Field()
    spider = scrapy.Field()
    # server = scrapy.Field()
    date = scrapy.Field()

    date_timestamp = scrapy.Field()
