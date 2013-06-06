# -*- coding: utf-8 -*-
from shiftinterface import ShiftRule

class PlVerbAfterRule(ShiftRule):
    
    def shift(self, sentence):
        """Checks if there is noun after verb (translation rule) and if yes,
            translates the sentence taking this noun into account.
            
            Args:
                sentence: list of touple (word and its form) which are after verb
            Returns:
                list of touple (word and its PAST form) which are after verb -- if rule is satisfied
                False -- otherwise
        """
        # list of touple (noun and its form) which are after verb
        self.nouns_after = []
        self.verb_with_form = None
        
        if not self._verb_exists(sentence):
            print "There is no noun in after verb in sentence"
            return False
        
        if self.verb_with_form == None:
            return False
        
        noun_lists = self.__get_nouns_matches()
        if len(noun_lists) != 1:
            return False
        else:
            # configuration for anDIP
            conf = {
                    'liczba' : self.verb_with_form[1]['liczba'],
                    'osoba' : self.verb_with_form[1]['osoba'],
                    'aspekt' : self.verb_with_form[1]['aspekt'],
                    'forma' : 'czas przeszły',
                    'rodzaj' : noun_lists[0][1]['rodzaj']
                    }
            infinitive = self.andip.get_conf(self.verb_with_form[0])[0][1]
            
            result = []
            for (word, form) in sentence:
                if form['klasa'] == 'czasownik':
                    result.append((self.andip.get_word(("czasownik", infinitive, conf)), form))
                else:
                    result.append((word,form))
            return result
        
        return False
    
    def _verb_exists(self, sentence):
        after_verb = False
        exists = False
        
        for j,(word, form) in enumerate(sentence):
            if form['klasa'] == 'czasownik':
                after_verb = True
                self.verb_with_form = (word, form)
            if form['klasa'] == 'rzeczownik' and after_verb:
                exists = True
                self.nouns_after.append((word, form))
        return exists

    def __get_nouns_matches(self):
        '''
        '''
        result = []
        
        for (word, form) in self.nouns_after:
            if self.verb_with_form[1]['liczba'] ==  form['liczba']:
                result.append((word, form))
        return result     