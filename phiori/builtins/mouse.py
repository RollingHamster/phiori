@handle("OnMouseClick")
def _mouse_mouseclick(*args, **kwargs):
	if int(kwargs["Reference5"]) == 0:
		if int(kwargs["Reference3"]) == 0:
			yield r"\![raise,OnSakuraMouseClick,{Reference0},{Reference1},{Reference2},{Reference3},{Reference4},{Reference5}]".format(**kwargs)
		elif int(kwargs["Reference3"]) == 1:
			yield r"\![raise,OnKeroMouseClick,{Reference0},{Reference1},{Reference2},{Reference3},{Reference4},{Reference5}]".format(**kwargs)
		else:
			yield r"\![raise,OnCharacterMouseClick,{Reference0},{Reference1},{Reference2},{Reference3},{Reference4},{Reference5}]".format(**kwargs)

@handle("OnMouseDoubleClick")
def _mouse_mousedoubleclick(*args, **kwargs):
	if int(kwargs["Reference5"]) == 0:
		if int(kwargs["Reference3"]) == 0:
			yield r"\![raise,OnSakuraMouseDoubleClick,{Reference0},{Reference1},{Reference2},{Reference3},{Reference4},{Reference5}]".format(**kwargs)
		elif int(kwargs["Reference3"]) == 1:
			yield r"\![raise,OnKeroMouseDoubleClick,{Reference0},{Reference1},{Reference2},{Reference3},{Reference4},{Reference5}]".format(**kwargs)
		else:
			yield r"\![raise,OnCharacterMouseDoubleClick,{Reference0},{Reference1},{Reference2},{Reference3},{Reference4},{Reference5}]".format(**kwargs)
