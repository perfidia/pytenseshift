# -*- coding: utf-8 -*-
from array import *
from nltk.corpus import pl196x, treebank
from nltk.tag import UnigramTagger, DefaultTagger
from nltk.tokenize import word_tokenize as tokenize
from taggers import FirstTagger
from rules import PlVerbAfterRule, PlVerbBeforeRule, PlPrononunBeforeRule
#import en
from andip import FileProvider, DatabaseProvider, PlWikiProvider


class PyTenseShift():

    def __init__(self, corpus):
        self.tagger = FirstTagger(corpus)
        #dtag = DefaultTagger("NN")
        #self.__utag = UnigramTagger(corpus.tagged_sents(), backoff = dtag)
    def _tokenize(self, tense):
        #return self.__utag.tag(tokenize(tense))
        return self.tagger.tag(tense)

    def getPastTense(self, tense):
        """Translates sentence given in present tense into past tense 
        
        Args:
            sentence (str): Sentence to translate
        Returns:
            str. Sentence in past tense
        """
        raise NotImplementedError("abstract method")

class PlPyTenseShift(PyTenseShift):
    
    def __init__(self):
        PyTenseShift.__init__(self, pl196x)
        ad1 = PlWikiProvider()
        ad2 = DatabaseProvider("../data/polish", backoff = ad1)
        self._andip = FileProvider("../data/polish", backoff = ad2)
        print self._andip.get_word(('czasownik', 'być', {'aspekt': 'niedokonane', 'forma': 'czas terazniejszy', 'liczba': 'pojedyncza', 'osoba': 'trzecia'}))
        print self._andip.get_word(('czasownik', 'mieć', {'aspekt': 'niedokonane', 'forma': 'czas terazniejszy', 'liczba': 'pojedyncza', 'osoba': 'trzecia'}))
        print self._andip.get_word(('czasownik', 'kupić', {'aspekt': 'dokonane', 'forma': 'czas terazniejszy', 'liczba': 'pojedyncza', 'osoba': 'trzecia'}))
        print self._andip.get_word(('czasownik', 'skakać', {'aspekt': 'niedokonane', 'forma': 'czas terazniejszy', 'liczba': 'pojedyncza', 'osoba': 'trzecia'}))
        print self._andip.get_conf("mamy")
        ad2.save_model(ad1.get_model())
        print "####"
        print self._andip.get_word(("czasownik", "mieć", {'aspekt': 'niedokonane', 'forma': 'czas przeszly', 'liczba': 'pojedyncza', 'osoba': 'trzecia', 'rodzaj': 'meski'}))
        print "####"
        self.shiftRules = {PlVerbBeforeRule(self._andip), PlPrononunBeforeRule(self._andip), PlVerbAfterRule(self._andip)};
    
    def getPastTense(self, tense):
        """Translates sentence given in present tense into past tense 
        
            Args:
                sentence (str): Sentence to translate
            Returns:
                str. Sentence in past tense
        """
        words = self._tokenize(tense)
        sentences = {}
        current_sentence = 0
        sentences[current_sentence] = []
        verb_occured = False
        for i, (word, form) in enumerate(words):
            if (form['klasa'] == "spójnik" or word == ',') and verb_occured == True: # spójnik, mozna podzielic zdanie
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
                print sentences[i]
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
