from option import *
from modules import wp, rss

MODULE_ID = {
	'wp': 1,
	'rss': 2
}
REGISTERED_MODULE = (
	wp.get_blogs,
	rss.get_blogs
)

def module_id(module_name: str) -> Option[int]:
	if module_name not in module_id:
		return None
	
	return Some(module_id[module_name])