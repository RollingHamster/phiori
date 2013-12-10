import sys, os
from collections import Iterable

class LiveDict(dict):
	
	def __init__(self, file, *args, **kwargs):
		self.filename = file
		if os.path.exists(file):
			with open(self.filename, "r", encoding=sys.getdefaultencoding()) as f:
				self.update(eval(f.read()))
		else:
			self.clear()
			self.update(*args, **kwargs)
	
	def _live(func):
		def wrap(self, *args, **kwargs):
			result = func(self, *args, **kwargs)
			with open(self.filename, "w", encoding=sys.getdefaultencoding()) as f:
				f.write(self.__str__())
			return result
		return wrap
	
	__setitem__ = _live(dict.__setitem__)
	__delitem__ = _live(dict.__delitem__)
	clear = _live(dict.clear)
	pop = _live(dict.pop)
	popitem = _live(dict.popitem)
	setdefault = _live(dict.setdefault)
	update = _live(dict.update)
