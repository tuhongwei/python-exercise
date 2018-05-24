#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scrapy
import re,os,urllib
from scrapy import Request

class XiaoHuarSpider(scrapy.spiders.Spider):
	name = "xiaohuar"
	allowed_domains = ["xiaohuar.com"]
	start_urls = [
		"http://www.xiaohuar.com/hua/",
	]

	def parse(self, response):
		# current_url = response.current_url
		# body = response.body
		# unicode_body = response.body_as_unicode()
		hxs = scrapy.Selector(response)
		all_urls = hxs.select('//a/@href').extract()
		for url in all_urls:
			if url.startswith('http://www.xiaohuar.com/list-1-'):
				yield Request(url, callback=self.parse)
		if re.match('http://www.xiaohuar.com/list-1-\d+.html', response.url):
			items = hxs.select('//div[@class="item_list infinite_scroll"]/div')
			for i in range(len(items)):
				src = hxs.select('//div[@class="item_list infinite_scroll"]/div[%d]//div[@class="img"]/a/img/@src' % i).extract()
				name = hxs.select('//div[@class="item_list infinite_scroll"]/div[%d]//div[@class="img"]/span/text()' % i).extract()
				school = hxs.select('//div[@class="item_list infinite_scroll"]/div[%d]//div[@class="img"]/div[@class="btns"]/a/text()' % i).extract()
				if src:
					ab_src = "http://www.xiaohuar.com" + src[0]
					print(ab_src)
					file_name = "%s_%s.jpg" % (school[0], name[0])
					file_path = os.path.join(os.path.abspath("."), "beauty", "pic", file_name)
					urllib.urlretrieve(ab_src, file_path)

	def start_requests(self):
		for url in self.start_urls:
			yield Request(url, dont_filter=True)


