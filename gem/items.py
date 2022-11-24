# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst    # TakeFirst text from data
from itemloaders.processors import MapCompose   # For function calling

def Single(value):
    return str(value)

def Double(value):
    data = []
    for i in value:
        data.append(i)
    return data

class GemItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field(input_processor = MapCompose() )
    price = scrapy.Field(input_processor = MapCompose())
    url = scrapy.Field(input_processor = MapCompose())
    key = scrapy.Field(input_processor = MapCompose())
    val = scrapy.Field(input_processor = MapCompose())
    category = scrapy.Field(input_processor = MapCompose())
    subCategory = scrapy.Field(input_processor = MapCompose())
