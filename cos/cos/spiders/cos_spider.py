#!/usr/bin/env python
# encoding: utf-8

import re
import scrapy
import atomdb
import redis

from scrapy import log
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector

class CosSpider(scrapy.spiders.Spider):
    name = 'cos'
    allow_domains = ['baidu.com']
    start_urls = ['http://tieba.baidu.com/f?kw=cos&fr=ala0&tpl=5']

    def parse(self, response):
        page_selector = HtmlXPathSelector(response)
        url = response.url
        log.msg(url)

        next_page_url = page_selector.select("//div[@class='pagination-default clearfix']/a/@href").extract()[-2]
        log.msg(next_page_url)
        #TODO:加入一层redis缓存 获取没有爬取过的列表页 进去下一页
        yield scrapy.Request(next_page_url, callback=self.parse)

        #TODO:解析当前页
        invitation_list = page_selector.select("//div[@class='threadlist_title pull_left j_th_tit ']/a/@href").extract()
        for invitation_url in invitation_list:
            invitation_url = 'http://tieba.baidu.com' + invitation_url
            log.msg(invitation_url)
            yield scrapy.Request(invitation_url, callback=self.parseCospics)

    #获取图片 进入Pipeline 存储图片
    def parseCospics(self, response):
        page_selector = HtmlXPathSelector(response)
        print response.url
        img_list = page_selector.select('//img/@src')
        for img in img_list:
            print img
