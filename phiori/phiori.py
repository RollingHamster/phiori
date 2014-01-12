import sys, os, traceback
import random, locale, time
from types import GeneratorType
from collections import Iterable
from .shiori import Shiori

class Phiori:
	
	configs = {}
	encoding = "utf-8"
	handlers = {}
	info = {}
	locale = locale.getdefaultlocale()
	objects = {}
	resources = {}
	response = None
	temps = {}
	variables = None
	words = None

	def event(handler, *args, **kwargs):
		try:
			res = handler(*args, **kwargs)
			if isinstance(res, Iterable):
				for r in res:
					Phiori.response[0] += str(r)
			elif res:
				Phiori.response[0] += str(res)
		except:
			Phiori.response[0] = r"\0\b2\_q{}\x\c\e".format(traceback.format_exc().replace("\\", "\\\\").replace("\n", r"\n\n[half]"))
	
	@staticmethod
	def handle(*events):
		def decorator(func):
			for event in events:
				if not Phiori.handlers.get(event):
					Phiori.handlers[event] = []
				Phiori.handlers[event].append(func)
			def wrapper(*args, **kwargs):
				Phiori.event(func, *args, **kwargs)
			return wrapper
		return decorator
	
	@staticmethod
	def print(*objects, sep=" ", end=r"\n"):
		for i, o in enumerate(objects):
			Phiori.response[0] += str(o) + (sep if i < len(objects) - 1 else "")
		Phiori.response[0] += end
	
	@staticmethod
	def simulate(name, *args):
		headers = {"ID": name}
		for i, arg in enumerate(args):
			headers["Reference" + str(i)] = arg
		request = Shiori.makerequest("phiori/ego", headers=headers)
		return process(request).headers.get("Value", "")
	
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
		Phiori.response[0] += text.format(*args, **kwargs)
	
	@staticmethod
	def writeline(text, *args, **kwargs):
		write(text + r"\n", *args, **kwargs)

def process(req):
	res = Shiori.makeresponse(Phiori.info.get("ownerghostname", ("phiori/persona", ))[0], 204)
	resid = "#res:{}:{:07}".format(hex(int(time.time())), random.randint(0, 9999999))
	Phiori.temps[resid] = [""]
	if "#res.stack" not in Phiori.temps:
		Phiori.temps["#res.stack"] = []
	Phiori.temps["#res.stack"].append(Phiori.response)
	Phiori.response = Phiori.temps[resid]
	if req.method == "GET":
		key = req.headers.get("ID")
		if key:
			value = {}
			for k, v in req.headers.items():
				if k.startswith("Reference"):
					value[int(k[9:])] = v
			Phiori.info[key] = value
		res = Shiori.makeresponse(Phiori.info.get("ownerghostname", ("phiori/persona", ))[0])
		ss = None
		if req.headers.get("ID", "").startswith("On") and req.headers.get("ID") in Phiori.handlers:
			for handler in Phiori.handlers[req.headers.get("ID")]:
				try:
					Phiori.event(handler, **req.headers)
				except:
					Phiori.response = Phiori.temps["#res.stack"].pop()
					res.headers["Value"] = r"\0\b2\_q{}\x\c\e".format(traceback.format_exc().replace("\\", "\\\\").replace("\n", r"\n\n[half]"))
					return res
			if Phiori.response[0]:
				res = Shiori.makeresponse(Phiori.info.get("ownerghostname", ("phiori/persona", ))[0], 200)
				res.headers["Value"] = Phiori.response[0]
		elif req.headers.get("ID") and req.headers.get("ID") in Phiori.resources:
			res.headers["Value"] = Phiori.resources[req.headers.get("ID")]
		else:
			res = Shiori.makeresponse(Phiori.info.get("ownerghostname", ("phiori/persona", ))[0], 204)
	elif req.method == "NOTIFY":
		key = req.headers.get("ID")
		if key:
			value = {}
			for k, v in req.headers.items():
				if k.startswith("Reference"):
					value[int(k[9:])] = v
			Phiori.info[key] = value
			res = Shiori.makeresponse(Phiori.info.get("ownerghostname", ("phiori/persona", ))[0], 204)
	del Phiori.temps[resid]
	Phiori.response = Phiori.temps["#res.stack"].pop()
	return res
