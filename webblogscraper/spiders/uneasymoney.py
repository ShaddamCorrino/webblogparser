import scrapy
from typing import Any
from scrapy.http import Response

class UneasyMoneySpider(scrapy.Spider):
    name = "david-glasner"
    starting_page = 1
    ending_page = 1
    base_url = "https://uneasymoney.com/page/{}/"
    def start_requests(self):
        for i in range(self.starting_page, self.ending_page + 1):
            url = self.base_url.format(i)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response: Response, **kwargs: Any) -> Any:
        articles = response.css("div.status-publish")
        for article in articles:
            link = article.css("div.entry-head h3.entry-title a::attr(href)").get()
            title = article.css("div.entry-head h3.entry-title a::text").get()
            publish_date = article.css("div.entry-head small.entry-meta span.chronodata "
                                       "abbr.published::attr(title)").get()
            content = article.css("div.entry-content").get()

            yield {
                "link": link,
                "title": title,
                "publish_date": publish_date,
                "content": content[:50]
            }
