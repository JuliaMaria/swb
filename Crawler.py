import scrapy
from scrapy.spiders import CrawlSpider
from scrapy.crawler import CrawlerProcess
from bs4 import BeautifulSoup
import re
from inscriptis import get_text
import urllib


def find_links(page):
    soup = BeautifulSoup(page, features='html.parser')
    links = []
    for a in soup.find_all('a', href=True):
        check1 = re.match(re.compile(r'^.*//'), a['href'])
        check2 = re.match(re.compile(r'.+\.(doc|docx|ppt|pptx|tex|pdf)$'), a['href'])
        if not check1 and not check2:
            links.append(a['href'])
    return links


class Crawler(CrawlSpider):
    name = "Crawler"
    visited = []

    def __init__(self, page, **kwargs):
        self.url = page
        super().__init__(**kwargs)

    def start_requests(self):
        yield scrapy.Request(url=self.url, callback=self.parse)

    def parse(self, response):
        if response.url not in self.visited:
            page = response.url
            self.visited.append(response.url)

            links = find_links(response.body)
            html = urllib.request.urlopen(page).read().decode('utf-8')
            text = get_text(html)

            print('Page: {}'.format(page))
            filename = 'crawl-{}.txt'.format(page.replace('/', ''))
            with open(filename, 'w+') as file:
                file.write(text)

            for link in links:
                link = link.strip('/')
                absolute_url = self.url + '/' + link
                yield scrapy.Request(absolute_url, callback=self.parse)


process = CrawlerProcess()

process.crawl(Crawler, page='http://rjawor.home.amu.edu.pl')
process.start()
