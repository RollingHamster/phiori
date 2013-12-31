@handle("OnSecondChange")
def _errmsg_secondchange(*args, **kwargs):
	if "_boot" in phiori.var:
		loaderrs = phiori.var["_boot"].get("loaderr")
		if loaderrs:
			for errfile in loaderrs:
				yield r"\0\b2\_q{}\x".format(errfile)
			yield r"\c"
		del phiori.var["_boot"]
