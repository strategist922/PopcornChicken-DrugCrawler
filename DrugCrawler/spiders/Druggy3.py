import scrapy
from DrugCrawler.items import DrugcrawlerItem
#Purposed for GARD rarediseases.org scraping

class Druggy1(scrapy.Spider):
    name = 'Druggy4'
    start_urls = ['https://globalgenes.org/rare-list/']

    # custom_settings = {
    #   'DEPTH_LIMIT': 1
    #}

    handle_httpstatus_list = [400]
    # allowed_domains = ['rarediseases.org']
    def parse(self, response):
        SET_SELECTOR = 'h1'
        for brickset in response.css(SET_SELECTOR):

            SCIENTIFIC_NAME = 'h1::text'
            # COMMON_NAME = 'ul a ::text'
            yield {
                "Header Ones": brickset.css(SCIENTIFIC_NAME).extract()
               # 'pieces': brickset.xpath(PIECES_SELECTOR).extract_first(),
            }
        a_selectors = response.xpath("//a")
        # Loop on each tag
        for selector in a_selectors:
            link = selector.xpath("@href").extract_first()
            # Create a new Request object
            request = response.follow(link, callback=self.parse)
            # Return it thanks to a generator
            yield request

    def parse_item(self, response):
        SCIENTIFIC_NAME = '//h1/text()'
        item = DrugcrawlerItem()
        item['title'] = response.xpath(SCIENTIFIC_NAME).extract()
        return item