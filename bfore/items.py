# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose,TakeFirst
import re

def urlQueryRemove(value):
    if value is not None:
        return value.split("?")[0]

def rating(value):
    if value is not None:
        if value.find("No") !=-1 :
            return 0
        return value.split()[1]

class BforeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    product_url = scrapy.Field()
    title = scrapy.Field()
    image_link = scrapy.Field(output_processor=MapCompose(urlQueryRemove))
    rating = scrapy.Field(input_processor=TakeFirst(), output_processor=MapCompose(rating))
    best_price = scrapy.Field(input_processor=TakeFirst())
    display = scrapy.Field()
    audio_features = scrapy.Field()
    internet_features_and_ports = scrapy.Field()
    general_specifications = scrapy.Field()
    smart_tv_features = scrapy.Field()
    update_on_price_baba = scrapy.Field()
    launched_in = scrapy.Field()
    model_name = scrapy.Field()
    no_of_people_rated=scrapy.Field()
    no_of_review = scrapy.Field()
    price_of_different_players = scrapy.Field()
    youtube_links=scrapy.Field()
    brand = scrapy.Field()
