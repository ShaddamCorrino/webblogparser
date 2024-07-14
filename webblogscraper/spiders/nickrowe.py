from typing import Any

import scrapy
from scrapy.http import Response


class NickRoweSpider(scrapy.Spider):
    name ="nickrowe"
    start_urls = ["http://worthwhile.typepad.com/worthwhile_canadian_initi/nick-rowe/"]

    def parse(self, response: Response, **kwargs: Any) -> Any:
        articles = response.css("div.entry-author-nick_rowe")

        for article in articles:
            link = article.css("h3.entry-header a::attr(href)").get()
            yield scrapy.Request(link, callback=self.parse_article)

        """next_page = response.css("span.pager-right a::attr(href)").get()
        if next_page:
            yield response.follow(next_page, self.parse)"""

    def parse_article(self, response: Response, **kwargs: Any) -> Any:
        article_title = response.css("h3.entry-header::text").get()
        article_content = response.css("div.entry-body").get()
        article_date = response.css("span.post-footers").get()
        yield {
            "title": article_title,
            "content": article_content.lstrip("<div class='entry-body'>").rstrip("</div>"),
            "date": article_date
        }

