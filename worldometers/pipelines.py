# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging

class WorldometersPipeline(object):
    def process_item(self, item, spider):
        return item
    def open_spider(self, spider):
        logging.warning('SPIDER OPENED FROM PIPELINE')

    def close_spider(self, spider):
        logging.warning('SPIDER CLOSED FROM PIPELINE')
    
    @classmethod
    def from_crawler(cls, crawler):
        #used to read settings.json file variables
        logging.warning(crawler.settings.get("MONGO_URL"))
