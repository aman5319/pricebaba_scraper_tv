# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider
from scrapy.loader import ItemLoader
from bfore.items import BforeItem
from termcolor import colored 
import pandas as pd
from .spider_utils import  *

class TvspiderSpider(Spider):
    name = 'tvSpider' 
    start_urls = ['https://pricebaba.com/television/pricelist/televisions-price-list-in-india/']

    def parse(self, response):
        urls = response.css("div.m-t-0").css("span.target_link::attr(data-href)").getall()[0::3]
        for url in urls:
            yield scrapy.Request(url=url , callback=self.detail_parser)
        next_page_url = response.css("a[rel=next] ::attr(href)").get()
        if next_page_url is not None:
            yield response.follow(url=next_page_url, callback=self.parse)

    def detail_parser(self,response):
        l = ItemLoader(item = BforeItem() , response = response)
        l.add_value("product_url",response.url)
        l.add_css("title" , "h1 ::text")
        l.add_css("image_link" , "img[class=gllry__img\ gllry__img--s\ lazy]::attr(data-src)")
        l.add_css("rating",".cui-rating::attr(title)")
        l.add_css("best_price",".lowestPrice ::text")
        table_content = response.css("div[class=blk\ ord-15]")
        for  table in table_content.css("table"):
            title = table.css(".txt-m ::text").get().lower().strip().replace(" ","_")
            temp = dict(zip([pre_process_header(i) for i in table.css(".w-40 ::text").getall()] ,
                     [pre_process_value(i) for i in table.css(".w-60 ::text").getall()]))
            l.add_value(title,temp)
        launched_in = table_content.css(".col-sm-6 .txt-wt-m ::text").get()
        model_name = table_content.css(".m-t-s .txt-wt-m ::text").get()
        update_value = pre_process_date(response.css("div[class=blk\ ord-23] ::text").get())
        l.add_value("launched_in",launched_in)
        l.add_value("model_name",model_name)
        l.add_value("update_on_price_baba",update_value)
        ratings ,reviews = response.css(".txt-underline").css(".txt-wt-b ::text").getall()
        l.add_value("no_of_people_rated",ratings)
        l.add_value("no_of_review",reviews)
        try:
            players = response.css("div[class=blk\ ord-19]").get()
            if players is not None and players.find:
                df = pd.read_html(players)[0][["Store","Price"]]
                temp = dict(zip(df.values[:,0] ,df.values[:,1] ))
                l.add_value("price_of_different_players",temp)
        except :
            print("No other players table found ")

        l.add_css("youtube_links",".youtubeVideoThumb::attr(data-videolink)")
        l.add_value("brand",response.css("a.brdcrmb__lnk ::text").getall()[-1])
        return l.load_item()
