import sys, os, traceback
from collections import Iterable

class Phiori:
	
	configs = {}
	handlers = {}
	info = {}
	objects = {}
	resources = {}
	response = ""
	variables = None
	words = None
	
	@staticmethod
	def event(handler, *args, **kwargs):
		result = ""
		try:
			response = handler(*args, **kwargs)
			if isinstance(response, Iterable):
				for res in handler(*args, **kwargs):
					result += str(res)
			else:
				result = response
				if result:
					result = str(result)
		except:
			exc_type, exc_value, exc_traceback = sys.exc_info()
			result = r"\0\b2\_q{}\x\c\e".format(traceback.format_exc().replace("\\", "\\\\").replace("\n", r"\n\n[half]"))
		return result
	
	@staticmethod
	def handle(event):
		def decorator(func):
			if not Phiori.handlers.get(event):
				Phiori.handlers[event] = []
			Phiori.handlers[event].append(func)
			def wrapper(*args, **kwargs):
				return Phiori.event(func, *args, **kwargs)
			return wrapper
		return decorator
	
	@staticmethod
	def print(*objects, sep=" ", end=r"\n"):
		for i, o in enumerate(objects):
			Phiori.response += str(o) + (sep if i < len(objects) - 1 else "")
		Phiori.response += end
	
	@staticmethod
	def write(text, *args, **kwargs):
		Phiori.response += text.format(*args, **kwargs)
	
	@staticmethod
	def writeline(text, *args, **kwargs):
		Phiori.response += text.format(*args, **kwargs) + r"\n"
