import scrapy
from scrapy_splash import splashRequests
from scrapy.selector import selector
from wikipedia.items import WikipediaItem

class SpiderwikiSpider(scrapy.Spider):
    name = "spiderwiki"
    allowed_domains = ["https://www.livegood.com/login"]
    lua_file_path = "code.lua"

    def read_lua(self):
        with open(lua_file_path, "r") as file:
            self.lua_code = file.read()

    def start_requests(self):
        SplashRequest(
            url = 'https://www.livegood.com/bo/home',
            callback = self.parse,
            endpoint = 'execute',
            args = {
                "lua_code": self.lua_code,
            }
        )

    def parse(self, response):
        learn_mores = response.xpath("//a[@class='btn learn-more-btn']")

        for learn_more in learn_mores:
            yield response.follow(learn_more, callback=self.scrape)

        
    
    def scrape(self, response):
        item = WikipediaItem()
        item['product_name'] = response.xpath("//h2[@class='text-uppercase']/text()").get()
        item['member_price'] = response.xpath("//span[@class='text--orange']/text()").get()
        item['retail_price'] = response.xpath("//span[@class='text--orange']/text()")[1].get()

        yield item


