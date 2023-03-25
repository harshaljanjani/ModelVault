# Scrapy Spider For Retrieving World Population Data
# Instructions to use: 1) Create an Anaconda v-env
# 2) Install Scrapy and its dependencies
# 3) Use the spider to retrieve the data from the website
import scrapy
class WorldometerSpider(scrapy.Spider):
    name = "worldometer"
    allowed_domains = ["www.worldometers.info"]
    start_urls = ["https://www.worldometers.info/world-population/population-by-country"]

    def parse(self, response):
        title = response.xpath('//h1/text()').get()
        countries = response.xpath('//td/a/text()').getall()

        # return data extracted
        yield {
            'titles': title,
            'countries': countries,
        }
