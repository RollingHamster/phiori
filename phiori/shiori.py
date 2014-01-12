import sys, os, locale
from collections import OrderedDict

class Shiori:
	
	VERSION3 = "SHIORI/3.0"
	VERSION2 = "SHIORI/2.5"
	
	def __init__(self):
		pass
	
	@staticmethod
	def fromrequest(req, encoding=None):
		if not encoding:
			_req = Shiori.fromrequest(req, "ascii")
			encoding = _req.headers.get("Charset", locale.getdefaultlocale())
			del _req
		req = req.decode(encoding, "replace")
		lines = req.split("\r\n")
		line = lines[0]
		shiori = Shiori()
		shiori.type = "request"
		parts = line.split(" ")
		if int(parts[-1].split("/")[1][0]) >= 3:
			shiori.method, shiori.version = parts
		else:
			shiori.method, shiori.request, shiori.version = parts
		shiori.headers = OrderedDict()
		i = 0
		for line in lines[1:]:
			i += 1
			if not line:
				break
			kv = line.split(":", 1)
			if len(kv) < 2:
				continue
			k, v = kv
			shiori.headers[k] = v[1:]
		shiori.contents = "\r\n".join(lines[i:]) or ""
		return shiori
	
	@staticmethod
	def makerequest(sender, method="GET", headers={}, contents="", encoding="utf-8"):
		shiori = Shiori()
		shiori.type = "request"
		shiori.method = method
		shiori.version = Shiori.VERSION3
		shiori.headers = OrderedDict({
			"Charset": encoding,
			"Sender": sender
		})
		shiori.headers.update(headers)
		shiori.contents = contents
		return shiori
	
	@staticmethod
	def makeresponse(sender, code=200, headers={}, contents="", encoding="utf-8"):
		shiori = Shiori()
		shiori.type = "response"
		shiori.version = Shiori.VERSION3
		shiori.code = code
		shiori.headers = OrderedDict({
			"Charset": encoding,
			"Sender": sender
		})
		shiori.headers.update(headers)
		shiori.contents = contents
		return shiori
	
	@staticmethod
	def makeresponse2(sender, code=200, headers={}, contents="", encoding="utf-8"):
		shiori = Shiori.makeresponse(sender, code, headers, contents, encoding)
		shiori.version = Shiori.VERSION2
		return shiori
	
	def __str__(self):
		res = ""
		if self.type == "request":
			if int(self.version.split("/")[1][0]) >= 3:
				res = "{} {}\r\n".format(self.method, self.version)
			else:
				res = "{} {} {}\r\n".format(self.method, self.request, self.version)
			for k, v in self.headers.items():
				res += "{}: {}\r\n".format(k, v)
			res += "\r\n"
			if self.contents:
				res += self.contents
		elif self.type == "response":
			res = "{} {} {}\r\n".format(self.version, self.code, status_codes.get(self.code, "Unknown"))
			for k, v in self.headers.items():
				res += "{}: {}\r\n".format(k, v)
			res += "\r\n"
			if self.contents:
				res += self.contents
		return res

status_codes = {
	200: "OK",
	204: "No Content",
	310: "Communicate",
	311: "Not Enough",
	312: "Advice",
	400: "Bad Request",
	500: "Internal Server Error"
}
