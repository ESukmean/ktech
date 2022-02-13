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

class article:
	title: str = ''
	article: str = ''
	post: datetime = None
	author: str = ''
	url: str = ''
	category: List[str] = []
	tag: Tuple[str] = ()

	def __init__(self, **kwargs) -> None:
		self.__dict__.update(kwargs)
	
	def get_summary(self) -> str:
		if 'article' not in self.__dict__:
			return ''

		article = _strip_tag_regex.sub('', self.article)
		import html

		return html.unescape(article)

	def get_tag(self) -> Tuple[str]:
		result = []

		if 'category' in self.__dict__:
			result.extend(self.category)
		
		article = self.get_summary()
		for tag, regex in _tag_keyword_re.items():
			if regex.find(article) == -1:
				continue
				
			result.append(tag)

		return tuple(result)
	
class blog:
	blog_id: int
	name: str
	link: str
	description: str

	article: List[article]

	def __init__(self, **kwargs):
		self.blog_id = 0
		self.name = ''
		self.link = ''
		self.description = ''
		self.article = list()

		self.__dict__.update(kwargs)
		
	async def fetch(self) -> List[article]:
		return []

	def add_article(self, article: 'article'):
		self.article.append(article)