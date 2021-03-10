# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging
import pymongo

class MongodbPipeline(object):
    collection_name = "best_movies"
    def process_item(self, item, spider):
        self.db[self.collection_name].insert(dict(item))
        return item
    def open_spider(self, spider):
        logging.warning('SPIDER OPENED FROM PIPELINE')
        self.client = pymongo.MongoClient("mongodb+srv://omar:xhP92@cluster0.nnhdq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        self.db = self.client["IMDB"]

    def close_spider(self, spider):
        logging.warning('SPIDER CLOSED FROM PIPELINE')
        self.client.close()
    
    # @classmethod
    # def from_crawler(cls, crawler):
    #     #used to read settings.json file variables
    #     logging.warning(crawler.settings.get("MONGO_URL"))
