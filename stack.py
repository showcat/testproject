# -*- coding: utf-8 -*-
import scrapy


class StackSpider(scrapy.Spider):
    name = 'stack'
    allowed_domains = ['http://stackoverflow.com/']
    start_urls = ['http://http://stackoverflow.com//']

    def parse(self, response):
        pass
