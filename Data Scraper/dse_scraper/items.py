import scrapy

class DseScraperItem(scrapy.Item):
    date = scrapy.Field()
    trading_code = scrapy.Field()
    ltp = scrapy.Field()
    high = scrapy.Field()
    low = scrapy.Field()
    openp = scrapy.Field()
    closep = scrapy.Field()
    ycp = scrapy.Field()
    trade = scrapy.Field()
    value = scrapy.Field()
    volume = scrapy.Field()
