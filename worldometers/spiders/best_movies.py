# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BestMoviesSpider(CrawlSpider):
    name = 'best_movies'
    allowed_domains = ['imdb.com']

    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0'

    def start_requests(self):
        yield scrapy.Request(url='https://www.imdb.com/search/title/?groups=top_250&sort=user_rating,desc&view=simple',
        headers={'User-Agent': self.user_agent})
    
    rules = (
        Rule(LinkExtractor(restrict_xpaths="//span[@class='lister-item-header']/span[@title]/a"), callback='parse_item', follow=True, process_request='set_user_agent'),
        Rule(LinkExtractor(restrict_xpaths="(//a[@class='lister-page-next next-page'])[2]"),process_request='set_user_agent'),
    )
    def set_user_agent(self, request):
        request.headers['User-Agent'] = self.user_agent
        return request
    def parse_item(self, response):
        
        # item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        # return item
        # print(response.url)
        yield {
            'title': response.xpath("//div[@class='title_wrapper']/h1/text()").get(),
            'year': response.xpath("//span[@id='titleYear']/a/text()").get(),
            'duration': response.xpath("normalize-space(//div[@class='title_wrapper']//time[@datetime]/text())").get(),
            'genre': response.xpath("(//div[@class='subtext']/a)[1]/text()").get(),
            'rating': response.xpath("//span[@itemprop='ratingValue']/text()").get(),
            'movie_url': response.xpath("(//a[@data-video])[1]/@href").get(),
            'user-agent': str(response.request.headers['User-Agent'])
        }
