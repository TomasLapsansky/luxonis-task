import json
import scrapy


class FlatSpider(scrapy.Spider):
    name = 'flats_api'
    allowed_domains = ['https://www.sreality.cz']
    start_urls = ['https://www.sreality.cz/api/en/v2/estates?category_main_cb=1&category_type_cb=1&per_page=500']

    def parse(self, response):
        json_response = json.loads(response.text)
        for item in json_response['_embedded']['estates']:
            yield {
                'title': item['name'],
                'image': item['_links']['images'][0]['href']
            }
