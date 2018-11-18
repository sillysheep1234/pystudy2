﻿# -*- coding: utf-8 -*-
import scrapy

class Test0318V1Spider(scrapy.Spider):
 name = 'test_0318_v1'
 allowed_domains = ['http://www.itcast.cn']
 start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

 def parse(self, response):
#  print(str(response.body,'utf-8'))
#  with open('test_0318_v2.html','w',encoding='utf-8') as f:
#   f.write(response.text)
  node_list=response.xpath("//div[@class='li_txt']")
  with open('teacher_list.txt','w',encoding='utf-8') as f:
   for node in node_list:
    name=node.xpath("./h3/text()").extract()
    title=node.xpath("./h4/text()").extract()
    info=node.xpath("./p/text()").extract()
    f.write(name[0]+";;"+title[0]+";;"+info[0]+"\n")
    print(name[0]+";;"+title[0])