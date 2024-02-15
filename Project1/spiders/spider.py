from typing import Any, Iterable
import scrapy
from pathlib import Path

from scrapy.http import Response

class ArticleSpider(scrapy.Spider):
    name = "article_spider"

    def start_requests(self):
        file_path = Path(__file__).resolve().parent.parent / 'articles.txt'
        with open(file_path, 'r') as file:
            urls = file.readlines()

        for url in urls:
            yield scrapy.Request(url.strip(), callback=self.parse)

    def parse(self, response):
        title = response.css('title::text').get()
        text = ''.join(response.css('p::text').getall())

        output_dir = Path(__file__).resolve().parent.parent / 'articles'
        file_path = output_dir / f"{title}.txt"

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(title + '\n')
            file.write(text)