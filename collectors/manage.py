import os
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from .collectors.spiders import CRAWLERS
from .collectors import settings

class CrawlerManager():

    def __init__(self):
        settings_file_path = 'collectors.collectors.settings'
        os.environ.setdefault('SCRAPY_SETTINGS_MODULE', settings_file_path)
        self.process = CrawlerProcess(get_project_settings())

    def start(self, crawler_name, *args, **kwargs):
        MySpider = CRAWLERS[crawler_name]
        if MySpider != None:
            self.process.crawl(MySpider, *args, **kwargs)
            self.process.start()