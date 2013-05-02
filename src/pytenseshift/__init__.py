# -*- coding: utf-8 -*-
from django.conf.locale import te
from array import *
from nltk.corpus import pl196x, treebank
from nltk.tag import UnigramTagger, DefaultTagger
from nltk.tokenize import word_tokenize as tokenize
#import en
# from andip import AnDiP
# from andip.provider import FileProvider, DatabaseProvider, PlWikiProvider


class ShiftRule():
    def shift(self, sentence):
        raise NotImplementedError("abstract method")

class PlShiftRule1(ShiftRule):
    def shift(self, sentence):
        for j, (word, form) in enumerate(sentence):
            pass # do all the stuff
        return False

class PlShiftRule2(ShiftRule):
    def shift(self, sentence):
        for j, (word, form) in enumerate(sentence):
            pass # do all the stuff
        return False

class TaggerInterface():
    
    def tag(self, tense):
        raise NotImplementedError("abstract method")

class MyTagger(TaggerInterface):
    
    def __init__(self, corpus):
        dtag = DefaultTagger("NN")
        self.__utag = UnigramTagger(corpus.tagged_sents(), backoff = dtag)
    def tag(self, tense):
        words = self.__utag.tag(tokenize(tense))
        
        for i, (word, form) in enumerate(words):
            word_info = {}
            if form[0] == 'V': word_info['klasa'] = 'czasownik'
            elif form[0] == 'S': word_info['klasa'] = 'rzeczownik'
            elif form[0] == 'A': word_info['klasa'] = 'przymiotnik'
            elif form[0] == 'N': word_info['klasa'] = 'liczebnik'
            elif form[0] == 'Z': word_info['klasa'] = 'zaimek'
            elif form[0] == 'D': word_info['klasa'] = 'przysłówek'
            elif form[0] == 'P': word_info['klasa'] = 'przyimek'
            elif form[0] == 'C': word_info['klasa'] = 'spójnik'
            elif form[0] == 'I': word_info['klasa'] = 'wykrzyknik'
            elif form[0] == 'T': word_info['klasa'] = 'partykuła'
            else: word_info['klasa'] = 'nieznany'
            
            if form[1] == 'S': word_info['liczba'] = 'pojedyncza'
            elif form[1] == 'P': word_info['liczba'] = 'mnoga'
            
            if(len(form) >= 3):
                if form[2] == 'N': word_info['przypadek'] = 'mianownik'
                elif form[2] == 'G': word_info['przypadek'] = 'dopełniacz'
                elif form[2] == 'D': word_info['przypadek'] = 'celownik'
                elif form[2] == 'A': word_info['przypadek'] = 'biernik'
                elif form[2] == 'I': word_info['przypadek'] = 'narzędnik'
                elif form[2] == 'L': word_info['przypadek'] = 'miejscownik'
                elif form[2] == 'V': word_info['przypadek'] = 'wołacz'
            
            if(len(form) >= 4):
                if form[3] == 'M': word_info['rodzaj'] = 'męski'
                elif form[3] == 'P': word_info['rodzaj'] = 'męski'
                elif form[3] == 'A': word_info['rodzaj'] = 'męski'
                elif form[3] == 'I': word_info['rodzaj'] = 'męski'
                elif form[3] == 'F': word_info['rodzaj'] = 'źeński'
                elif form[3] == 'N': word_info['rodzaj'] = 'nijaki'
                elif form[3] == 'O': word_info['rodzaj'] = 'męski'
                elif form[3] == 'R': word_info['rodzaj'] = 'żeński'
                elif form[3] == 'T': word_info['rodzaj'] = 'żeński'
            if(len(form) >= 6):
                if form[5] == '1': word_info['osoba'] = 'pierwsza'
                elif form[5] == '2': word_info['osoba'] = 'druga'
                elif form[5] == '3': word_info['osoba'] = 'trzecia'
                elif form[5] == 'I': word_info['osoba'] = 'bezokolicznik'
                elif form[5] == 'B': word_info['osoba'] = 'bezosobnik'
                elif form[5] == 'U': word_info['osoba'] = 'imiesłów'
                elif form[5] == 'W': word_info['osoba'] = 'imiesłów'
            if(len(form) >= 7):
                if form[6] == 'T': word_info['czas'] = 'teraźniejszy'
                elif form[6] == 'P': word_info['czas'] = 'przeszły'
                elif form[6] == 'F': word_info['czas'] = 'przyszły'
            if(len(form) >= 8):
                if form[7] == 'O': word_info['tryb'] = 'oznajmujący'
                elif form[7] == 'P': word_info['tryb'] = 'przypuszczający'
                elif form[7] == 'R': word_info['tryb'] = 'rozkazujący'
            if(len(form) >= 9):
                if form[8] == 'D': word_info['aspekt'] = 'dokonany'
                elif form[8] == 'N': word_info['aspekt'] = 'niedokonany'
            
            words[i] = (words[i][0], word_info)
        
        return words

class PyTenseShift():

    def __init__(self, corpus):
        self.tagger = MyTagger(corpus)
        #dtag = DefaultTagger("NN")
        #self.__utag = UnigramTagger(corpus.tagged_sents(), backoff = dtag)
    def _tokenize(self, tense):
        #return self.__utag.tag(tokenize(tense))
        return self.tagger.tag(tense)

    def getPastTense(self, tense):
        
        """

        :param tense:
        :raise:
        """
        raise NotImplementedError("abstract method")

class PlPyTenseShift(PyTenseShift):
    
    def __init__(self):
        PyTenseShift.__init__(self, pl196x)
        self.shiftRules = {PlShiftRule1(), PlShiftRule2()};
        # ad1 = AnDiP(DatabaseProvider("../andip_tmp"))
        # self._andip = AnDiP(PlWikiProvider(),  backoff = ad1)
    
    def getPastTense(self, tense):
        words = self._tokenize(tense)
        sentences = {}
        current_sentence = 0
        sentences[current_sentence] = []
        verb_occured = False
        for i, (word, form) in enumerate(words):
            if form['klasa'] == "spójnik" or (word == ',' and verb_occured == True): # spójnik, mozna podzielic zdanie
                sentences[current_sentence].append(words[i])
                current_sentence = current_sentence + 1
                sentences[current_sentence] = []
                verb_occured = False
            else:
                if form['klasa'] == "czasownik":
                    verb_occured = True
                sentences[current_sentence].append(words[i])
        
        new_sentence = []
        for i in sentences:
            for rule in self.shiftRules:
                #r = rule()
                ret = rule.shift(sentences[i])
                if ret != False:
                    sentences[i] = ret
                    break
            #sentences[i] = " ".join(sentences[i][1]);
            
            for j, (word, form) in enumerate(sentences[i]):
                new_sentence.append(word)
        return " ".join(new_sentence)

'''class EnPyTenseShift(PyTenseShift):

    def __init__(self):
        PyTenseShift.__init__(self, treebank)
        self.__en = en

    def getPastTense(self, tense):

        words = self._tokenize(tense)

        for i, (word, form) in enumerate(words):

            if word == 'to' and len(words) > i:
                words[i + 1] = (words[i + 1][0], "NN")

            if len(form) == 3 and form[0:3] in ['VBZ', 'VBP']:
                form = "VB" # we care about this kind of verbs

            if form[0:2] == 'MD':
                form = "VB" # we care about modals

            if form == "VB": # shift to past

                # exceptions
                exc = {"may" : "might", "will" : "would", "must" : "must", "ought" : "ought", "shall" : "should"}

                if exc.has_key(word):
                    word = exc[word]
                else:
                    try:
                        # print en.verb.infinitive(word), en.verb.is_tense(word, "1st singular present",  negated = False), en.verb.is_tense(word, "3rd singular present", negated = False), en.verb.past(word)
                        if en.verb.infinitive(word) == "be":
                            if en.verb.is_tense(word, "1st singular present",  negated = False) or en.verb.is_tense(word, "3rd singular present", negated = False):
                                word = "was"
                            else:
                                word = "were"
                        else:
                            word = en.verb.past(word)
                            if len(word) == 0:
                                raise Exception()
                    except Exception, KeyError:
                        raise Exception("Nodebox linguistics does not recognize the verbs.")

            if form == 'VB' and len(words) > i:
                j = i + 1
                if words[j][1] == 'RB' and  words[j][0] in ['not', "n't"] and len(words) > j:
                    j = j + 1
                words[j] = (words[j][0], "NN")

            words[i] = (word, form)

        result = ""
        for (word, form) in words:
            if word not in ["n't", ".", "!", "?"] and word[0] != "'":
                result += " "
            result += word;

        return result[1:]
'''
