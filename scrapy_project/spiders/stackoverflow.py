# -*- coding: utf-8 -*-
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy_project.items import QuestionItem
from twisted.internet import reactor


class StackoverflowSpider(scrapy.Spider):
    name = "stackoverflow"
    allowed_domains = ["stackoverflow.com"]
    start_urls = ['https://stackoverflow.com/questions/39706005/crawlerprocess-vs-crawlerrunner']

    def parse(self, response):
        item = QuestionItem()
        item["title"] = response.xpath('//div[@id="question-header"]/h1/a/text()').extract()[0]
        item["identifier"] = response.url.split("/")[4]
        item["url"] = response.url
        return item


    def start_spider(self):
        process = CrawlerProcess({
            'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
        })

        process.crawl(StackoverflowSpider)
        process.start()

