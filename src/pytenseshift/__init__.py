# -*- coding: utf-8 -*-
from array import *
from nltk.corpus import pl196x, treebank
from nltk.tag import UnigramTagger, DefaultTagger
from nltk.tokenize import word_tokenize as tokenize
from taggers import FirstTagger
from rules import PlVerbAfterRule, PlVerbBeforeRule, PlPrononunBeforeRule
from src import en
from andip import FileProvider, DatabaseProvider, PlWikiProvider


class PyTenseShift(object):

    """Initialization of PyTenseShift objects.
    
    The important part when you use the PlPyTenseShift is that
    we allow you to implmenent your own Tagger to optimize your
    results in translating from present to past tense. So, you need
    to implement the taggerinterface and change the second line of
    this code
    """
    def __init__(self, corpus, isPl):
        if isPl:
            self.tagger = FirstTagger(corpus)
        else:
            dtag = DefaultTagger("NN")
            self.__utag = UnigramTagger(corpus.tagged_sents(), backoff = dtag)

    """ Tokenize the input sentence into words.
    This kind of representation is better to evaluate.
    
    """
    def _tokenize(self, tense, isPl):
        if isPl:
            return self.tagger.tag(tense)
        else:
            return self.__utag.tag(tokenize(tense))

    def getPastTense(self, tense):
        """Translates sentence given in present tense into past tense 
        
        Args:
            sentence (str): Sentence to translate
        Returns:
            str. Sentence in past tense
        """
        raise NotImplementedError("abstract method")

class PlPyTenseShift(PyTenseShift):
    
    """Initialization and setting up the word bank for andip.
    
    Andip is a program which let us get information about every word.
    We mean its form, tense, etc. But first we need to get configuration
    of word we are going to use later.
    
    The important part of PyTenseShift project is that you can create
    your own rules for translating polish present tense into past tense.
    You only have to add your own Rule to shiftRules. 
    """
    def __init__(self):
        PyTenseShift.__init__(self, pl196x, True)
        
        # ANDIP Configuration
        ad1 = PlWikiProvider()
        ad2 = DatabaseProvider("../data/polish", backoff = ad1)
        ad3 = FileProvider("../data/polish", backoff = ad2)
        ad1.get_word(("czasownik", "występować", {'aspekt': 'niedokonane', 'forma': 'czas teraźniejszy', 'liczba': 'mnoga', 'osoba': 'trzecia'}))
        ad1.get_word(("czasownik", "robić", {'aspekt': 'niedokonane', 'forma': 'czas teraźniejszy', 'liczba': 'mnoga', 'osoba': 'trzecia'}))
        ad1.get_word(("czasownik", "mieć", {'aspekt': 'niedokonane', 'forma': 'czas przeszły', 'liczba': 'mnoga', 'osoba': 'trzecia', 'rodzaj': 'm'}))
        #print ad1.get_conf('robiłem')
        #print ad1.get_conf('robię')
        #print ad1.get_conf('robili')
        #print ad1.get_conf('występowałam')
        #print ad1.get_conf('mamy')
        ad2.save_model(ad1.get_model())
        # END ANDIP Configuration
        
        self.shiftRules = {PlVerbBeforeRule(ad2), PlPrononunBeforeRule(ad2), PlVerbAfterRule(ad2)};
    
    def getPastTense(self, tense):
        """Translates sentence given in present tense into past tense 
        
            Args:
                sentence (str): Sentence to translate
            Returns:
                str. Sentence in past tense
        """
        words = self._tokenize(tense, True)
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
                ret = rule.shift(sentences[i])
                if ret != False:
                    sentences[i] = ret
                    break
            sentences[i] = " ".join([word for (word,form) in sentences[i]]);
        return " ".join([value for value in sentences.values()])

class EnPyTenseShift(PyTenseShift):

    def __init__(self):
        PyTenseShift.__init__(self, treebank, False)
        self.__en = en

    def getPastTense(self, tense):

        words = self._tokenize(tense, False)

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

