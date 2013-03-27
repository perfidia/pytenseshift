#from string import maketrans   # Required to call maketrans function.

class PyTenseShift():
    def __init__(self):
        pass

    def getPastTense(self, present_tense):
        raise Exception("abstract method")
    
class PlPyTenseShift(PyTenseShift):
    def __init__(self):
        PyTenseShift.__init__(self)
    
    def __tokenize(self, string):
        return string.split(" ")
        # translate(maketrans(".,;!?", "     "))
        
    def getPastTense(self, present_tense):
        
        word_list = self.__tokenize(present_tense)
        return word_list
        
    
    