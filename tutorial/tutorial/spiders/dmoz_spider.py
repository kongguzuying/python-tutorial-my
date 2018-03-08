from scrapy.spider import Spider
from tutorial.items import DmozItem
from tutorial.dao import ArticleDao


class DmozSpider(Spider):
    name = "huxiu"
    allowed_domains = ["www.oschina.net"]
    start_urls = [
        "http://www.oschina.net"
    ]

    def parse(self, response):
        dao = ArticleDao()
        for sel in response.xpath('//div[@class="page"]/div[@class="box vertical news"]'):
            item = DmozItem()
            item['title'] = sel.xpath('a/text()')[0].extract()
            item['link'] = sel.xpath('a/@href')[0].extract()
            item['name'] = sel.xpath('a/@title')[0].extract()
            print('标题：', item['title'], '地址：', item['link'], '描述：', item['name'])

            dao.add_article(item)