# Scrapy Crawler For Retrieving Movie Transcripts, Titles, Plots And Associated Metadata
# Note To The User: Change 'start-urls' to "https://subslikescript.com/" if you want to retrieve 'all' of the movies data. The current script only retrieves data of those movies beginning with the letter 'X'
# Instructions To Use: 1) Create an Anaconda v-env
# 2) Install Scrapy and its dependencies
# 3) Use the crawler to retrieve the data from the website
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class TranscriptsSpider(CrawlSpider):
    name = "transcripts"
    allowed_domains = ["subslikescript.com"]  
    # Setting a user-agent variable
    start_urls = ['https://subslikescript.com/movies_letter-X']  # Let's test scraping all the pages for the X letter
    
    # LinkExtractor() automatically searches for the @href attribute. No need to mention it explicitly
    # Setting rules for the crawler
    rules = (
        Rule(LinkExtractor(restrict_xpaths=("//ul[@class='scripts-list']/a")), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths=("(//a[@rel='next'])[1]"))),
    )

    # Driver Function
    def parse_item(self, response):
        # Getting the article box that contains the data we want (title, plot, etc)
        article = response.xpath("//article[@class='main-article']")
        # Extract the data we want and then yield it
        yield{ 
            'title': article.xpath('./h1/text()').get(),
            'plot': article.xpath('./p/text()').get(),
            'transcript': article.xpath('./div[@class="full-script"]/text()').getall(),
            'url': response.url,
        }
