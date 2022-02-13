from datetime import datetime
from typing import *
import re

_tag_keyword_re = {
	'network': re.compile('network|ip|packet'),
	'web': re.compile('html|css|javascript|js'),
	'android': re.compile('android|안드로이드'),
	'ios': re.compile('iphone|ipad|ios')
}
_strip_tag_regex = re.compile('<.*?>')

class Article:
	title: str = ''
	article: str = ''
	post: datetime = None
	author: str = ''
	url: str = ''
	category: List[str] = []
	tag: Tuple[str] = ()

	def __init__(self, **kwargs) -> None:
		self.__dict__.update(kwargs)
	
	def get_clean_article(self) -> str:
		if 'article' not in self.__dict__:
			return ''

		article = _strip_tag_regex.sub('', self.article)
		import html
		return html.unescape(article)

	def get_summary(self) -> str:
		return self.get_clean_article()

	def get_tag(self) -> Tuple[str]:
		result = []

		if 'category' in self.__dict__:
			result.extend(self.category)
		
		article = self.get_summary()
		for tag, regex in _tag_keyword_re.items():
			if regex.search(article) is None:
				continue
				
			result.append(tag)

		return tuple(result)
	
class Blog:
	blog_id: int
	name: str
	link: str
	description: str

	article: List[Article]

	def __init__(self, **kwargs):
		self.blog_id = 0
		self.name = ''
		self.link = ''
		self.description = ''
		self.article = list()

		self.__dict__.update(kwargs)
		
	async def fetch(self) -> List[Article]:
		return []

	def add_article(self, article: Article):
		self.article.append(article)