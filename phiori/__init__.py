import sys, os, traceback
import datetime, json, random, re, time, urllib.request, urllib.parse, yaml
from .shiori import *
from .phiori import *
from .collections import LiveDict, LiveJsonDict, LiveBsonDict, LivePersonaDict, PropertyDict

def load(path, _len):
	Phiori.configs = LivePersonaDict(os.path.join(path, "config.txt"))
	Phiori.resources = LivePersonaDict(os.path.join(path, "resource.txt"))
	Phiori.variables = LiveBsonDict(os.path.join(path, "variable.dat"))
	Phiori.words = LiveJsonDict(os.path.join(path, "words.dic"))
	Phiori.encoding = Phiori.configs.get("encoding", "utf-8")
	Phiori.objects = {
		#phiori variables
		"phiori": PropertyDict({
			"config": Phiori.configs,
			"encoding": Phiori.encoding,
			"info": Phiori.info,
			"locale": Phiori.locale,
			"path": path,
			"res": Phiori.resources,
			"temp": Phiori.temps,
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
		"yaml": yaml,
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
		"simulate": Phiori.simulate,
		"write": Phiori.write,
		"writeline": Phiori.writeline,
	}
	Phiori.objects["_"] = Phiori.objects["phiori"]
	Phiori.objects["P"] = Phiori.objects["phiori"]
	Phiori.temps["_boot"] = {}
	Phiori.temps["_boot"]["loaderr"] = []
	for filename in os.listdir(os.path.join(path, "phiori", "builtins")):
		if os.path.splitext(filename)[1] == ".py":
			try:
				with open(os.path.join(path, "phiori", "builtins", filename), "r", encoding=Phiori.encoding) as f:
					module = compile(f.read(), os.path.join(path, "phiori", "builtins", filename), "exec")
					exec(module, Phiori.objects)
			except:
				Phiori.temps["_boot"]["loaderr"].append(r"Error has occurred while loading builtin modules.\n\n" + r"{}".format(traceback.format_exc().replace("\\", "\\\\").replace("\n", r"\n\n[half]")))
	for filename in os.listdir(path):
		if os.path.splitext(filename)[1] == ".py":
			try:
				with open(os.path.join(path, filename), "r", encoding=Phiori.encoding) as f:
					module = compile(f.read(), os.path.join(path, filename), "exec")
					exec(module, Phiori.objects)
			except:
				Phiori.temps["_boot"]["loaderr"].append(r"Error has occurred while loading user modules.\n\n" + r"{}".format(traceback.format_exc().replace("\\", "\\\\").replace("\n", r"\n\n[half]")))
	return True

def unload():
	return True

def request(req, _len):
	req = Shiori.fromrequest(req)
	res = process(req)
	return str(res).encode(res.headers.get("Charset", Phiori.encoding))
