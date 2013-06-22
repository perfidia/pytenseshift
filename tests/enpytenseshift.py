# -*- coding: utf-8 -*-

import unittest

from src.pytenseshift import EnPyTenseShift

class EnPyTenseShiftTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ad = EnPyTenseShift()

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

    # 's 'll ... handling
    # print en.getPastTense("My girlfriend said that the Lord of the Rings movies are boring. Now, i'm a single.")
    #

    # ERRORS
    # print en.getPastTense("You can use the library to conjugate verbs, pluralize nouns, write out numbers, find dictionary descriptions and synonyms for words, summarise texts and parse grammatical structure from sentences.")


    def testGetPastTense(self):
        self.assertEquals(1, 1);

if __name__ == '__main__':
    #import sys;sys.argv = ['', 'Test.test']
    unittest.main()
