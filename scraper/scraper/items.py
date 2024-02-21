import scrapy


class ScraperItem(scrapy.Item):
    title = scrapy.Field()
    image = scrapy.Field()
