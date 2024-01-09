import scrapy

#爬虫获取的对象需要组装成Item对象
class MovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    title=scrapy.Field()
    rank=scrapy.Field()
    subject=scrapy.Field()