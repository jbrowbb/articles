from scrapy.crawler import CrawlerProcess
from spiders.spider import ArticleSpider

def scrape_articles():
    process = CrawlerProcess()
    process.crawl(ArticleSpider)
    process.start()