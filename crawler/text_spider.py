import scrapy
import json
from preprocess import get_text


class TextSpider(scrapy.Spider):
    name = "textscrapy"

    def get_urls(self):
        with open('datasets/data_to_scrape.csv') as f:
            urls = f.readlines()
        return urls

    def start_requests(self):
        for url in self.get_urls():
            self.log('Will scrape new url %s' % url)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        response.replace(encoding='UTF-8')

        url = response.request.url
        html = response.body

        yield {
            'url': url,
            'text': get_text(html),
        }
