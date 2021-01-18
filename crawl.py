from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import time

# This file runs both spiders at the same time
t1 = time.time()
process = CrawlerProcess(get_project_settings())
process.crawl('opti_en')
process.crawl('opti_bg')
process.start()
t2 = time.time()
print(f"Scraping finished in {round(t2-t1,2)} seconds.")
