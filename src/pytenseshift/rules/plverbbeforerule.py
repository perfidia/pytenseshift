from shiftinterface import ShiftRule

class PlVerbBeforeRule(ShiftRule):
    '''
    Rule runs when there is only one noun that matches to verb in sentence.
    ''' 
    
    def shift(self, sentence):
        # list of touple (noun and its form) which are before verb
        self.nouns_before = []
        self.verb_with_form = None
        
        if not self.__noun_exists(sentence):
            print "There is no noun in before verb in sentence"
            return False
        
        if self.verb_with_form == None:
            return False

        noun_lists = self.__get_nouns_matches()
        if len(noun_lists) > 1:
            return False
        else:
            print "TRUE"
            for (word, form) in noun_lists:
                print word, form
            return False
    
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
            
            
            
            