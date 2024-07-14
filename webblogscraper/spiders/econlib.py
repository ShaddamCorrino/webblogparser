from typing import Any

import scrapy
from scrapy.http import Response


class EconlibParser(scrapy.Spider):
    name = "econlib"
    start_urls = ["https://www.econlib.org/econlog/econlog-archive/?orderby=date&order=desc"]
    counter = 0
    max_limit = 428

    def parse(self, response: Response, **kwargs: Any) -> Any:
        self.counter += 1
        articles = response.css("div.econarch-items")
        for article in articles:
            link = article.css("div.pad-right h4 a::attr(href)").get()
            author = article.css("div.pad-right p.econ_mr_author strong::text").get()
            if author == "By Scott Sumner":
                yield scrapy.Request(link, callback=self.parse_article)

        next_page = response.css("a.next::attr(href)").get()
        if next_page and self.counter < self.max_limit:
            yield response.follow(next_page, self.parse)

    def parse_article(self, response: Response, **kwargs: Any) -> Any:
        date = response.css("div.article-info p::text")[1].get()
        article_title = response.css("h1.post-title::text").get()
        article_author = response.css("span.pp-author-boxes-name a::text").get()
        article_content = response.css("div.post-content").get()

        yield {
            "date": date,
            "title": article_title,
            "author": article_author,
            "content": article_content
        }
