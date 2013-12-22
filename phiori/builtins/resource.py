def loadres():
	with open(os.path.join(phiori.path, "resource.txt"), "r", encoding=phiori.encoding) as f:
		lines = f.read().replace("\r", "").split("\n")
		for line in lines:
			line = line.strip()
			if not line:
				continue
			kv = line.split(",", 1)
			if len(kv) == 2:
				k, v = kv
				phiori.res[k.strip()] = v.strip()

if os.path.exists(os.path.join(phiori.path, "resource.txt")):
	loadres()
