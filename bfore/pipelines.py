# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
from termcolor import colored
import csv
from datetime import datetime

class BforePipeline(object):

    def open_spider(self, spider):
        self.li = []

    def close_spider(self, spider):
        file_name = datetime.strftime(datetime.now(),"TV_%a_%b_%d_%Y_%I:%M:%S_%p.csv")
        with open(file_name,"w") as csvfile:
            l=set()
            for i in self.li:
                l=l.union(json.loads(i).keys())
            fieldnames=list(l)
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for i in self.li:
                writer.writerow(json.loads(i))

    def process_item(self, item, spider):
        d={}
        for key,value in dict(item).items():
            if len(value)==1 and not isinstance(value[0],dict):
                d[key]=value[0]
            elif len(value)==1 and  isinstance(value[0],dict):
                d.update(value[0])
            elif len(value)==0:
                d[key]="None"
            elif len(value)>1:
                d[key]=value
        self.li.append(json.dumps(d))
