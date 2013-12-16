def initsurface(count=2):
	res = ""
	for i in range(0, count - 1):
		if r > 1:
			res += r"\p[{}]".format(narrator)
		else:
			res += "\\" + str(narrator)
	return res

def makemenu(*args, **kwargs):
	res = ""
	items = {}
	if args:
		for arg in args:
			items[arg] = arg
	if kwargs:
		for k, v in kwargs.items():
			items[k] = v
	for k, v in items.items():
		res += makemenuitem(v, k)
	return res

def makemenuitem(title, id=None, *args):
	res = r"\![*]\q[{}".format(title)
	if id:
		res += ",{}".format(id)
	else:
		res += ",{}".format(title)
	if isinstance(id, str):
		if id.startswith("On"):
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
