#!/usr/bin/env python
# encoding: utf-8

import re
import scrapy
import atomdb

from scrapy import log
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector

from weibo.weibo.spiders.weibo_login import weiboLogin
from config.conf import WEIBO_USER, WEIBO_PASSWORD

class WeiboSpider(scrapy.spiders.Spider):
    name = 'weibo'
    allow_domains = ['']
    start_urls = ['']

    def parse(self, response):
        pass

if __name__ == '__main__':
    WBLogin = weiboLogin()
    WBLogin.login(user_name = WEIBO_USER, pwd = WEIBO_PASSWORD)
