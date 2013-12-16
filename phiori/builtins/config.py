def loadconfig():
	with open(os.path.join(phiori.path, "config.txt"), "r") as f:
		lines = f.read().replace("\r", "").split("\n")
		for line in lines:
			line = line.strip()
			if not line:
				continue
			kv = line.split(",", 1)
			if len(kv) == 2:
				k, v = kv
				phiori.config[k.strip()] = v.strip()

def saveconfig():
	with open(os.path.join(phiori.path, "config.txt"), "w") as f:
		for k, v in phiori.config.items():
			f.write(k + "," + v + "\n")

def defaultconfig():
	phiori.config = {
		"talk.interval": 15,
	}

if os.path.exists(os.path.join(phiori.path, "config.txt")):
	loadconfig()
else:
	defaultconfig()
	saveconfig()
