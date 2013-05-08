# -*- coding: utf-8 -*-

from array import *
from nltk.corpus import pl196x, treebank
from nltk.tag import UnigramTagger, DefaultTagger
from nltk.tokenize import word_tokenize as tokenize
from taggerinterface import TaggerInterface

class FirstTagger(TaggerInterface):
    
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
                elif form[3] == 'F': word_info['rodzaj'] = 'żeński'
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