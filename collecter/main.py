import asyncio
from typing import *
from option import *
import modules
import crawler
import db

async def main():
	while True:
		rm = modules.REGISTERED_MODULE

		blog_list: List[crawler.Blog] = list()
		fetch_task: List = list()
		for get_func in rm:
			blogs: Tuple[crawler.Blog] = get_func()

			# create task를 사용한 순간 background에서 작업이 시작됨
			# await를 하는건 main으로 join을 하기 위함	
			fetch_task.extend(map(lambda b: asyncio.create_task(b.fetch()), blogs))
			blog_list.extend(blogs)

		for task in zip(fetch_task, blog_list):
			result: Result[crawler.Blog, str] = await task[0]
			if result.is_err:
				print('err', result)
				continue

			result: crawler.Blog = result.unwrap()
			print('blog:', result.name)
			for article in result.article:
				article: crawler.Article = article
				print('*', article.title, article.get_tag(), article.get_summary())


		await asyncio.sleep(60 * 10)


asyncio.run(main())
	