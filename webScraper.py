'''
Program to scrape data from any job listing websites

Author: Kumar Shivam

'''

import scrapy


class CareerGuide(scrapy.Spider):
    name = 'Career'

    # This is a built-in Scrapy function that runs first where we'll override the default headers
    def start_requests(self):
        url = 'https://www.careerguide.com/career-options'
        
        # Setting the headers here.
        headers =  {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36',
            'Accept': 'application/json,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
        }
        yield scrapy.http.Request(url, headers=headers)

    # Creating functions to perform parsing through url
    def parse(self, response):
        for subject in response.css('div.col-md-4'):
            if subject.css('h2.c-font-bold ::text').get() == "Institutes in India":
                pass
            else:
                yield {
                    'name': subject.css('h2.c-font-bold ::text').get(),
                    'jobs': subject.css('ul.c-content-list-1.c-theme.c-separator-dot ::text').getall(),
                }
