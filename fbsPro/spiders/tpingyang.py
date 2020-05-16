# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider

"""太平洋全站分类数据 """
class TpingyangSpider(RedisCrawlSpider):
    name = 'tpingyang'
    # start_urls = ['https://product.pconline.com.cn/category.html']
    redis_key = 'tpingyangQueue'

    rules = (
        # 1、提取所有分类的url并请求，到达每一个小分类的页面,并且跟踪
        Rule(LinkExtractor(restrict_xpaths='//div[@class="list-detail"]/a'),callback="type_url",follow=True),
        # 2、小分类有多个页面，这里要翻页功能，并且跟踪
        Rule(LinkExtractor(restrict_xpaths='//div[@class="pager"]/a'), callback="page_url", follow=True),
        # 3、继续进一层，到达该小分类的每个商品的详情页
        Rule(LinkExtractor(restrict_xpaths='//div[@class="item-wrap"]/div[1]/a'), callback='parse_detail'),
    )

    def type_url(self, response):
        print("种类url")

    def page_url(self,response):
        print("页码url")

    def parse_detail(self, response):
        print('数据')
        # item = {}
        # item['goods_name'] = response.xpath('//div[@class="pro-info"]//h1/text()').extract_first().strip()
        # # translate(str.maketrans('','','大全'))删除字符串的指定文字，python3.6之后可直接调用，不需要用正则的sub
        # item['goods_type'] = response.xpath('//div[@class="crumb"]/a[3]/text()').extract_first().translate(str.maketrans('','','大全'))
        # rank = response.xpath('//*[@id="JweekRank"]/a/i[1]/text()').extract_first()
        # if rank:
        #     item['rank'] = '本周排名:' + rank
        # goods_price= response.xpath('//i[@class="r-price"]/a/text()').extract_first()
        # item['goods_price'] = '暂未标价'
        # if goods_price.isdecimal():
        #     item['goods_price'] = '￥' + goods_price
        # item['goods_price_trend'] = '价格波动未知'
        # goods_price_trend = response.xpath('//span[@class="level stable"]/text()').extract_first()
        # if goods_price_trend:
        #     item['goods_price_trend'] = '价格波动' + goods_price_trend
        # item['pic_url'] = 'http:' + response.xpath('//*[@id="JareaTop"]/div[1]/div[1]/a[1]/img/@src').extract_first()
        # goods_content = response.xpath('//span[@class="pro-des-span"]/text() | //p[@class="keyparams-text"]/text()').extract()
        # item['goods_content'] = ''.join(goods_content).strip().replace('\r','').replace('\n','')
        # print(item)
        # yield item
