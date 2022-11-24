# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
from pymongo import MongoClient
import urllib 
import uuid
import os
from .Environment import PASSWORD, ROOT, CLUSTER_

class GemPipeline:
    def __init__(self) :    
        
        URL = ROOT + urllib.parse.quote(PASSWORD) + CLUSTER_

        self.cluster = MongoClient(URL)
        self.DataBase = self.cluster['Scrapy']
        
        self.CollectionProducts = self.DataBase['Products']
        self.collectionFeatures = self.DataBase['Features']

    def process_item(self, item, spider):
        key = []
        val = []
        url = item['url']
        name = item['name']
        price = item['price']
        category = item['category']
        subCategory = item['subCategory']
        _id = str(uuid.uuid4())

        Products = {'_id': _id, 'category': category[0], 'subCategory': subCategory[0], 'name':name[0], 'price':price[0], 'url': url[0], }
        
        Features = {'_id': _id}        
        for (i, j) in zip(item['key'], item['val']):
            Features[i[0]] = j[0]
        
        self.CollectionProducts.insert_one(Products)
        self.collectionFeatures.insert_one(Features)
        
        return item
