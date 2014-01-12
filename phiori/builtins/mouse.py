@handle("OnMouseClick")
def _mouse_mouseclick(*args, **kwargs):
	if not kwargs.get("Status"):
		if int(kwargs["Reference5"]) == 0:
			if int(kwargs["Reference3"]) == 0:
				yield simulate("OnSakuraMouseClick", kwargs["Reference0"], kwargs["Reference1"], kwargs["Reference2"], kwargs["Reference3"], kwargs["Reference4"], kwargs["Reference5"])
			elif int(kwargs["Reference3"]) == 1:
				yield simulate("OnKeroMouseClick", kwargs["Reference0"], kwargs["Reference1"], kwargs["Reference2"], kwargs["Reference3"], kwargs["Reference4"], kwargs["Reference5"])
			else:
				yield simulate("OnCharacterMouseClick", kwargs["Reference0"], kwargs["Reference1"], kwargs["Reference2"], kwargs["Reference3"], kwargs["Reference4"], kwargs["Reference5"])

@handle("OnMouseDoubleClick")
def _mouse_mousedoubleclick(*args, **kwargs):
	if not kwargs.get("Status"):
		if int(kwargs["Reference5"]) == 0:
			if int(kwargs["Reference3"]) == 0:
				yield simulate("OnSakuraMouseDoubleClick", kwargs["Reference0"], kwargs["Reference1"], kwargs["Reference2"], kwargs["Reference3"], kwargs["Reference4"], kwargs["Reference5"])
			elif int(kwargs["Reference3"]) == 1:
				yield simulate("OnKeroMouseDoubleClick", kwargs["Reference0"], kwargs["Reference1"], kwargs["Reference2"], kwargs["Reference3"], kwargs["Reference4"], kwargs["Reference5"])
			else:
				yield simulate("OnCharacterMouseDoubleClick", kwargs["Reference0"], kwargs["Reference1"], kwargs["Reference2"], kwargs["Reference3"], kwargs["Reference4"], kwargs["Reference5"])
