from option import *
from crawler import *
import crawler
import db
import modules

MODULE_NAME = 'rss'

def get_blogs() -> Tuple[crawler.rss]:
	mid: Option[int] = modules.module_id(MODULE_NAME)
	blogs = mid.map_or(lambda mid: db.get_blogs(mid), tuple())

	return tuple(map(lambda info: crawler.rss(info), blogs))
