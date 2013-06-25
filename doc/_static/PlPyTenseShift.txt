======================
PlPyTenseShift
======================

PlPyTenseShift is intended for translating polish sentences in present tense into past tense.

.. autoclass:: pytenseshift.PlPyTenseShift
	:members:

Here is simple example for using this tool:

::

	# -*- coding: utf-8 -*-
	from pytenseshift import PlPyTenseShift
	pl = PlPyTenseShift()
	print en.getPastTense("Michal skacze na trampolinie")

Output:

::

	Michal skakal na trampolinie.