def makemenu(*args, **kwargs):
	res = ""
	items = {}
	if args:
		for arg in args:
			items[arg] = arg
	if kwargs:
		for k, v in kwargs:
			items[k] = v
	for k, v in items:
		res += makemenuitem(k, v)

def makemenuitem(title, id=None, *args):
	res = r"\![*]\q[{},{}".format(title, id or title)
	if isinstance(id, str):
		if str.startswith("On"):
			for arg in args:
				res += arg + ","
			res = res[:-1]
	res += r"]\n"
	return res

def say(narrator, surface=None, text=None):
	res = ""
	if narrator > 1:
		res += r"\p[{}]".format(narrator)
	else:
		res += "\\" + str(narrator)
	if text is not None:
		if surface:
			if surface > 9:
				res += r"\s[{}]".format(surface)
			else:
				res += r"\s" + str(surface)
	else:
		text = surface
	if text:
		res += str(text)
	res += r"\n\n"
	return res
