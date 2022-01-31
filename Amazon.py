import scrapy
from scrapy.utils.response import open_in_browser

def get_headers(s, sep=': ', strip_cookie=True, strip_cl=True, strip_headers: list = []) -> dict():     ## for remove captcha's
    d = dict()
    for kv in s.split('\n'):
        kv = kv.strip()
        if kv and sep in kv:
            v=''
            k = kv.split(sep)[0]
            if len(kv.split(sep)) == 1:
                v = ''
            else:
                v = kv.split(sep)[1]
            if v == '\'\'':
                v =''
            # v = kv.split(sep)[1]
            if strip_cookie and k.lower() == 'cookie': continue
            if strip_cl and k.lower() == 'content-length': continue
            if k in strip_headers: continue
            d[k] = v
    return d


class AmazonSpider(scrapy.Spider):
    name = 'Amazon'

    url = "https://www.amazon.com/s?k=Macbook+air&page=2&crid=3MNE1JFI77HRT&qid=1643619462&sprefix=macbook+%2Caps%2C928&ref=sr_pg_{}"

    def start_requests(self):                                  ## headers  $  paginations
        header = {

            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'cookie': 'session-id=130-7121030-0301419; session-id-time=2082787201l; i18n-prefs=USD; sp-cdn="L5Z9:PK"; csm-hit=tb:s-XCTRVW85NPD43G5Y64E9|1643619434252&t:1643619436492&adb:adblk_no; ubid-main=133-2904675-4700602; session-token=PPCEDsMiFWyDwOXaQyweyFjCp3DWxJJAFR7i3F5e5GtMiLl0iVYHMIt2Q3LEo0wQ6WEAtess/WfqR3mLnQSK+yw0D51V4pV1uJI70ZHJ776sK5DCZwHyyGQiP/bT1sfSm2uCOFGhfvXooZ2W3JKkDKkfmGI/+XAus9cIAPz5OrHbrAqz8SQSpn9Vep/BHE9F',
            'downlink': '2.15',
            'ect': '4g',
            'rtt': '50',
            'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
        }
        for i in range(3):                                                    ##  Paginations of pages
            url_list = scrapy.Request(self.url.format(i), headers=header)
            yield url_list

    def parse(self, response):

        open_in_browser(response)                 ## Open webbrower of sites

        item = response.css('.s-result-item')
        for data in item:
           name = data.css('.a-size-medium::text').getall()
           price = data.css('a > .a-size-base::text').getall()
           image = data.css('div > img::attr(src)').get()

           amazon_dict= {
                "Name": name,
                "Price": price,
                "Image": image
            }

           yield amazon_dict
