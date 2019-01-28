
"""
Alpha Utilities
"""

ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class Alphabet(object):
    """Alphabet"""
    def __init__(self):
        self.alpha = ALPHA #"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        
    def __contains__(self, l):
        """use: 'if x in alpha:'"""
        return l in self.alpha
        
    @staticmethod
    def normal(i):
        """normalise the position"""
        return i%26
        
    def pos(self, l):
        """return the position"""
        return self.alpha.index(l)
        
    def letter(self, i):
        """return the letter"""
        return self.alpha[i]

alpha = Alphabet()
