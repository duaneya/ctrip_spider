# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from ctrip.items import CtripItem
import datetime
from scrapy import Spider
from urllib.parse import quote
from scrapy_splash import SplashRequest
import requests as rq

script = """
function main(splash, args)
  --splash:on_request(function(request)
  --  request:set_proxy{
  --      host = args.ip,
  --      port = args.port,
  --  }
  --end)
  splash:set_user_agent("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36")
  splash.images_enabled = false
  assert(splash:go(args.url))
  local ok, reason = splash:wait(5)
  if ok then
    splash:set_viewport_full()
    elements_before = splash:select_all('.btn_book.arrow_down')
    while(true)
    do
      splash:evaljs("var q=document.documentElement.scrollTop=100000")
      elements_now = splash:select_all('.btn_book.arrow_down')
      if #elements_now == #elements_before then
        break
      end
      elements_before = elements_now
    end
    for _, ele in ipairs(elements_now) do
      ele:mouse_click()
    end
    elements = splash:select_all('a.arrow_down[data-ubt="c_cabin_book_open"]')
    --elements[2]:mouse_click()
    for _, ele in ipairs(elements) do
      pcall(function() ele:mouse_click() end)
    end
    return {
    html = splash:html()
  }
  end
end
"""



def get_urls():
    city = ['tao', 'sha', 'bjs', 'can', 'wuh']
    urls = []
    for depart in city:
        for destination in city:
            if depart == destination:
                continue
            else:
                today = datetime.date.today()
                for i in range(8):
                    flight_time = str(today + datetime.timedelta(days=i))
                    flight_time_url = flight_time[:4] + '-' + flight_time[5:7] + '-' + flight_time[8:10]
                    url = "https://flights.ctrip.com/itinerary/oneway/" + depart + "-" + destination + "?date=" + flight_time_url
                    urls.append(url)

    return urls


class CtripspySpider(scrapy.Spider):
    name = 'ctripspy'
    allowed_domains = ['ctrip.com']

    # start_urls = ['https://flights.ctrip.com/itinerary/oneway/bjs-sha?date=2019-04-19']

    # start_urls = get_urls()
    def start_requests(self):
        urls = get_urls()
        for url in urls:
            yield SplashRequest(url, callback=self.parse, endpoint='execute',
                                args={'lua_source': script})

    def parse(self, response):
        flights = response.xpath(
            '//div[@class="search_box search_box_tag search_box_light search_box_spread Label_Flight"]')
        # print(response.xpath('//button'))
        # flights = response.xpath(
        #     '//div[@class="search_box search_box_tag search_box_light Label_Flight"]')
        for flight in flights:
            dls = flight.xpath(
                './div[@class="search_table search_table-list"]/div[contains(@class,"search_table_inner search-table-inner")]')
            for dl in dls:
                flight_header = flight.xpath('./div[@class="search_table_header"]')
                l = ItemLoader(item=CtripItem(), response=response)
                # from scrapy.shell import inspect_response
                # inspect_response(response, self)
                l.add_value('company', flight_header.xpath(
                    './div[@class="inb logo"]//div[@data-ubt-hover="c_flight_aircraftInfo"]')[0].xpath(
                    './/strong//text()').extract())  #
                l.add_value('flight_number', flight_header.xpath(
                    './div[@class="inb logo"]//div[@data-ubt-hover="c_flight_aircraftInfo"]')[0].xpath(
                    './span/span/span//text()').extract())  #
                l.add_value('aircraft_model', flight_header.xpath(
                    './div[@class="inb logo"]//div[@data-ubt-hover="c_flight_aircraftInfo"]')[1].xpath(
                    './/text()').extract())
                l.add_value('flight_time_away', flight_header.xpath(
                    './div[@class="inb right"]//strong[@class="time"]//text()').extract())  #
                l.add_value('flight_airport_away',
                            flight_header.xpath(
                                './div[@class="inb right"]//div[@class="airport"]//text()').extract())
                l.add_value('flight_time_arrive', flight_header.xpath(
                    './div[@class="inb left"]//strong[@class="time"]//text()').extract())  #
                l.add_value('flight_airport_arrive',
                            flight_header.xpath(
                                './div[@class="inb left"]//div[@class="airport"]//text()').extract())
                l.add_value('on_time_rate', flight_header.xpath(
                    './/div[@class="service-item"]/div[@class="clearfix"]//text()').extract())
                l.add_value('refund_fee',
                            dl.xpath('.//div[contains(@class,"inb after_sales")]//text()').extract())
                l.add_value('discount',
                            ''.join(dl.xpath('.//div[contains(@class,"inb discount")]//text()').extract()).replace(' ',
                                                                                                                   '').replace(
                                ',', ''))
                l.add_value('price', ''.join(dl.xpath(
                    './/div[contains(@class,"inb flt_price")]/span[@class="base_price02"]//text()').extract()).replace(
                    ',', '').replace(' ', ''))  #
                l.add_value('status', dl.xpath('.//div[contains(@class,"inb last_item")]//text()').extract())
                l.add_value('version', '0.2')
                l.add_value('url', response.url)
                # l.add_value('project', self.settings.get('BOT_NAME'))
                l.add_value('spider', self.name)
                # l.add_value('server', socket.gethostname())
                now = datetime.datetime.now()
                l.add_value('date', now.strftime("%Y%m%d%H%M%S"))
                l.add_value('date_timestamp', now.timestamp())
                yield l.load_item()
