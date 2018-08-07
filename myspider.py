import scrapy
from scrapy.crawler import CrawlerProcess

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

if __name__ == "__main__":
    process = CrawlerProcess({
        'FEED_FORMAT': 'jsonlines',
        'FEED_URI': 'log/wiprodigital.json'
    })

    process.crawl(WiproDigitalSpider)
    process.start()
