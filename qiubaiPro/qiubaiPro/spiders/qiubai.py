import scrapy


class QiubaiSpider(scrapy.Spider):
    name = "qiubai"
    allowed_domains = ["www.xxx.com"]
    start_urls = ["https://www.qiushibaike.com/text/"]

    def parse(self, response):
        #解析：作者的名称+段子内容
