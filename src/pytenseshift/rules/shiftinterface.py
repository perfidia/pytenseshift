class ShiftRule():
    def __init__(self, andip):
        self.andip = andip
    
    def shift(self, sentence):
        raise NotImplementedError("abstract method")