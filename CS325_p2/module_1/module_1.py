import os

def get_urls(articles_file):
    """ Reads URLs form a text file

        Args:
            article_file: Path to the file containing URLs (assumed to be in "Data/raw").

        Returns:
            A list of URLs    
    """

    # Costruct abolte path based on expected filder structure
    articles_file = os.path.join("Data", "raw", articles_file)

    # Reads URLs from the file
    with open(articles_file, 'r') as file:
        urls = [line.strip() for line in file.readlines()]

    return urls