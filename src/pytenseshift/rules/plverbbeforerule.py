from shiftinterface import ShiftRule

class PlVerbBeforeRule(ShiftRule):
    
    def shift(self, sentence):
        
        if not self._verb_exists(sentence):
            print "There is no noun in before verb in sentence"
            return False
        
        for j, (word, form) in enumerate(sentence):
            pass
        return False
    
    def _verb_exists(self, sentence):
        for j,(word, form) in enumerate(sentence):
            if form['klasa'] == 'czasownik':
                break
            if form['klasa'] == 'rzeczownik':
                return True
        return False