# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import psycopg2


class ScraperPipeline:
    def process_item(self, item, spider):
        return item


class PostgresPipeline:
    def open_spider(self, spider):
        hostname = spider.settings.get('DATABASE')['host']
        username = spider.settings.get('DATABASE')['username']
        password = spider.settings.get('DATABASE')['password']
        database = spider.settings.get('DATABASE')['database']
        port = spider.settings.get('DATABASE')['port']
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database, port=port)
        self.cur = self.connection.cursor()

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()

    def process_item(self, item, spider):
        self.cur.execute("INSERT INTO flat (name, image) VALUES (%s, %s)", (item['title'], item['image']))
        self.connection.commit()
        return item
