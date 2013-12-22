import sys, os, traceback
import datetime, json, locale, random, re, time, urllib.request, urllib.parse
from .shiori import *
from .phiori import *
from .collections import LiveDict, LiveJsonDict, PropertyDict

def load(path, _len):
	Phiori.variables = LiveDict(os.path.join(path, "variable.dat"))
	Phiori.words = LiveJsonDict(os.path.join(path, "words.dic"))
	Phiori.objects = {
		#phiori variables
		"phiori": PropertyDict({
			"config": Phiori.configs,
			"encoding": sys.getdefaultencoding(),
			"info": Phiori.info,
			"locale": locale.getdefaultlocale(),
			"path": path,
			"res": Phiori.resources,
			"var": Phiori.variables,
			"words": Phiori.words,
		}),
		#imports
		"datetime": datetime,
		"json": json,
		"os": os,
		"random": random,
		"re" : re,
		"sys": sys,
		"time": time,
		"urllib": urllib,
		#builtin functions
		"abs": abs,
		"all": all,
		"any": any,
		"ascii": ascii,
		"bin": bin,
		"bool": bool,
		"bytearray": bytearray,
		"bytes": bytes,
		"callable": callable,
		"chr": chr,
		"classmethod": classmethod,
		"compile": compile,
		"delattr": delattr,
		"dict": dict,
		"dir": dir,
		"divmod": divmod,
		"enumerate": enumerate,
		"eval": eval,
		"exec": exec,
		"filter": filter,
		"float": float,
		"format": format,
		"frozenset": frozenset,
		"getattr": getattr,
		"globals": globals,
		"hasattr": hasattr,
		"hash": hash,
		"help": help,
		"hex": hex,
		"id": id,
		"input": input,
		"int": int,
		"isinstance": isinstance,
		"issubclass": issubclass,
		"iter": iter,
		"len": len,
		"list": list,
		"locals": locals,
		"map": map,
		"max": max,
		"memoryview": memoryview,
		"min": min,
		"next": next,
		"object": object,
		"oct": oct,
		"open": open,
		"ord": ord,
		"pow": pow,
		"property": property,
		"range": range,
		"repr": repr,
		"reversed": reversed,
		"round": round,
		"set": set,
		"setattr": setattr,
		"slice": slice,
		"sorted": sorted,
		"staticmethod": staticmethod,
		"str": str,
		"sum": sum,
		"super": super,
		"tuple": tuple,
		"type": type,
		"vars": vars,
		"zip": zip,
		"__import__": __import__,
		#phiori functions
		"handle": Phiori.handle,
		"print": Phiori.print,
		"write": Phiori.write,
		"writeline": Phiori.writeline,
	}
	Phiori.objects["_"] = Phiori.objects["phiori"]
	Phiori.objects["P"] = Phiori.objects["phiori"]
	Phiori.variables["_boot"] = {}
	Phiori.variables["_boot"]["loaderr"] = []
	for filename in os.listdir(os.path.join(path, "phiori", "builtins")):
		if os.path.splitext(filename)[1] == ".py":
			try:
				with open(os.path.join(path, "phiori", "builtins", filename), "r", encoding=sys.getdefaultencoding()) as f:
					module = compile(f.read(), os.path.join(path, "phiori", "builtins", filename), "exec")
					exec(module, Phiori.objects)
			except:
				Phiori.variables["_boot"]["loaderr"].append(r"{}".format(traceback.format_exc().replace("\\", "\\\\").replace("\n", r"\n\n[half]")))
	for filename in os.listdir(path):
		if os.path.splitext(filename)[1] == ".py":
			try:
				with open(os.path.join(path, filename), "r", encoding=sys.getdefaultencoding()) as f:
					module = compile(f.read(), os.path.join(path, filename), "exec")
					exec(module, Phiori.objects)
			except:
				Phiori.variables["_boot"]["loaderr"].append(r"{}".format(traceback.format_exc().replace("\\", "\\\\").replace("\n", r"\n\n[half]")))
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
				except:
					exc_type, exc_value, exc_traceback = sys.exc_info()
					Phiori.response = ""
					res.headers["Value"] = r"\0\b2\_q{}\x\c\e".format(traceback.format_exc().replace("\\", "\\\\").replace("\n", r"\n\n[half]"))
					return str(res)
		elif req.headers.get("ID") and req.headers.get("ID") in Phiori.resources:
			res.headers["Value"] = Phiori.resources[req.headers.get("ID")]
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
