# -*- coding: utf-8 -*-
import scrapy

from scrapy_splash import SplashRequest
import requests as rq
script = """
function main(splash, args)
  splash:set_user_agent("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36")
  splash.images_enabled = false
  assert(splash:go(args.url))
  local ok, reason = splash:wait(3)
  if ok then
    return {
    html = splash:html()
  }
  end
end
"""

def get_proxy():
    ip_port = str(rq.get("http://127.0.0.1:8050/get/").content, encoding="utf-8")
    return ip_port


class TestproxySpider(scrapy.Spider):
    name = 'testproxy'
    allowed_domains = ['httpbin.org']

    # start_urls = ['http://httpbin.org/get']
    def start_requests(self):
        # url = 'https://flights.ctrip.com/itinerary/oneway/tao-bjs?date=2019-04-18'
        for i in range(3):
            url = 'http://httpbin.org/get'
            yield SplashRequest(url=url, endpoint='execute',callback=self.parse, args={'lua_source':script})

    def parse(self, response):
        print("fsdfs")
        print(''.join(response.xpath('//*//text()').extract()))
