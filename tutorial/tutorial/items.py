import scrapy


class TItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class DmozItem(scrapy.Item):
    title = scrapy.Field()    # 标题
    link = scrapy.Field()     # 链接
    name = scrapy.Field()     # 简述
    posttime = scrapy.Field() # 发布时间