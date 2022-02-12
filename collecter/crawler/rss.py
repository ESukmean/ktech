from option import *
from crawler import blog, article
import aiohttp
from defusedxml.ElementTree import fromstring as xml_fromstring
import datetime

class rss(blog):
	base: str

	def __init__(self, **kwargs):
		self.__dict__.update(kwargs)
	

	async def fetch(self) -> Result[blog, str]:
		try:
			async with aiohttp.ClientSession() as session:
				headers = {
					'user-agent': 'Mozilla/5.0 (compatible; KTech; +https://github.com/ESukmean/ktech)'
				}

				async with session.get(self.base + '/feed/rss2', headers = headers) as response:
					if response.status != 200:
						return Err(f'status code != 200 ({self.base}/feed/rss2)')

					body = await response.text()
					root = xml_fromstring(body).find('channel')
					if root is None:
						return Err('not rss2 feed')

					title = Option.maybe(root.find('title')).map(lambda e: e.text).unwrap_or('')
					link = Option.maybe(root.find('link')).map(lambda e: e.text).unwrap_or('')
					description = Option.maybe(root.find('description')).map(lambda e: e.text).unwrap_or('')
					
					print(root.attrib)

					crawl_result = blog(title = title, link = link, description = description)
					for child in root.findall('item'):
						title = Option.maybe(child.find('title')).map(lambda e: e.text).unwrap_or('')
						url = Option.maybe(child.find('link')).map(lambda e: e.text).unwrap_or(self.base)
						author = Option.maybe(child.find('dc:creator')).map(lambda e: e.text).unwrap_or('')
						category = tuple(map(lambda el: el.text, child.findall('category')))
						description = Option.maybe(child.find('description')).map(lambda e: e.text).unwrap_or('')

						item = article(title = title, url = url, author = author, category = category, description = description)
						print(title, url, author, category, description)

						post = child.find('pubDate')
						if post is not None:
							pubDT = datetime.datetime.strptime(post.text, '%a, %d %b %Y %H:%M:%S %z')
							item.post = pubDT
						
						crawl_result.add_article(item)

					return Ok(crawl_result)


		except Exception as e:
			return Err('Error while fetch' + str(e))
				
