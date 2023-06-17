# Scrapy Spider For Retrieving Data With Infinite Scrolling From A Quotes API
# Target Website: Quotes To Scrape: https://quotes.toscrape.com/scroll
# 26/03/2023 -> Used the API calls to scrape quotes data (XHR Markup Syntax) 
# Instructions To Use: 1) Create an Anaconda v-env
# 2) Install Scrapy and its dependencies
# 3) Use the crawler to retrieve the data from the website
import scrapy
import json
class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/api/quotes?page=1"]

    def parse(self, response):
        json_response = json.loads(response.body)
        quotes =  json_response.get('quotes') # Get quotes key from the response
        print(quotes) # List of JSON objects
        for quote in quotes: 
            yield{
                'author': quote.get('author').get('name'),
                'tags': quote.get('tags'),
                'quotes': quote.get('text')
            }
        # Dealing with infinite pagination using the attributes of the JSON response object itself
        has_next = json_response.get('has_next')
        if has_next == True:
            next_page_number = json_response.get('page') + 1
            yield scrapy.Request(url = f'https://quotes.toscrape.com/api/quotes?page={next_page_number}', callback = self.parse)
        # print(response.body) -> Spider testing function call
