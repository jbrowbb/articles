from pathlib import Path

def get_urls(article_file: Path):
    """ Reads URLs form a text file.

    Args:
        articles_file: Path to the file containing URLs

    Returns:
        A list of URLs to be scraped
    """

    # Reads URLs from the file
    with article_file.open('r') as file:
        urls = [line.strip() for line in file.readlines()]

    return urls