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
        Rule(LinkExtractor(restrict_xpaths='//div[@class="list-detail"]/a'),follow=True),
        # 2、小分类有多个页面，这里要翻页功能，并且跟踪
        Rule(LinkExtractor(restrict_xpaths='//div[@class="pager"]/a'),follow=True),
        # 3、继续进一层，到达该小分类的每个商品的详情页
        Rule(LinkExtractor(restrict_xpaths='//div[@class="item-wrap"]/div[1]/a'), callback='parse_detail'),
    )

    def parse_detail(self, response):
        item = {}
        item['goods_name'] = response.xpath('//div[@class="pro-info"]//h1/text()').extract_first().strip()
        # translate(str.maketrans('','','大全'))删除字符串的指定文字，python3.6之后可直接调用，不需要用正则的sub
        item['goods_type'] = response.xpath('//div[@class="crumb"]/a[3]/text()').extract_first().translate(str.maketrans('','','大全'))
        score = response.xpath('//a[@class="p-comment fl"]/span[@class="p-c-score"]/text()').extract_first()
        item['score'] = '暂无评分'
        if score:
            item['score'] = '评分' + score
        goods_price= response.xpath('//i[@class="r-price"]/a//text() | //em[@class="r-price fc-red"]//text()').extract()
        goods_price = ''.join(goods_price).replace(' ','').strip()
        item['goods_price'] = '暂无报价'
        if goods_price:
            item['goods_price'] = goods_price
        item['goods_price_trend'] = '价格波动未知'
        goods_price_trend = response.xpath('//span[@class="level stable"]/text()').extract_first()
        if goods_price_trend:
            item['goods_price_trend'] = '价格' + goods_price_trend
        pic_url = response.xpath('//div[@class="big-pic"]/a//img/@src').extract_first()
        if pic_url:
            item['pic_url'] = 'http:' + pic_url
        goods_content = response.xpath('//span[@class="pro-des-span"]/text() | //div[@class="b-tb ovh"]//p/text()').extract()
        item['goods_content'] = '该商品无相关介绍'
        if goods_content:
            item['goods_content'] = ''.join(goods_content).strip().replace('\r','').replace('\n','').replace(' ','')
        print(item)
        yield item
