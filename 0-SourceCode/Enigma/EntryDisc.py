# -*- coding: utf-8 -*-

"""
Enigma Input (ETW)
Glossary


ETW     Eintrittzwalze 
        Entry disc

There are only 2 varieties of the ETW

ABCDEFGHIJKLMNOPQRSTUVWXYZ
QWERTZUIOASDFGHJKPYXCVBNML
"""

from .AlphaUtils import alpha


class EntryDisc(object):
    """Entry Disc class"""
    def __init__(self, machine):
        """"""
        self.etwCode = machine['ETW']
        self.reverse = False
            
    def setReverse(self):
        self.reverse = True
        
    def __repr__(self):
        return "ETW: %s" % self.etwCode
        
    def __call__(self, ltr, debug=False):
        """encrypt the incoming letter - use: 'ETW(letter)'"""
        encltr = ltr
        if self.reverse:
            encltr = self.etwCode[alpha.pos(encltr)]
        else:
            encltr = alpha.letter(self.etwCode.index(encltr))
        if debug: print("in letter %s - out letter %s" % (ltr, encltr))
        return encltr

    #def encrypt(self, ltr):
    #    encltr = ltr
    #    encltr = alpha.letter(self.etwCode.index(encltr))
    #    if debug: print "in letter %s - out letter %s" % (ltr, encltr)
    #    return encltr
        
    #def decrypt(self, ltr):
    #    encltr = ltr
    #    encltr = self.etwCode[alpha.pos(encltr)]
    #    if debug: print "in letter %s - out letter %s" % (ltr, encltr)
    #    return encltr
        