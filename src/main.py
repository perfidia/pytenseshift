# -*- coding: utf-8 -*-
'''
Created on Mar 20, 2013

@author: Bartosz Alchimowicz
'''
from pytenseshift import PlPyTenseShift 
from pytenseshift import EnPyTenseShift

# pl = PlPyTenseShift()
en = EnPyTenseShift()

# print pl.getPastTense("Jadę na rowerze.")
print en.getPastTense("I am big enthusiast of Python language.")
