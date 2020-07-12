# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser


class QuotesSpider(scrapy.Spider):
    name = "quotes_login"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = (
        'http://quotes.toscrape.com/login',
    )

    def parse(self, response):
        login_token = response.css('input[name="csrf_token"]::attr(value)').extract_first()
        postParam = FormRequest.from_response(response,
                                              formdata = {'csrf_token':login_token,
                                                          'username': 'foobar',
                                                          'password':'foobar'},
                                               callback = self.getPage)

        return postParam

    def getPage(self, response):
        open_in_browser(response)
        h1_tag = response.css('h1 a::text').extract_first()
        print(h1_tag)
