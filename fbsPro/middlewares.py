# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import random

from scrapy import signals


class FbsproSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class FbsproDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        """这儿加ip代理"""'西祠的很多不能用我日'
        # proxy_list = ['http://125.123.155.19:3000',
        #               'https://125.126.112.177:60004',
        #               'http://125.126.109.80:60004',
        #               'https://125.126.98.3:60004',
        #               'http://60.179.230.193:3000',
        #               'http://120.79.139.253:8080',
        #               'http://60.179.254.211:3000',
        #               'https://182.108.45.238:1624',]
        # request.meta['proxy'] = random.choice(proxy_list)
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # 一般我们会用random.choice(代理池列表)
        # request.meta['proxy'] = 'http://60.189.192.228:3000'
        # return request  # 重新发送修正后的请求
        pass

    """————————————————
    版权声明：本文为CSDN博主「The_shy等风来」的原创文章，遵循CC
    4.0
    BY - SA版权协议，转载请附上原文出处链接及本声明。
    原文链接：https://blog.csdn.net/qq_37623764/article/details/105476058"""

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
