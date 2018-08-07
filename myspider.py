import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.exceptions import DropItem

class WiproDigitalSpider(scrapy.Spider):
    name = 'wiprodigital'
    start_urls = ['http://wiprodigital.com']
    allowed_domains = ['wiprodigital.com']

    def parse(self, response):
        for image in response.css('img'):
            yield { 'url': response.request.url, 'image': image.css('::attr(src)').extract_first() }

        for anchor in response.css('a'):
            yield { 'url': response.request.url, 'anchor': anchor.css('::attr(href)').extract_first() }
            yield response.follow(anchor, self.parse)

class DuplicatesPipeline(object):
    def __init__(self):
        self.data = set()

    def process_item(self, item, spider):
        row = item.get('url') + item.get('image', '') + item.get('anchor', '')
        if row in self.data:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.data.add(row)
            return item

if __name__ == "__main__":
    process = CrawlerProcess({
        'FEED_FORMAT': 'jsonlines',
        'FEED_URI': 'log/wiprodigital.json',
        'ITEM_PIPELINES': {
            'myspider.DuplicatesPipeline': 1
        }
    })

    process.crawl(WiproDigitalSpider)
    process.start()
