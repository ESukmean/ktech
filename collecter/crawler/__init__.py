from datetime import datetime
from typing import *

class article:
	title: str
	article: str
	post: datetime
	author: str
	url: str
	category: List[str]
	tag: Tuple[str]

	def __init__(self, **kwargs) -> None:
		self.__dict__.update(kwargs)
		
	def get_summary(self) -> str:
		pass

	def get_tag(self) -> Tuple[str]:
		pass
	
	
class blog:
	blog_id: int
	name: str
	link: str
	description: str

	article: List[article]

	def __init__(self, **kwargs):
		self.__dict__.update(kwargs)
		
	async def fetch(self) -> List[article]:
		pass

	async def add_article(self, article: 'article'):
		self.article.append(article)