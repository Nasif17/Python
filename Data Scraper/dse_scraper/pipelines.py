import csv

class DseScraperPipeline:
    def process_item(self, item, spider):
        with open('output.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([
                item['date'], item['trading_code'], item['ltp'], item['high'], item['low'],
                item['openp'], item['closep'], item['ycp'], item['trade'], item['value'], item['volume']
            ])
        return item
