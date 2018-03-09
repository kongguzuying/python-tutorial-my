from scrapy.spider import Spider
from tutorial.items import DmozItem
from tutorial.dao import ArticleDao

import os
import scrapy

image_urls = set()
download_images = set()


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

            link = item['link']
            print('link:', link)
            next_url = response.urljoin(link)
            request = scrapy.Request(next_url, callback=self.parse_item, errback=self.parse_error)
            yield request

    def parse_item(self, response):
        global image_urls
        for sel in response.xpath('//img'):
            image_url = sel.xpath('@src')[0].extract()
            if image_url.startswith('http') and (image_url.endswith('jpg') or image_url.endswith('png')):
                image_urls.add(image_url)
                print('image_url:', image_url)

        dao = ArticleDao()
        need_download_images = image_urls - download_images
        for image_url in need_download_images:
            dao.save_img(image_url, os.path.basename(image_url))
            download_images.add(image_url)

    def parse_error(self, failed):
        print('failed')
