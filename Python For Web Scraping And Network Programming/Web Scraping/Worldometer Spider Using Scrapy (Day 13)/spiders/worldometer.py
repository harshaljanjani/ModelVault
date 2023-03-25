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
        countries = response.xpath('//td/a/').getall()

        for country in countries:
            country_name = country.xpath(".//text()").get()
            link = country.xpath(".//@href").get()
            # Return data extracted at each iteration
            # If we were to yield "scrapy.Request(url=link)", we'd not be able to visit the scraped link as it is, since it's in relative form.
            # Obselete way of concatenation: absolute_url = f'https://www.worldometers.info/{link}'
            absolute_url = response.urljoin(link) 
            yield {
                'country_names': country_name,
                'links': absolute_url, # Convert relative links to absolute links
            }
            # Alternative Syntax:
            # scrapy.Request(url=absolute_url) -> 200 OK response
            # response.follow(url=link) -> 200 OK response
