from option import *
from crawler import rss, blog
import aiohttp
from defusedxml.ElementTree import parse


class wordpress(blog):
	base: str
	rss_crawler: rss

	def __init__(self, **kwargs):
		self.__dict__.update(kwargs)
		self.rss_crawler = rss(kwargs)
		self.rss_crawler.url = self.base + '/feed/rss2'

	async def fetch(self) -> Result[blog]:
		return await self.rss_crawler.fetch()