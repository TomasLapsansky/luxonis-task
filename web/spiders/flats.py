import scrapy


class FlatsSpider(scrapy.Spider):
    name = "flats"
    URL = "https://www.sreality.cz/en/search/for-sale/apartments?page="
    cnt = 1

    def start_requests(self):
        url_start = self.URL + str(self.cnt)
        yield scrapy.Request(url=url_start, callback=self.response_parser)

    def response_parser(self, response):
        for selector in response.css('div.property, .ng-scope'):
            yield {
                'title': selector.css('span.name, .ng-binding').extract_first(),
                # 'price': selector.css('.price_color::text').extract_first()
            }

        self.cnt += 1
        next_page_link = self.URL = self.cnt
        if next_page_link:
            yield response.follow(next_page_link, callback=self.response_parser)
