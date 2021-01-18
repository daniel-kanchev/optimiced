import scrapy
import time
from scrapy.loader import ItemLoader
from optimiced.items import Article
from datetime import datetime
import re


class OptiSpider(scrapy.Spider):
    name = 'opti_en'
    allowed_domains = ['optimiced.com']
    start_urls = ['http://optimiced.com/en']

    def parse(self, response):
        articles = response.xpath("//article")
        for article in articles:
            link = article.xpath(".//h2/a/@href").get()
            yield response.follow(link, self.parse_article)

        previous_url = response.xpath("//div[@class='previous']/a/@href").get()
        if previous_url:
            yield response.follow(previous_url, self.parse)

    def parse_article(self, response):
        item = ItemLoader(item=Article(), response=response)

        date = response.xpath("//time/text()").get()
        title = response.xpath("//h1/text()").get()

        article = response.xpath("//article[1]")

        # all text in content section
        text = article.xpath(".//div[@class='entry-content']/descendant-or-self::*/text()").getall()

        text = [re.sub(' +', ' ', t).strip() for t in text if re.sub(' +', ' ', t).strip()]  # removes whitespace
        text = " ".join(text)

        # format date
        date_time_obj = datetime.strptime(date, '%d/%B/%Y')  # 7/January/2014
        date = date_time_obj.strftime("%y/%m/%d")

        item.add_value('title', title)
        item.add_value('date', date)
        item.add_value('link', response.url)
        item.add_value('text', text)
        item.add_value('lang', 'en')

        return item.load_item()
