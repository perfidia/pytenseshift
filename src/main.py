# -*- coding: utf-8 -*-
'''
Created on Mar 20, 2013

@author: Bartosz Alchimowicz
'''
from pytenseshift import PlPyTenseShift 
#from pytenseshift import EnPyTenseShift

pl = PlPyTenseShift()
#print pl.getPastTense("Jadę na rowerze.")
#print pl.getPastTense("Ala ma kota.")
print pl.getPastTense("Ala ma kota a Marek ma psa")
print pl.getPastTense("Ja mam rowery")

'''en = EnPyTenseShift()
print en.getPastTense("I do not have to do it.")
print en.getPastTense("I don't have to do it.")
print en.getPastTense("I may do it later.")
print en.getPastTense("I have to do it.")
print en.getPastTense("I am big enthusiast of Python language.")
print en.getPastTense("I go out door and play football.")
print en.getPastTense("I go to visit my parents.")
print en.getPastTense("They aren't crazy. They are pretty awesome!")
print en.getPastTense("We are making photos and creating a lot of modern realistic landscapes.")
print en.getPastTense("It can allow to do it, making sandwich.")
print en.getPastTense("There's no need to develop the sysem like this.")
print en.getPastTense("He does the washing every weekend while I don't do it anytime.")
print en.getPastTense("The world is not in your books and maps. It's out there.")
print en.getPastTense(''' '''Home is behind, the world ahead,
And there are many paths to tread
Through shadows to the edge of night,
Until the stars are all alight.
Mist and shadow, cloud and shade,
All shall fade, all shall fade.'''#)
