import scrapy
import time
from scrapy.loader import ItemLoader
from optimiced.items import Article
from datetime import datetime
import re


class OptiSpider(scrapy.Spider):
    name = 'opti_bg'
    allowed_domains = ['optimiced.com']
    start_urls = ['http://optimiced.com/bg']

    def parse(self, response):
        posts = response.xpath("//div[@class='post']")
        for post in posts:
            link = post.xpath(".//h2/a/@href").get()
            date = post.xpath(".//small/text()").get()
            yield response.follow(link, self.parse_article, cb_kwargs=dict(date=date))

        # url to previous page
        previous_url = response.xpath("//div[@class='alignleft']/a/@href").get()
        if previous_url:
            yield response.follow(previous_url, self.parse)

    def parse_article(self, response, date):
        item = ItemLoader(item=Article(), response=response)

        title = response.xpath("//div[@class='post']/h2/a/text()").get()

        text = response.xpath("//div[@class='entry']/descendant-or-self::*/text()").getall()
        text = [re.sub(' +', ' ', t).strip() for t in text if re.sub(' +', ' ', t).strip()]  # removes whitespace
        text = " ".join(text)

        # removes unnecessary meta info at the end of the post
        cut_off_index = text.find("This entry was posted")
        text = text[:cut_off_index]

        # removes date suffix, such as 'st', 'rd', etc.
        date = date.split(' ')
        date[1] = date[1][:-3]
        date = " ".join(date)

        # format date
        date_time_obj = datetime.strptime(date.strip(), '%B %d %Y @ %H:%M')  # December 31st, 2016 @ 13: 00
        date = date_time_obj.strftime("%y/%m/%d %H:%M")

        item.add_value('title', title)
        item.add_value('date', date)
        item.add_value('link', response.url)
        item.add_value('text', text)
        item.add_value('lang', 'bg')

        return item.load_item()
