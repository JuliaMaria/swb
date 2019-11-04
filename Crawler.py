import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.crawler import CrawlerProcess
from bs4 import BeautifulSoup


def find_links(page):
    soup = BeautifulSoup(page, features='html.parser')
    links = []
    for a in soup.find_all('a', href=True):
        if a['href'].endswith('.php'):
            links.append(a['href'])
    return links


class Crawler(CrawlSpider):
    name = "Crawler"
    BASE_URL = 'http://rjawor.home.amu.edu.pl'
    visited = []

    rules = (Rule(LinkExtractor(), callback="parse_obj", follow=True),
             )

    def start_requests(self):

        urls = [
            'http://rjawor.home.amu.edu.pl',
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        if response.url not in self.visited:
            page = response.url
            print(page)
            # filename = 'page-crawl-(%s).html' % page
            self.visited.append(response.url)
            # with open(filename, 'w+') as f:
            #     f.write(response.body)

            for link in find_links(response.body):
                absolute_url = self.BASE_URL + '/' + link
                yield scrapy.Request(absolute_url, callback=self.parse)


process = CrawlerProcess()

process.crawl(Crawler)
process.start()

