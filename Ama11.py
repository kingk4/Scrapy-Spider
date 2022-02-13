import scrapy
from scrapy.crawler import CrawlerProcess

class AmazonnSpider(scrapy.Spider):
    name = 'Amazonn'
    allowed_domains = ['amazon.com/']
    url = 'https://www.amazon.com/s?k=Macbook+air+laptops&crid=282GNWGPCNSBL&sprefix=macbook+air+laptopa%2Caps%2C407&ref=nb_sb_noss'


    def start_requests(self):                                  # Requests headers
        header = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'cookie': 'session-id=130-7121030-0301419; session-id-time=2082787201l; i18n-prefs=USD; sp-cdn="L5Z9:PK"; ubid-main=133-2904675-4700602; session-token=bh+5kJc6IWEK+VEXaHk4fibQ4pxlpHzZoWpE0AgHJ+nhIgRDyYDSNcMiCZWv63bZgN0AmJmrJSYVoffZomoCfY1HnWluZMjYE6U5NiMoPfKSXuR8PL4KsOUB4vydBKG3urZfq81fv4f81SxUL2Ezly/72krskxH7hEBTehOZUY4vq5fyE1Y+4lbzUJnfEa3+; skin=noskin; csm-hit=tb:NKDY0CZV86CE8AE3NT3C+s-D4ZCGPNP8XR4PP2VCGD7|1644583948911&t:1644583948911&adb:adblk_no',
            'downlink': '1.5',
            'ect': '3g',
            'pragma': 'no-cache',
            'referer': 'https://www.amazon.com/',
            'rtt': '350',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'
            }

        url_list = scrapy.Request(self.url, headers=header, callback=self.parse_logs)
        yield url_list


    def parse_logs(self, response):
        header1 = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'cookie': 'session-id=130-7121030-0301419; session-id-time=2082787201l; i18n-prefs=USD; sp-cdn="L5Z9:PK"; ubid-main=133-2904675-4700602; session-token=bh+5kJc6IWEK+VEXaHk4fibQ4pxlpHzZoWpE0AgHJ+nhIgRDyYDSNcMiCZWv63bZgN0AmJmrJSYVoffZomoCfY1HnWluZMjYE6U5NiMoPfKSXuR8PL4KsOUB4vydBKG3urZfq81fv4f81SxUL2Ezly/72krskxH7hEBTehOZUY4vq5fyE1Y+4lbzUJnfEa3+; skin=noskin; csm-hit=tb:NKDY0CZV86CE8AE3NT3C+s-D4ZCGPNP8XR4PP2VCGD7|1644583948911&t:1644583948911&adb:adblk_no',
            'downlink': '1.5',
            'ect': '3g',
            'pragma': 'no-cache',
            'referer': 'https://www.amazon.com/',
            'rtt': '350',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'
        }

        links = response.css('h2 > a::attr(href)').getall()
        for i in links:
            url1 = response.urljoin(i)
            # self.log(url1)
            links1 = response.follow(url=url1, headers=header1, callback=self.parse, dont_filter=True)             ## calling funtion by Name !!!!
            yield links1

    def parse(self, response):

        rating = response.css(".a-size-base::text").get()
        shipping ={
            "Shipping & import": rating
        }

        yield shipping



