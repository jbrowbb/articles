from module_1 import scraper
from module_2 import spider
import os

def main():
    # Path to the file containing URLs
    urls_file = 'Data/raw/urls.txt'

    # Scrape articles and save them in separate files
    article_files = scraper.scrape_articles(urls_file)

    # Create an instance of ArticleSpider from module_2
    article_spider = spider.ArticleSpider(article_files)

    # Start crawling and processing articles
    for article_text in article_spider.start_requests():
        # Get the title of the article
        title = article_text.split('\n', 1)[0]

        # Create a file path for the processed article
        processed_file_path = os.path.join('Data', 'processed', f'{title}.txt')

        # Write the article text to the processed file
        with open(processed_file_path, 'w', encoding='utf-8') as processed_file:
            processed_file.write(article_text)

if __name__ == "__main__":
    main()