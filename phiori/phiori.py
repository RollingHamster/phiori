import sys, os
from collections import Iterable

class Phiori:
	
	configs = {}
	handlers = {}
	info = {}
	objects = {}
	resources = {}
	response = ""
	variables = None
	
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
	def event(handler, *args, **kwargs):
		result = ""
		response = handler(*args, **kwargs)
		if isinstance(response, Iterable):
			for res in handler(*args, **kwargs):
				result += res
		else:
			result = response
		return result
	
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
