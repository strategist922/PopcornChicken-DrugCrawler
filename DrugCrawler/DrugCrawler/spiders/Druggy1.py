# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from DrugCrawler.item import DrugcrawlerItem


class ElectronicsSpider(CrawlSpider):
    name = "Druggy1"
    allowed_domains = ["www.olx.com.pk"]
    start_urls = [
        'https://www.olx.com.pk/computers-accessories/',
        'https://www.olx.com.pk/tv-video-audio/',
        'https://www.olx.com.pk/games-entertainment/'
    ]

    rules = (
        Rule(LinkExtractor(allow=(), restrict_css=('.pageNextPrev',)),
             callback="parse_item",
             follow=False),)

    def parse_item(self, response):
        item_links = response.css('.large > .detailsLink::attr(href)').extract()
        for a in item_links:
            yield scrapy.Request(a, callback=self.parse_detail_page)

    def parse_detail_page(self, response):
        title = response.css('h1::text').extract()[0].strip()
        price = response.css('.pricelabel > strong::text').extract()[0]

        item = DrugcrawlerItem()
        item['title'] = title
        item['price'] = price
        item['url'] = response.url
        yield item
