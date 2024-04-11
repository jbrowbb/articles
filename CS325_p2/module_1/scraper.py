from bs4 import BeautifulSoup
import requests
from pathlib import Path

class ArticleScraper:
    def __init__(self, urls_file):
        self.urls_file = urls_file

    def scrape_articles(self):
        with open(self.urls_file, 'r') as file:
            urls = file.readlines()

        processed_dir = Path(__file__).resolve().parent.parent / 'Data' / 'processed'
        processed_dir.mkdir(parents=True, exist_ok=True)

        for url in urls:
            response = requests.get(url.strip())
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.title.string
            text = '\n'.join([p.get_text() for p in soup.find_all('p')])

            file_path = processed_dir / f"{title}.txt"

            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(title + '\n')
                file.write(text)
