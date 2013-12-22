_shellstate_patience = 15

@handle("OnSecondChange")
def _shellstate_secondchange(*args, **kwargs):
	if not "shellstate.mikire.timer" in phiori.var:
		phiori.var["shellstate.mikire.timer"] = 0
	if not "shellstate.kasanari.timer" in phiori.var:
		phiori.var["shellstate.kasanari.timer"] = 0
	if int(kwargs["Reference1"]) == 1:
		phiori.var["shellstate.mikire.timer"] += 1
	else:
		phiori.var["shellstate.mikire.timer"] = 0
	if int(kwargs["Reference2"]) == 1:
		phiori.var["shellstate.kasanari.timer"] += 1
	else:
		phiori.var["shellstate.kasanari.timer"] = 0
	if phiori.var["shellstate.mikire.timer"] >= _shellstate_patience and int(kwargs["Reference3"]) == 1:
		phiori.var["shellstate.mikire.timer"] = 0
		yield r"\![raise,OnMikire]"
	if phiori.var["shellstate.kasanari.timer"] >= _shellstate_patience and int(kwargs["Reference3"]) == 1:
		phiori.var["shellstate.kasanari.timer"] = 0
		yield r"\![raise,OnKasanari]"
