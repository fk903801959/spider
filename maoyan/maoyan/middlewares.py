# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from fake_useragent import UserAgent

class UserAgentMiddleware:
    def process_request(self, request, spider):
        request.headers.setdefault(b'User-Agent', UserAgent().random)

