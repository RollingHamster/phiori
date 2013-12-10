@handle("OnMouseMove")
def _stroke_mousemove(*args, **kwargs):
	var["stroke.target"] = kwargs["Reference3"]
	if "stroke.collision" not in var:
		var["stroke.collision"] = ""
		var["stroke.point"] = 0
	if var["stroke.collision"] != kwargs["Reference4"]:
		var["stroke.point"] = 0
		var["stroke.collision"] = kwargs["Reference4"]
		var["stroke.begintime"] = time.time()
	elif var["stroke.collision"]:
		var["stroke.point"] += 1
		now = time.time()
		if now > var["stroke.begintime"] + 2:
			if var["stroke.point"] / (now - var["stroke.begintime"]) > 16:
				yield r"\![raise,OnStroke,{},{},{}]".format(var["stroke.target"], var["stroke.collision"], var["stroke.point"])
				var["stroke.collision"] = ""
				var["stroke.point"] = 0
