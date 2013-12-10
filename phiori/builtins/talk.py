@handle("OnSecondChange")
def _talk_secondchange(*args, **kwargs):
	if not "talk.timer" in var:
		var["talk.timer"] = 0
	if not "talk.interval" in var:
		var["talk.interval"] = int(config["talk.interval"]) + random.randint(-2, 4)
	if kwargs["Reference3"] == "1":
		var["talk.timer"] += 1
	if var["talk.timer"] >= var["talk.interval"]:
		yield r"\![raise,OnTalk]"

@handle("OnTranslate")
def _talk_translate(*args, **kwargs):
	var["talk.timer"] = 0
	var["talk.interval"] = int(config["talk.interval"]) + random.randint(-2, 4)
