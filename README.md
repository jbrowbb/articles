## article.txt
- filled with five urls from Variety that are articles over YouTube:
    - MatPat leaving YouTube
    - Free streaming of Escape the Night by Joey Graceffa
    - 2018 YouTube Rewind being cringey
    - Ned Fulmer getting removed from The Try Guys channel
    - Grand Theft Auto 6 is the most viewed YouTube trailer

 ## article.txt p2
 - filled with five more urls from Variety that are over anime
   - Newflix and other streaming services are doubling down on anime
   - Crunchyroll and Funnimation are merging, while Sony drops Funimation
   - Attack on Kyoto Animation
   - Netfilx Live Action One Piece aiming to capitalize
   - Funimation ends anime licensing pact with Crunchyroll

## requirements.yml
- Created a base in conda called article_reader with python version 3.10.11
- Activated the environment
- Installing pandas package 2.1.4 with numpy 1.26.3
- Installed scrapy 2.8.0 from anaconda.org anaconda/packages/scrapy
###
- Exporting article_reader environment as requirements.yml
- Moved into Project-1 folder
- Deactivated environment

## powershell

In the powershell with the README.md file conda install scrapy.
Then use scrapy startproject myproject to use the spider feature in scrapy.
Inside the main project folder create a folder to hold all the written articles text files, as well as main.py and scraper.py
Inside the second folder with the same name as the main folder, there is a folder called spiders, inside that add spider.py

## main.py
- Imports the function scrape_articles from scraper.py

## scraper.py
- Uses the class CralerProcess from the crawler folder that is apart of the package scrapy
- Uses the function crawl with the class inside spider.py
- Then starts the crawl function

## spider.py
- Loacated in the spiders folder
- Uses a function called start_requests, which reads the lines from articles.txt and sends each url to send a resquest to scrapy to read the lines from the article
    - The function uses strip() the remove the white space from the article
    - callback=self.parse is used in the next function called parse, which directs the request and writes it to the different text files
