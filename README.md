# Stack Overflow Scraping

Save all question and answer of any user in MongoDb using Scrapy (http://scrapy.org) + MongoDb

##Compatability

This is Compatability with Python 3

## How to run this script

1. Download this repository on your local disk
2. Open the terminal (for linux OS) or Command Prompt (for windows OS) and browse the location of this folder
3. Run below commands in this folder

scrapy crawl feeds

### Usage

This program required python to be installed

Install Python 3.6 from https://www.python.org/downloads/

### Create a virtual environment not required, but nice to have

mkvirtualenv webscrapper

### Install python packages

pip install scrapy #Scrapy 1.5.0

### Install and Setup MongoDB from https://www.mongodb.com/

Set below parameters in settings.py

MONGODB_SERVER = "localhost"

MONGODB_PORT = 27017

MONGODB_DB = "stackoverflow" #Database name

MONGODB_COLLECTION = "feeds" #Collection name

cd stackoverflow

scrapy crawl feeds

You can use this code as an example to help you get started as well as Scrapy's great documentation. http://doc.scrapy.org/en/0.24/

==> All questions and answers will be stored in MongoDb.

## License

This project is licensed under the MIT License