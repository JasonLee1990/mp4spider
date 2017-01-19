# -*- coding: utf-8 -*-
__author__ = 'yutiansut'
import scrapy
from scrapy.spider import Spider  
from scrapy.http import Request  
from scrapy.selector import Selector  
from Spider.items import SpiderItem

class SihuSpider(scrapy.Spider):
   # download_delay = 1  
    name = "sihu"
    allowed_domains = ["www.27sihu.com"]
    start_urls = ['https://www.27sihu.com/']
    items = []
    def parse(self, response):
        sel = Selector(response)  
        item=SpiderItem();
        html=response.xpath('//a/@href').extract()
        
        
       
        for h in html:
            if h.endswith('mp4'):
              #  print '``````````````get MP4``````````````````'
                print h
                item['mp4']=h;
                yield item
                yield SpiderItem
            else:
                url='https://www.27sihu.com'+h
               # print url
                item['html']=url;
                yield Request(url, callback=self.parse)
        #    print h
        




