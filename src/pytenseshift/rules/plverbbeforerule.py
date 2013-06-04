# -*- coding: utf-8 -*-
from shiftinterface import ShiftRule

class PlVerbBeforeRule(ShiftRule):
    '''
    Rule runs when there is only one noun that matches to verb in sentence.
    ''' 
    
    def shift(self, sentence):
        """Checks if there is (only one) noun before verb (translation rule) and if yes,
            translates the sentence taking this noun into account.
            
            Args:
                sentence: list of touple (word and its form) which are after verb
            Returns:
                list of touple (word and its PAST form) which are after verb -- if rule is satisfied
                False -- otherwise
        """
        # list of touple (noun and its form) which are before verb
        self.nouns_before = []
        self.verb_with_form = None
        
        if not self.__noun_exists(sentence):
            print "There is no noun in before verb in sentence"
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
    
    def __noun_exists(self, sentence):
        '''
        Check if there is any noun before verb and save it to list.
        '''
        exists = False
        
        for j,(word, form) in enumerate(sentence):
            if form['klasa'] == 'czasownik':
                self.verb_with_form = (word, form)
                break
            if form['klasa'] == 'rzeczownik':
                exists = True
                self.nouns_before.append((word, form))
        return exists
    
    def __get_nouns_matches(self):
        '''
        '''
        result = []
        
        for (word, form) in self.nouns_before:
            if self.verb_with_form[1]['liczba'] ==  form['liczba']:
                result.append((word, form))
        return result
            
            
            
            