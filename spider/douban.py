import scrapy
from scrapy import Selector
from items import MovieItem 

class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["movie.douban.com"]
    start_urls = ["https://movie.douban.com/top250"]

    def parse(self, response):
        sel = Selector(response)
        # sel.re sel.xpath sel.css
        list_items=sel.css('#content > div > div.article > ol > li')
        for list_item in list_items:
            movie_item=MovieItem()
            movie_item['title']=list_item.css('span.title::text').extract_first()
            movie_item['rank']=list_item.css('span.rating_num::text').extract_first()
            movie_item['subject']=list_item.css('span.inq::text').extract_first()
        # /html/body/div[3]/div[1]/div/div[1]/ol/li[1] //*[@id="content"]/div/div[1]/ol/li[1]
        yield movie_item