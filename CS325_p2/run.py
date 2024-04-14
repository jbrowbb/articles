from pathlib import Path
from module_1.module_1 import get_urls
from module_2.module_2 import scrape_articles

if __name__ == "__main__":
    """ Scrapes articles from text file and saves them to separate files. """

    # Path to article file with article urls, can change
    articles_file = Path(__file__).resolve().parent /'Data'/'raw'/'articles.txt'

    # Get Urls from text file
    urls = get_urls(articles_file)

    # Scrapes articles from URLs
    scrape_articles(urls)

    print(f"Articles scraped and saved to Data/processed")