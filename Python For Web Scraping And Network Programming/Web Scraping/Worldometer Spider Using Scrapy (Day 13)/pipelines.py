# Define your item pipelines here
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# Useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import logging
import pymongo

# MongoDB Atlas Pipeline For Storing Scraped Data Into Collections
class MongoDBPipeline:
    collection_name = 'transcripts'
    # Called when spider starts running
    def open_spider(self,spider):
        logging.warning('Spider Opened - Pipeline')
        self.client = pymongo.MongoClient("mongodb+srv://adminUser:adminPass@mongo-cluster.wav4pod.mongodb.net/?retryWrites=true&w=majority") # Set connection string -> This is an exemplar connection string, the original connection string has not been kept open-source.
        self.db = self.client['My_Database']

    # Destructor function (Called when spider finishes scraping process)
    def close_spider(self,spider):
        logging.warning('Spider Closed - Pipeline')
        self.client.close() # Close connection with MongoDB

    # Function called for each item scraped from the website
    def process_item(self, item, spider):
        self.db[self.collection_name].insert(item) # Name of collection to insert each item into
        return item
