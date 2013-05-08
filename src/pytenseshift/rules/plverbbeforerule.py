from shiftinterface import ShiftRule

class PlVerbBeforeRule(ShiftRule):
    def shift(self, sentence):
        for j, (word, form) in enumerate(sentence):
            pass # do all the stuff
        return False