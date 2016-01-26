#! /usr/bin/env python
# -*- coding: utf-8 -*-

from config.conf import REDIS_CONF

#百度贴吧过滤列表页
def get_url(url_list):
    conn = redis.Redis(host=REDIS_CONF['host'], port=REDIS_CONF['port'], db=REDIS_CONF['db'], password=REDIS_CONF['redis_pwd'])
    data = 'cid={0}&pwd={1}'.format(USER_NAME, PWD)
    final_url_list = []
    for item in url_list:
        conn.set('percent_session_key', session_key, '1800')#缓存半个小时
        print conn.get('percent_session_key')
