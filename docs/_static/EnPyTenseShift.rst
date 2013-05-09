======================
EnPyTenseShift
======================

EnPyTenseShift is intended for translating english sentences in present tense into past tense.

.. autoclass:: pytenseshift.EnPyTenseShift
	:members:

Here is simple example for using this tool:

::

	# -*- coding: utf-8 -*-
	from pytenseshift import EnPyTenseShift
	en = EnPyTenseShift()
	print en.getPastTense("Michael jumps on a trampoline.")
	print en.getPastTense("Michael is jumping on a trampoline.")

Output:

::
	
	Michael jumped on a trampoline.
	Michael was jumping on a trampoline.
	

