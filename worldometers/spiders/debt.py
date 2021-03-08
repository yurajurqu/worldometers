# -*- coding: utf-8 -*-
import scrapy


class DebtSpider(scrapy.Spider):
    name = 'debt'
    allowed_domains = ['worldpopulationreview.com']
    start_urls = ['http://worldpopulationreview.com/countries/countries-by-national-debt']

    def parse(self, response):
        countries = response.xpath('//table/tbody/tr')
        for country in countries:
            name = country.xpath('.//a/text()').get()
            debt = country.xpath('(.//td)[2]/text()').get()
            yield {
                'country': name,
                'debt': debt
            }
