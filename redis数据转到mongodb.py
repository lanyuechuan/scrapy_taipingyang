# -*- coding: utf8 -*-
# @Author   : lanyuechuan
# @time     : 2020/5/14 17:01
# @File     : 连接redis.py
from pymongo import MongoClient
# 建立连接,我是docker跑的8004端口映射到mnogod的默认端口27017
client = MongoClient(host='0.0.0.0',port=8004)
collection = client['movie']['chuan']

import redis
conn = redis.Redis(host='0.0.0.0.', password='11111111111111111')

data_list = conn.lrange('fbs:items', 0, 2000)
i = 1
for dic in data_list:
    item = {}
    item['name'] = eval(dic.decode()).get('name')
    item['dec'] = eval(dic.decode()).get('dec')
    collection.insert_one(item)
    print('正在插入第{}条数据......'.format(i))
    i += 1
