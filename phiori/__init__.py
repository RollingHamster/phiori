import sys, os
import json, locale, random, re, time, urllib.request, urllib.parse
from .shiori import *
from .phiori import *
from .collections import LiveDict, LiveJsonDict

def load(path, _len):
	Phiori.variables = LiveDict(os.path.join(path, "variable.dat"))
	Phiori.words = LiveJsonDict(os.path.join(path, "words.dic"))
	Phiori.objects = {
		"config": Phiori.configs,
		"encoding": sys.getdefaultencoding(),
		"locale": locale.getdefaultlocale(),
		"handle": Phiori.handle,
		"info": Phiori.info,
		"json": json,
		"os": os,
		"path": path,
		"print": Phiori.print,
		"random": random,
		"re" : re,
		"res": Phiori.resources,
		"sys": sys,
		"time": time,
		"urllib": urllib,
		"var": Phiori.variables,
		"words": Phiori.words,
		"write": Phiori.write,
		"writeline": Phiori.writeline,
	}
	for filename in os.listdir(os.path.join(path, "phiori", "builtins")):
		if filename.endswith(".py"):
			try:
				with open(os.path.join(path, "phiori", "builtins", filename), "r", encoding=sys.getdefaultencoding()) as f:
					exec(f.read(), Phiori.objects)
			except ex:
				pass
	for filename in os.listdir(path):
		if filename.endswith(".py"):
			try:
				with open(os.path.join(path, filename), "r", encoding=sys.getdefaultencoding()) as f:
					exec(f.read(), Phiori.objects)
			except ex:
				pass
	return True

def unload():
	try:
		Phiori.objects["saveconfig"]()
	except:
		pass
	return True

def request(req, _len):
	req = Shiori.fromrequest(req)
	res = Shiori.makeresponse("phiori", 204)
	if req.method == "GET":
		res = Shiori.makeresponse("phiori")
		ss = None
		if req.headers.get("ID", "").startswith("On") and req.headers.get("ID") in Phiori.handlers:
			for handler in Phiori.handlers[req.headers.get("ID")]:
				try:
					ss = Phiori.event(handler, **req.headers)
					if ss:
						res.headers["Value"] = str(ss)
					elif Phiori.response:
						res.headers["Value"] = Phiori.response
					Phiori.response = ""
				except ex:
					Phiori.response = ""
					res.headers["Value"] = r"{}\n\n{}".format(str(handler), str(ex))
					return str(res)
		elif req.headers.get("ID") and req.headers.get("ID") in Phiori.resources:
			res.headers["Value"] = Phiori.resources["ID"]
		else:
			res = Shiori.makeresponse("phiori", 204)
	elif req.method == "NOTIFY":
		key = req.headers.get("ID")
		if key:
			value = {}
			for k, v in req.headers.items():
				if k.startswith("Reference"):
					value[int(k[9:])] = v
			Phiori.info[key] = value
			res = Shiori.makeresponse("phiori", 204)
	return str(res)
