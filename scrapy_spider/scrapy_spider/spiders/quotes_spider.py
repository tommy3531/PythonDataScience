# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule, SitemapSpider
from scrapy.linkextractors import LinkExtractor


class QuotesSpiderSpider(SitemapSpider):
    # The name of the spider
    name = "datablogger"

    # The domains that are allowed (links to other domains are skipped)
    sitemap_urls = ['https://worldview.stratfor.com/sitemap.xml']
    sitemap_rules = [('china', 'parse')]

    def parse(self, response):
        print(response.url)
