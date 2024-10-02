# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json

class WebblogscraperPipeline:
    def process_item(self, item, spider):
        return item


class MoneyIllusionPipeline:
    ID = 1
    def process_item(self, item, spider):
        with open(f"{self.ID}.json", "w") as file:
            json.dump(item, file)
        self.ID = self.ID + 1
