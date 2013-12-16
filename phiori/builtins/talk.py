@handle("OnSecondChange")
def _talk_secondchange(*args, **kwargs):
	if not "talk.timer" in phiori.var:
		phiori.var["talk.timer"] = 0
	if not "talk.interval" in phiori.var:
		phiori.var["talk.interval"] = int(phiori.config["talk.interval"]) + random.randint(-2, 4)
	if kwargs["Reference3"] == "1":
		phiori.var["talk.timer"] += 1
	if phiori.var["talk.timer"] >= phiori.var["talk.interval"]:
		yield r"\![raise,OnTalk]"

@handle("OnTranslate")
def _talk_translate(*args, **kwargs):
	phiori.var["talk.timer"] = 0
	phiori.var["talk.interval"] = int(phiori.config["talk.interval"]) + random.randint(-2, 4)
