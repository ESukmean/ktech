from typing import Dict, Tuple
proto = {
	'get_blogs': {
		1: ({'base': 'https://blog.esukmean.com'}, )
	}
}

class Inner:
	pass

class DB:
	connection = Inner()
	def get_blogs(self, module_id: int) -> Tuple[Dict]:
		base = proto['get_blogs']
		if module_id not in base:
			return tuple()

		return base[module_id]

