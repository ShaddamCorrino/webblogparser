from typing import Any

import scrapy
from scrapy.http import Response


class EconlibParser(scrapy.Spider):
    name = "econlib"

    def parse(self, response: Response, **kwargs: Any) -> Any:
        return NotImplemented
