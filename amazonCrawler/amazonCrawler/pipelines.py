# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
class AmazoncrawlerPipeline(object):

    def __init__(self):
        #connect to monbgodb
        self.con = pymongo.MongoClient("mongodb+srv://scrapyUser:scrapyapp@fullstackapp-ltrls.mongodb.net/Quotes?retryWrites=true&w=majority")
        db = self.con['test']
        self.collection = db["AmazonBooks"]


    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item

