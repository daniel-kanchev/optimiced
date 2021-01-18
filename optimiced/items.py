import scrapy


class Article(scrapy.Item):
    title = scrapy.Field()  # title of the article
    link = scrapy.Field()  # link to the article
    date = scrapy.Field()  # date when article was posted
    text = scrapy.Field()  # full text of the article
    lang = scrapy.Field()  # language it was written in (bg/en)
