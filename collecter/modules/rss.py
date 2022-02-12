from option import *
from typing import *
from crawler.rss import rss
import db
import modules

MODULE_NAME = 'rss'

def get_blogs() -> Tuple[rss]:
	mid: Option[int] = modules.module_id(MODULE_NAME)
	db_manager = db.db()
	blogs = mid.map_or(lambda mid: db_manager.get_blogs(mid), tuple())

	return tuple(map(lambda info: rss(info), blogs))
