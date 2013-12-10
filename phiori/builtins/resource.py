def loadres():
	with open(os.path.join(path, "resource.txt"), "r") as f:
		lines = f.read().replace("\r", "").split("\n")
		for line in lines:
			line = line.strip()
			if not line:
				continue
			kv = line.split(",", 1)
			if len(kv) == 2:
				k, v = kv
				res[k.strip()] = v.strip()

if os.path.exists(os.path.join(path, "resource.txt")):
	loadconfig()
