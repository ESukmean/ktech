import asyncio
from typing import *
import modules
import crawler
import db

async def main():
	while True:
		rm = modules.REGISTERED_MODULE

		blog_list: List[crawler.blog] = list()
		fetch_task: List = list()
		for get_func in rm:
			blogs: Tuple[crawler.blog] = get_func()

			# create task를 사용한 순간 background에서 작업이 시작됨
			# await를 하는건 main으로 join을 하기 위함	
			fetch_task.extend(map(lambda b: asyncio.create_task(b.fetch()), blogs))
			blog_list.extend(blogs)

		for task in zip(fetch_task, blog_list):
			result = await task[0]
			print(result)

		await asyncio.sleep(60 * 10)


asyncio.run(main())
	