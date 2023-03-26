# Define your item pipelines here
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# Useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import logging
import pymongo
import sqlite3

# MongoDB Atlas Pipeline For Storing Scraped Data Into Collections
class MongoDBPipeline:
    collection_name = 'transcripts'
    # Called when spider starts running
    def open_spider(self,spider):
        logging.warning('Spider Opened MongoDB - Pipeline')
        self.client = pymongo.MongoClient("mongodb+srv://adminUser:adminPass@mongo-cluster.wav4pod.mongodb.net/?retryWrites=true&w=majority") # Set connection string -> This is an exemplar connection string, the original connection string has not been kept open-source.
        self.db = self.client['My_Database']

    # Destructor function (Called when spider finishes scraping process)
    def close_spider(self,spider):
        logging.warning('Spider Closed MongoDB - Pipeline')
        self.client.close() # Close connection with MongoDB

    # Function called for each item scraped from the website
    def process_item(self, item, spider):
        self.db[self.collection_name].insert(item) # Name of collection to insert each item into
        return item

# SQLite3 Pipeline For Storing Scraped Data Into A Relational DB
class SQLite3Pipeline:
    # Called when spider starts running
    def open_spider(self,spider):
        logging.warning('Spider Opened SQLite3 - Pipeline')
        self.connection = sqlite3.connect('transcripts.db') # Create a database file
        # Create a cursor object
        self.c = self.connection.cursor()
        try:
            # Enter query
            self.c.execute('''
                CREATE TABLE transcripts(
                    title TEXT,
                    plot TEXT,
                    transcript TEXT,
                    url TEXT
                )
            ''')
            self.connection.commit()
        except sqlite3.OperationalError:
            pass

    # Destructor function (Called when spider finishes scraping process)
    def close_spider(self,spider):
        logging.warning('Spider Closed SQLite3 - Pipeline')
        self.connection.close()
        
    # Function called for each item scraped from the website
    def process_item(self, item, spider):
        self.c.execute('''
            INSERT INTO transcripts(title,plot,transcript,url) VALUES(?,?,?,?)
        ''', (
            item.get('title'),
            item.get('plot'),
            item.get('transcript'),
            item.get('url'),
        ))
        self.connection.commit()
        return item