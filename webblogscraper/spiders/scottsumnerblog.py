from typing import Any

import scrapy
from scrapy.http import Response


class MoneyIllusionParser(scrapy.Spider):
    name = "money_illusion"
    start_urls = ["https://www.themoneyillusion.com/"]

    def parse(self, response: Response, **kwargs: Any) -> Any:
        articles = response.css("div.post")
        for article in articles:
            title = article.css("h1 a").get()
            link = article.css("h1 a::attr(href)").get()
            content = article.css("div.entry").get()
            yield {
                "title": title,
                "link": link,
                "content": content
            }
        next_page = response.css("div.pagenavigation2 div.alignright a::attr(href)")
        if next_page:
            yield response.follow(next_page, self.parse)