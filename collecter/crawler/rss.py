from option import *
from crawler import blog, article
import aiohttp
from defusedxml.ElementTree import parse
import datetime

class rss(blog):
	base: str

	def __init__(self, **kwargs):
		self.__dict__.update(kwargs)
	

	async def fetch(self) -> Result[blog]:
		try:
			async with aiohttp.ClientSession() as session:
				headers = {
					
				}

				async with session.get(self.base + '/feed/rss2', headers = headers) as response:
					if response.status != 200:
						return Err(f'status code != 200 ({self.base}/feed/rss2)')

					body = await response.text()
					et = parse(body)

					root = et.get_root()
					
					title = root.get('title', '')
					link = root.get('link', self.base + '/feed/rss2')
					description = root.get('description', '')

					crawl_result = blog(title = title, link = link, description = description)
					for child in root.findall('item'):
						title = child.get('title', '')
						url = child.get('link', self.base)
						author = child.get('dc:creator', None)
						category = tuple(map(lambda el: el.text, child.findall('category')))
						description = child.get('description', '')

						item = article(title = title, url = url, author = author, category = category, description = description)
						
						post = child.get('pubDate')
						if post is not None:
							pubDT = datetime.datetime.strptime(post, '%Y-%m-%d %H:%M:%S')
							item.post = pubDT

						crawl_result.add_article(item)

					return Ok(crawl_result)


		except Exception as e:
			return Err('Error while fetch' + str(e))
				
