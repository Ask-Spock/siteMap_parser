# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup


class AsktalSpider(scrapy.Spider):
    name = 'asktal5'
    allowed_domains = ['www.ask-tal.co.il']
    start_urls = ['http://www.ask-tal.co.il/']

    def parse(self, response):
        soup = BeautifulSoup(response.body, 'html.parser')
        filename = 'ask-tal5.html'
        with open(filename, 'w') as f:
            text = soup.title.get_text()
            f.write(text)
            print(text)




