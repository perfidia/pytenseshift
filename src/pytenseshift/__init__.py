# -*- coding: utf-8 -*-
from django.conf.locale import te

from nltk.corpus import pl196x, treebank
from nltk.tag import UnigramTagger
from nltk.tokenize import word_tokenize as tokenize

# from andip import AnDiP
# from andip.provider import FileProvider, DatabaseProvider, PlWikiProvider

class PyTenseShift():

    def __init__(self, corpus):
        self.__utag = UnigramTagger(corpus.tagged_sents())

    def _tokenize(self, tense):
        return self.__utag.tag(tokenize(tense))

    def getPastTense(self, tense):
        """

        :param tense:
        :raise:
        """
        raise NotImplementedError("abstract method")
    
class PlPyTenseShift(PyTenseShift):

    def __init__(self):
        PyTenseShift.__init__(self, pl196x)
        # ad1 = AnDiP(DatabaseProvider("../andip_tmp"))
        # self._andip = AnDiP(PlWikiProvider(),  backoff = ad1)
    
    def getPastTense(self, tense):

        words = self._tokenize(tense)

        return words
        
    
class EnPyTenseShift(PyTenseShift):

    def __init__(self):
        PyTenseShift.__init__(self, treebank)

    def getPastTense(self, tense):

        words = self._tokenize(tense)

        return words