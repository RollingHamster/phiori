@handle("OnMinuteChange")
def _time_minutechange(*args, **kwargs):
	now = datetime.datetime.today()
	if now.minute == 0:
		yield r"\![raise,OnHourChange,{},{},{},{}]".format(kwargs["Reference0"], kwargs["Reference1"], kwargs["Reference2"], kwargs["Reference3"])

@handle("OnHourChange")
def _time_hourchange(*args, **kwargs):
	now = datetime.datetime.today()
	if now.hour == 0:
		yield r"\![raise,OnDayChange,{},{},{},{}]".format(kwargs["Reference0"], kwargs["Reference1"], kwargs["Reference2"], kwargs["Reference3"])
