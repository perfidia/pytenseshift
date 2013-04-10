# -*- coding: utf-8 -*-
from django.conf.locale import te

from nltk.corpus import pl196x, treebank
from nltk.tag import UnigramTagger, DefaultTagger
from nltk.tokenize import word_tokenize as tokenize
import en
# from andip import AnDiP
# from andip.provider import FileProvider, DatabaseProvider, PlWikiProvider

class PyTenseShift():

    def __init__(self, corpus):
        dtag = DefaultTagger("NN")
        self.__utag = UnigramTagger(corpus.tagged_sents(), backoff = dtag)

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
        self.__en = en

    def getPastTense(self, tense):

        words = self._tokenize(tense)


        for (word, form) in words:
            if form[0:2] == 'VB' : # VBP VBZ MD
                # try:
                #     # en.verb.past(word)
                #     # en.verb.conjugate()
                # except KeyError:
                #     pass
                # else:
                #     pass
                print word, form, self.__en.is_verb(word)

                # TODO
                # czasownik po czasowniku - drugi ignored "will not do"
                # czasownik z "to"
                # modale ręcznie
                # nieregularny być - wtedy trzeba
                # przeczenia 't lub not, nt?

                # formy skrótowe 'm 're 's 'll

        # return words