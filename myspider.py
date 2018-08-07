import scrapy
from scrapy.crawler import CrawlerProcess

class WiproDigitalSpider(scrapy.Spider):
    name = 'wiprodigital'
    start_urls = ['http://wiprodigital.com']

    def parse(self, response):
        for title in response.css('.post-header>h2'):
            yield {'title': title.css('a ::text').extract_first()}

        for next_page in response.css('div.prev-post > a'):
            yield response.follow(next_page, self.parse)

if __name__ == "__main__":
    process = CrawlerProcess({
        'FEED_FORMAT': 'jsonlines',
        'FEED_URI': 'log/wiprodigital.json'
    })

    process.crawl(WiproDigitalSpider)
    process.start()
