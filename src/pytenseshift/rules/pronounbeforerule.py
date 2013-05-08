# -*- coding: utf-8 -*-

from shiftinterface import ShiftRule

class PlPrononunBeforeRule(ShiftRule):
    
    def shift(self, sentence):
        
        if not self._pronoun_exists(sentence):
            print "There is no pronoun in before verb in sentence"
            return False
        
        self._get_past_verb(sentence)
        
        #for j, (word, form) in enumerate(sentence):
        #    print word, form
        return False
    
    def _pronoun_exists(self, sentence):
        for j,(word, form) in enumerate(sentence):
            if form['klasa'] == 'czasownik':
                break
            if form['klasa'] == 'zaimek':
                return True
        return False
    
    def _get_past_verb(self, sentence):
        pronoun = ''
        result = None
        
        for j,(word, form) in enumerate(sentence):
            if form['klasa'] == 'zaimek':
                pronoun = word
                break
        
        if pronoun.lower() == 'ja':
            result = {'liczba':'pojedyńcza', 'forma' : 'czas przeszły', 'osoba' : 'pierwsza', 'rodzaj' : 'męski'}
        elif pronoun.lower() == 'ty':
            result = {'liczba':'pojedyńcza', 'forma' : 'czas przeszły', 'osoba' : 'druga', 'rodzaj' : 'męski'}
        elif pronoun.lower() == 'on':
            result = {'liczba':'pojedyńcza', 'forma' : 'czas przeszły', 'osoba' : 'trzecia', 'rodzaj' : 'męski'}
        elif pronoun.lower() == 'ona':
            result = {'liczba':'pojedyńcza', 'forma' : 'czas przeszły', 'osoba' : 'trzecia', 'rodzaj' : 'żeński'}
        elif pronoun.lower() == 'ono':
            result = {'liczba':'pojedyńcza', 'forma' : 'czas przeszły', 'osoba' : 'trzecia', 'rodzaj' : 'nijaki'}
        elif pronoun.lower() == 'my':
            result = {'liczba':'mnoga', 'forma' : 'czas przeszły', 'osoba' : 'pierwsza', 'rodzaj' : 'męski'}
        elif pronoun.lower() == 'wy':
            result = {'liczba':'mnoga', 'forma' : 'czas przeszły', 'osoba' : 'druga', 'rodzaj' : 'męski'}
        elif pronoun.lower() == 'oni':
            result = {'liczba':'mnoga', 'forma' : 'czas przeszły', 'osoba' : 'trzecia', 'rodzaj' : 'męski'}
        elif pronoun.lower() == 'one':
            result = {'liczba':'mnoga', 'forma' : 'czas przeszły', 'osoba' : 'trzecia', 'rodzaj' : 'męski'}
            
        return result
                