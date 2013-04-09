# -*- coding: utf-8 -*-

from nltk.corpus import pl196x
from nltk.tag import UnigramTagger
from nltk.tokenize import word_tokenize as tokenize

from andip import AnDiP
from andip.provider import FileProvider, DatabaseProvider, PlWikiProvider

class PyTenseShift():

    def __init__(self, corpus, wikiprovider):
        self._utag = UnigramTagger(corpus.tagged_sents())
        ad1 = AnDiP(DatabaseProvider("../andip_tmp"))
        self._andip = AnDiP(wikiprovider,  backoff = ad1)

    def getPastTense(self, tense):
        """

        :param tense:
        :raise:
        """
        raise NotImplementedError("abstract method")
    
class PlPyTenseShift(PyTenseShift):

    def __init__(self):
        PyTenseShift.__init__(self, pl196x, PlWikiProvider())
    
    def __tokenize(self, string):
        return string.split(" ")
        # translate(maketrans(".,;!?", "     "))
        
    def getPastTense(self, tense):

        words = ut.tag(tokenize(tense))

        return words
        
    
    