from option import *
from crawler import *
import crawler
import db
import modules

MODULE_NAME = 'wp'

def get_blogs() -> Tuple[crawler.wordpress]:
	mid: Option[int] = modules.module_id(MODULE_NAME)
	blogs = mid.map_or(lambda mid: db.get_blogs(mid), tuple())

	return tuple(map(lambda info: crawler.wordpress(info), blogs))
