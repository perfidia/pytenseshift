from shiftinterface import ShiftRule

class PlVerbAfterRule(ShiftRule):
    
    def shift(self, sentence):
        
        if not self._verb_exists(sentence):
            print "There is no noun in after verb in sentence"
            return False
        
        for j, (word, form) in enumerate(sentence):
            pass # do all the stuff
        return False
    
    def _verb_exists(self, sentence):
        after_verb = False
        
        for j,(word, form) in enumerate(sentence):
            if form['klasa'] == 'czasownik':
                after_verb = True
            if form['klasa'] == 'rzeczownik' and after_verb:
                return True
        return False
        