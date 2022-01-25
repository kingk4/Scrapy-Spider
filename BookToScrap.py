import scrapy
                                             ## { scrapy shell "https://quotes.toscrape.com/" }        content of website
                                             ##  { response }   check response of website
                                             ## { scrapy genspider quotes quotes.toscrape.com/  }     create class of scrapy spider
                                             ## { scrapy runspider quotes.py }        run/execute  scrapy spider

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    page = 2
    allowed_domains = ['quotes.toscrape.com/']
    url = 'https://quotes.toscrape.com/page/{}/'

    def start_requests(self):                                 ## paginations of 4 pages !!!
        for i in range(1,4):
            yield scrapy.Request(self.url.format(i))

    def parse(self, response):
        self.log(f"Response :: {response.url}")                ## response of websites
        quotes_list = response.css(".quote")

        for data in quotes_list:

            books ={
                "Quote " : data.css('[itemprop="text"]::text').get(),
                "Author Name " : data.css('.author::text').get(),
                "Tags " : data.css('.tag::text').getall()
            }
            yield books                              ## return dictionary

        imp_tags = response.css(".tags-box")
        for i_tags in imp_tags:

            tags ={
                "Important_Tags" : i_tags.css(".tag-item  a::text").get()
            }

            yield tags                             ## return dictionary

#   ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
