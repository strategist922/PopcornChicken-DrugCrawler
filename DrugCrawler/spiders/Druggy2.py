import scrapy
#Purposed for GARD rarediseases.org scraping

class Druggy1(scrapy.Spider):
    name = 'Druggy2'
    start_urls = ['https://rarediseases.info.nih.gov/diseases/browse-by-first-letter/Z']

    # custom_settings = {
    #   'DEPTH_LIMIT': 1
    #}

    handle_httpstatus_list = [400]
    # allowed_domains = ['rarediseases.org']
    def parse(self, response):
        SET_SELECTOR = 'ul.listing-diseases'
        for brickset in response.css(SET_SELECTOR):

            # SCIENTIFIC_NAME = 'ul span ::text'
            COMMON_NAME = 'ul a ::text'
            yield {
                'Common Names Z': brickset.css(COMMON_NAME).extract()
               # 'pieces': brickset.xpath(PIECES_SELECTOR).extract_first(),
            }
        NEXT_PAGE_SELECTOR = 'ul.m10.clearfix.alpha-search.alpha-block-list a ::attr(href)'
        next_page = response.css(NEXT_PAGE_SELECTOR).getall()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
        )

