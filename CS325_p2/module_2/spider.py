from bs4 import BeautifulSoup
from pathlib import Path
import requests

class ArticleSpider:
    def __init__(self, urls_file):
        self.urls_file = urls_file

    def start_requests(self):
        with open(self.urls_file, 'r') as file:
            urls = file.readlines()

        for url in urls:
            response = requests.get(url.strip())
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.title.string
            text = '\n'.join([p.get_text() for p in soup.find_all('p')])

            yield title, text