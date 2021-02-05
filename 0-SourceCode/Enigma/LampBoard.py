# -*- coding: utf-8 -*-
"""
Lamp Board
Glossary

Used to display the encrypted letter as a result of pressing a key on the keyboard.

this makes it easier to highlight the encrypted letter the Enigma 
Machine produces upon pressing a key on the Keyboard.

"""


class LampBoard(object):
    """Lamp Board class"""
    def __init__(self, debug=False):
        """"""
        self.debug = debug
        
    def __repr__(self):
        return "Lamp Board"
        
    def enableDebug(self, debug=False):
        self.debug = debug
        
    def __call__(self, ltr, debug=False):
        """display the resultant encrypted letter"""
        if self.debug: print("Light Lamp: %s" % ltr)
        return ltr
