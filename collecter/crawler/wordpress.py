from option import *
from crawler import *
from crawler.rss import rss


class wordpress(blog):
	base: str
	rss_crawler: rss

	def __init__(self, **kwargs):
		self.__dict__.update(kwargs)
		self.rss_crawler = rss(**kwargs)
		self.rss_crawler.url = self.base + '/feed/rss2'

	async def fetch(self) -> Result[blog, str]:
		return await self.rss_crawler.fetch()