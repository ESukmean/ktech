from option import *
from typing import *
from crawler.rss import Rss
import db
import modules

MODULE_NAME = 'rss'

def get_blogs() -> Tuple[Rss]:
	mid: Option[int] = modules.module_id(MODULE_NAME)
	db_manager = db.DB()
	blogs = mid.map_or(lambda mid: db_manager.get_blogs(mid), tuple())

	return tuple(map(lambda info: Rss(info), blogs))
