import scrapy
from dse_scraper.items import DseScraperItem

class DseSpider(scrapy.Spider):
    name = 'dse_spider'
    start_urls = [
        'https://www.dsebd.org/day_end_archive.php?startDate=2025-01-01&endDate=2025-07-08&inst=All%20Instrument&archive=data'  # The full URL should be correctly formatted here
    ]

    def parse(self, response):
        # Select the rows of the table
        rows = response.css('table tbody tr')

        # Loop through each row and extract the data
        for row in rows:
            item = DseScraperItem()
            item['date'] = row.css('td:nth-child(1)::text').get()
            item['trading_code'] = row.css('td:nth-child(2)::text').get()
            item['ltp'] = row.css('td:nth-child(3)::text').get()
            item['high'] = row.css('td:nth-child(4)::text').get()
            item['low'] = row.css('td:nth-child(5)::text').get()
            item['openp'] = row.css('td:nth-child(6)::text').get()
            item['closep'] = row.css('td:nth-child(7)::text').get()
            item['ycp'] = row.css('td:nth-child(8)::text').get()
            item['trade'] = row.css('td:nth-child(9)::text').get()
            item['value'] = row.css('td:nth-child(10)::text').get()
            item['volume'] = row.css('td:nth-child(11)::text').get()

            # Yield the item so that it can be saved or processed
            yield item
