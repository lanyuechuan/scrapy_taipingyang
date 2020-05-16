# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient

client = MongoClient(host='120.27.242.29',port=8004)  # 实例化client，建立连接,我是docker跑的8004端口映射到默认端口27017



class FbsproPipeline(object):
    collection = client['tai_ping_yang']['goods']  # 选择数据库及里面的集合
    def process_item(self, item, spider):
        self.collection.insert_one(item)
        return item
