import sys, os, traceback
import random
from collections import Iterable

class Phiori:
	
	configs = {}
	handlers = {}
	info = {}
	objects = {}
	resources = {}
	response = ""
	temps = {}
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
	def handle(*events):
		def decorator(func):
			for event in events:
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
		args = list(args)
		if isinstance(text, list) or isinstance(text, tuple) or isinstance(text, set):
			text = random.choice(text)
		elif isinstance(text, dict):
			text = random.choice(text.items())
		if args:
			for i, a in enumerate(args):
				if isinstance(a, list) or isinstance(a, tuple) or isinstance(a, set):
					args[i] = random.choice(a)
				elif isinstance(a, dict):
					args[i] = random.choice(a.items())
		if kwargs:
			for k, v in kwargs.items():
				if isinstance(v, list) or isinstance(v, tuple) or isinstance(v, set):
					kwargs[k] = random.choice(v)
				elif isinstance(v, dict):
					kwargs[k] = random.choice(v.items())
		Phiori.response += text.format(*args, **kwargs)
	
	@staticmethod
	def writeline(text, *args, **kwargs):
		write(text + r"\n", *args, **kwargs)
