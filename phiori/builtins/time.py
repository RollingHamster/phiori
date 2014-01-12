@handle("OnMinuteChange")
def _time_minutechange(*args, **kwargs):
	now = datetime.datetime.today()
	if now.minute == 0:
		yield simulate("OnHourChange", kwargs["Reference0"], kwargs["Reference1"], kwargs["Reference2"], kwargs["Reference3"])
		if now.hour == 0:
			yield simulate("OnDayChange", kwargs["Reference0"], kwargs["Reference1"], kwargs["Reference2"], kwargs["Reference3"])
