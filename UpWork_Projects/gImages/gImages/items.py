# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst


class GimagesItem(scrapy.Item):
    place_name = scrapy.Field(output_processor=TakeFirst())
    latitude = scrapy.Field(output_processor=TakeFirst())
    longitude = scrapy.Field(output_processor=TakeFirst())
    file_name = scrapy.Field(output_processor=TakeFirst())
    image_urls = scrapy.Field()
    #images = scrapy.Field()
    