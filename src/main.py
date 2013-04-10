# -*- coding: utf-8 -*-
'''
Created on Mar 20, 2013

@author: Bartosz Alchimowicz
'''
from pytenseshift import PlPyTenseShift 
from pytenseshift import EnPyTenseShift

# pl = PlPyTenseShift()
# print pl.getPastTense("Jadę na rowerze.")


# import en
# print en.verb.past("does")
# print en.verb.past("can")
# print en.verb.past("have")
# fail:
# print en.verb.past("will")
# print en.verb.past("may")
# print en.verb.past("must")
# print en.verb.past("ought")
# print en.verb.past("is", negate=True)
# print en.verb.past("are", person=1, negate=False)
# print en.verb.past("are", person=3, negate=False)
# print en.verb.past("are", person=2, negate=False)
# print en.verb.past("are")
# for i in ['swimming', 'making', 'am', 'are', 'fighting', 'was']:
#     # print i, en.is_verb(i), en.verb.infinitive(i), en.verb.present(i, person=1, negate=True), en.verb.past(i, person="3rd", negate=False)
#     print en.verb.conjugate(i, "past", negate=False), en.verb.is_tense(i, "1st singular past", negated=False)
#     # are 1, 2, 3, "1st", "2nd", "3rd", "plural", "*". Just use the one you like most.
# print en.verb.present("gave", person=3, negate=False)



en = EnPyTenseShift()
# print en.getPastTense("I do not have to do it.")
# print en.getPastTense("I don't have to do it.")
# print en.getPastTense("I may do it later.")
# print en.getPastTense("I have to do it.")
print en.getPastTense("I am big enthusiast of Python language.")
# print en.getPastTense("I go out door and play football.")
# print en.getPastTense("I go to visit my parents.")
# print en.getPastTense("Ther aren't crazy. They are pretty awesome!")
# print en.getPastTense("We are making photos and creating a lot of modern realistic landscapes.")
# print en.getPastTense("You can use the library to conjugate verbs, pluralize nouns, write out numbers, find dictionary descriptions and synonyms for words, summarise texts and parse grammatical structure from sentences.")
# print en.getPastTense("It can allow to do it, making sandwich.")
# print en.getPastTense("There's not need to develop the system which will allow collecting and presenting information which are important from the KNOW criteria’s point of view.")
# print en.getPastTense("He does the washing every weekend while I don't do it anytime.")
# print en.getPastTense("Mo girlfriend said that the Lord of the Rings movies are boring. Now, i'm a single.")
# print en.getPastTense("The world is not in your books and maps. It's out there.")
# print en.getPastTense(''' Home is behind, the world ahead,
# And there are many paths to tread
# Through shadows to the edge of night,
# Until the stars are all alight.
# Then world behind and home ahead,
# We'll wander back and home to bed.
# Mist and twilight, cloud and shade,
# Away shall fade! Away shall fade! ''')