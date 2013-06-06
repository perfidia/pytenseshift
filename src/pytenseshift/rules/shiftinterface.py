"""
If you want to implement your own rules for translating polish 
sentences into present tense into past tense you have to derived
from this class.
"""
class ShiftRule():
    def __init__(self, andip):
        self.andip = andip
    
    def shift(self, sentence):
        """Translates sentence given in present tense into past tense if specified rule is satisfied
            
            Args:
                sentence: list of touple (word and its form) which are after verb
            Returns:
                list of touple (word and its PAST form) which are after verb -- if rule is satisfied
                False -- otherwise
        """
        raise NotImplementedError("abstract method")