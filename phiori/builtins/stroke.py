@handle("OnMouseMove")
def _stroke_mousemove(*args, **kwargs):
	phiori.var["stroke.target"] = kwargs["Reference3"]
	if "stroke.collision" not in phiori.var:
		phiori.var["stroke.collision"] = ""
		phiori.var["stroke.point"] = 0
	if var["stroke.collision"] != kwargs["Reference4"]:
		phiori.var["stroke.point"] = 0
		phiori.var["stroke.collision"] = kwargs["Reference4"]
		phiori.var["stroke.begintime"] = time.time()
	elif var["stroke.collision"]:
		phiori.var["stroke.point"] += 1
		now = time.time()
		if now > phiori.var["stroke.begintime"] + 2:
			if phiori.var["stroke.point"] / (now - var["stroke.begintime"]) > 16:
				yield r"\![raise,OnStroke,{},{},{}]".format(phiori.var["stroke.target"], phiori.var["stroke.collision"], phiori.var["stroke.point"])
				phiori.var["stroke.collision"] = ""
				phiori.var["stroke.point"] = 0
