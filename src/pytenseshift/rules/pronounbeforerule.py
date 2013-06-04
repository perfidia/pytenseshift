# -*- coding: utf-8 -*-

from shiftinterface import ShiftRule

class PlPrononunBeforeRule(ShiftRule):
    
    def shift(self, sentence):
        """Translates sentence given in present tense into past tense if specified rule is satisfied
            
            Args:
                sentence: list of touple (word and its form) which are after verb
            Returns:
                list of touple (word and its PAST form) which are after verb -- if rule is satisfied
                False -- otherwise
        """
        self.verb_with_form = None
        
        if not self._pronoun_exists(sentence):
            #print "There is no pronoun in before verb in sentence"
            return False
        
        if self.verb_with_form == None:
            return False
        
        print "PRONOUN TRUE"
        
        conf = self._get_past_verb(sentence)
        conf['aspekt'] = self.verb_with_form[1]['aspekt']
        result = []
        for (word, form) in sentence:
            if form['klasa'] == 'czasownik':
                infinitive = self.andip.get_conf(word)[0][1]
                result.append((self.andip.get_word(("czasownik", infinitive, conf)), form))
            else:
                result.append((word,form))
        return result
    
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
            result = {'liczba':'pojedyńcza', 'forma' : 'czas przeszły', 'osoba' : 'pierwsza', 'rodzaj' : 'm'}
        elif pronoun.lower() == 'ty':
            result = {'liczba':'pojedyńcza', 'forma' : 'czas przeszły', 'osoba' : 'druga', 'rodzaj' : 'm'}
        elif pronoun.lower() == 'on':
            result = {'liczba':'pojedyńcza', 'forma' : 'czas przeszły', 'osoba' : 'trzecia', 'rodzaj' : 'm'}
        elif pronoun.lower() == 'ona':
            result = {'liczba':'pojedyńcza', 'forma' : 'czas przeszły', 'osoba' : 'trzecia', 'rodzaj' : 'ż'}
        elif pronoun.lower() == 'ono':
            result = {'liczba':'pojedyńcza', 'forma' : 'czas przeszły', 'osoba' : 'trzecia', 'rodzaj' : 'n'}
        elif pronoun.lower() == 'my':
            result = {'liczba':'mnoga', 'forma' : 'czas przeszły', 'osoba' : 'pierwsza', 'rodzaj' : 'm'}
        elif pronoun.lower() == 'wy':
            result = {'liczba':'mnoga', 'forma' : 'czas przeszły', 'osoba' : 'druga', 'rodzaj' : 'm'}
        elif pronoun.lower() == 'oni':
            result = {'liczba':'mnoga', 'forma' : 'czas przeszły', 'osoba' : 'trzecia', 'rodzaj' : 'm'}
        elif pronoun.lower() == 'one':
            result = {'liczba':'mnoga', 'forma' : 'czas przeszły', 'osoba' : 'trzecia', 'rodzaj' : 'm'}
            
        return result
                