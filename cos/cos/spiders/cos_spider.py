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
        print page_selector.select("//div[@class='pagination-default clearfix']/a/text()")
        if page_selector.select("//div[@class='pagination-default clearfix']/a/text()").extract() == u'下一页':
            next_page_url = page_selector.select("//div[@class='pagination-default clearfix']/a/@href").extract()[0]
            log.msg(next_page_url)
            #TODO:加入一层redis缓存 获取没有爬取过的列表页 进去下一页
            yield scrapy.Request(next_page_url, callback=self.parse)

        #TODO:解析当前页
        invitation_list = 'http://tieba.baidu.com' + page_selector.select("//div[@class='threadlist_title pull_left j_th_tit ']/a/@href").extract()[0]
        for invitation_url in invitation_list:
            yield scrapy.Request(invitation_list, callback=self.parseCospics)

    #获取图片 进入Pipeline 存储图片
    def parseCospics(self, response):
        page_selector = HtmlXPathSelector(response)
        print response.url
