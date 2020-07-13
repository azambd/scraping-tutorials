# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = (
        'http://quotes.toscrape.com/',
    )

    def parse(self, response):
        # quotes = response.xpath('//*[@class="quote"]')
        # for quote in quotes:
        #     text = quote.xpath('.//*[@class="text"]/text()').extract_first()
        #     author = quote.xpath('.//*[@itemprop="author"]/text()').extract_first()
        #     tags = quote.xpath('.//*[@itemprop="keywords"]/@content').extract_first()
        #Using CSS Selector:
        quotes = response.css('div.quote')
        for quote in quotes:
            text = quote.css('span.text::text').extract_first()
            author = quote.css('small[itemprop="author"]::text').extract_first()
            tags = quote.css('[itemprop="keywords"]::attr(content)').extract_first()

            yield{'Text': text,
                  'Author': author,
                  'Tags': tags}

        next_page_url = response.css('.next a::attr(href)').extract_first()
        absolute_next_page_url = response.urljoin(next_page_url)
        yield scrapy.Request(absolute_next_page_url)
