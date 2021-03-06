from option import *
from typing import *
from crawler.wordpress import Wordpress
import db
import modules

MODULE_NAME = 'wp'

def get_blogs() -> Tuple[Wordpress]:
	mid: Option[int] = modules.module_id(MODULE_NAME)
	
	db_manager = db.DB()
	blogs = mid.map_or(lambda mid: db_manager.get_blogs(mid), tuple())

	return tuple(map(lambda info: Wordpress(**info), blogs))
