# -*- coding: utf-8 -*-
import scrapy


class AutotypeSpider(scrapy.Spider):
	name = 'autotype'
	allowed_domains = ['autohome.com.cn']
	start_urls = ['https://www.autohome.com.cn/car/40_1-0.0_0.0-0-0-0-0-0-0-0-0/']

	def parse(self, response):
		with open('car_page.txt','w',encoding='utf-8') as f:
			f.write(response.text)

		node_list=response.xpath("//li")
		with open('car_list_40+.txt','w',encoding='utf-8') as g:
			for node in node_list:
				name=node.xpath("./h4/a/text()").extract()
				if len(str(name))>2:
					g.write(str(name)+'\n')
					print(name)

#		with open('car_list.txt','w',encoding='utf-8') as g:
#			for node in node_list:
#				name=node.xpath("./h4/text()").extract()
#				g.write(name[0])
#				print(name[0])

#        pass
#  with open('teacher_list.txt','w',encoding='utf-8') as f:
#   for node in node_list:
#    name=node.xpath("./h3/text()").extract()
#    title=node.xpath("./h4/text()").extract()
#    info=node.xpath("./p/text()").extract()
#    f.write(name[0]+";;"+title[0]+";;"+info[0]+"\n")
#    print(name[0]+";;"+title[0])