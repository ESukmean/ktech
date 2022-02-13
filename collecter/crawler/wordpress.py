from option import *
from crawler import *
from crawler.rss import Rss

class Wordpress(Blog):
	base: str
	rss_crawler: Rss

	def __init__(self, **kwargs):
		super().__init__() 
		self.__dict__.update(kwargs)
		self.rss_crawler = Rss(**kwargs)
		self.rss_crawler.url = self.base + '/feed/rss2'

	async def fetch(self) -> Result[Blog, str]:
		blog_obj = await self.rss_crawler.fetch()
	
		if blog_obj.is_err:
			return blog_obj

		blog_obj: Blog = blog_obj.unwrap()
		for index, article in enumerate(blog_obj.article):
			article: Article = article
			article.article = article.get_clean_article()
			pos = article.article.find('... Continue Reading →')
			if pos == -1:
				continue

			clean_article = article.article[:pos]
			blog_obj.article[index].article = clean_article

		return Ok(blog_obj)
			
