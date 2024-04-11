from module_1 import get_urls
from module_2 import scrape_articles

if __name__=="__main__":
    """ SCrapes articles from text file and saces them to separate files."""

    # replace with path if not correct (assumption it is in "Data/raw")
    articles_file = "articles.txt"

    # Get URLs from the text file
    urls = get_urls(articles_file)

    # Scrape articles from the URLs
    scrape_articles(urls)

    print(f"Articles scraped and saved into Data/processed")