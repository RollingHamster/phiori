@handle("OnMouseMove")
def _stroke_mousemove(*args, **kwargs):
	phiori.var["stroke.target"] = kwargs["Reference3"]
	if "stroke.collision" not in phiori.var:
		phiori.var["stroke.collision"] = ""
		phiori.var["stroke.point"] = 0
	if phiori.var["stroke.collision"] != kwargs.get("Reference4"):
		phiori.var["stroke.point"] = 0
		phiori.var["stroke.collision"] = kwargs.get("Reference4")
		phiori.var["stroke.begintime"] = time.time()
	elif phiori.var["stroke.collision"]:
		phiori.var["stroke.point"] += 1
		now = time.time()
		if now > phiori.var["stroke.begintime"] + 2:
			if phiori.var["stroke.point"] / (now - phiori.var["stroke.begintime"]) > 16:
				phiori.temp["stroke.raise"] = True
				phiori.temp["stroke.target"], phiori.temp["stroke.collision"], phiori.temp["stroke.point"] = phiori.var["stroke.target"], phiori.var["stroke.collision"], phiori.var["stroke.point"]
				phiori.var["stroke.collision"] = ""
				phiori.var["stroke.point"] = 0

@handle("OnSecondChange")
def _stroke_secondchange(*args, **kwargs):
	if phiori.temp.get("stroke.raise"):
		if int(kwargs["Reference3"]):
			yield r"\![raise,OnStroke,{},{},{}]".format(phiori.temp["stroke.target"], phiori.temp["stroke.collision"], phiori.temp["stroke.point"])
		del phiori.temp["stroke.raise"]
		del phiori.temp["stroke.target"]
		del phiori.temp["stroke.collision"]
		del phiori.temp["stroke.point"]
