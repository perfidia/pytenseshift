# -*- coding: utf-8 -*-

from shiftinterface import ShiftRule

class PlPrononunBeforeRule(ShiftRule):
    
    def shift(self, sentence):
        self.verb_with_form = None
        
        if not self._pronoun_exists(sentence):
            print "There is no pronoun in before verb in sentence"
            return False
        
        if self.verb_with_form == None:
            return False
        
        print "PRONOUN TRUE"
        
        conf = self._get_past_verb(sentence)
        conf['aspekt'] = self.verb_with_form[1]['aspekt']
        print conf
        return False
    
    def _pronoun_exists(self, sentence):
        exists = False
        
        for j,(word, form) in enumerate(sentence):
            if form['klasa'] == 'czasownik':
                self.verb_with_form = (word, form)
                break
            if form['klasa'] == 'zaimek':
                exists = True
        return exists
    
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
                