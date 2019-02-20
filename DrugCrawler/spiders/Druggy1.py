import scrapy

#Purposed for NORD rarediseases.org scraping

class Druggy1(scrapy.Spider):
    name = 'Druggy1'
    start_urls = ['https://rarediseases.org/?s=A&post_type=rare-diseases']

    def parse(self, response):
        SET_SELECTOR = 'h3.rdr-one-title'
        for brickset in response.css(SET_SELECTOR):

            TITLE_SELECTOR = 'h3 a ::text'
           # PIECES_SELECTOR = './/dl[dt/text() = "Pieces"]/dd/a/text()'
            yield {
                'title': brickset.css(TITLE_SELECTOR).extract(),
               # 'pieces': brickset.xpath(PIECES_SELECTOR).extract_first(),
            }

        NEXT_PAGE_SELECTOR = '.next a ::attr(href)'
        next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )