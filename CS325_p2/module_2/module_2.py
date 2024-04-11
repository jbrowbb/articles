import os
from bs4 import BeautifulSoup
import requests

def scrape_articles(urls):
    """ Downloads articles, extracts content and save to processed files.
    
        Args:
            urls: A list of URLs to scrape
    """

    # Create the output directory is it doesn't exist
    output_dir = os.path.join("Data", "processed")
    os.makedirs(output_dir, exist_ok=True)

    # Scrape and save data for each URL
    for inx, url in enumerate(urls):
        try:
            # Download webpafe content
            response = requests.get(url)
            response.raise_for_status()     # Raise exception for non-200 status codes

            # Parse the HTML content with BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.arser')

            # Extracts article text (modify logic as needed)
            article_text = soup.get_text(strip=True)        # Get all test (adjust selector if needed)

            # Save data to the text file in the processed directory
            article_file  = os.path.join(output_dir, f'article_{idx + 1}.txt')
            with open(article_file, 'w', encoding='utf-8') as f:
                f.write(article_text)
            print(f"Article {idx + 1} scraped and saved")

        except Exception as e:
            print(f"Error scraoing article {idx +1}: {e}")