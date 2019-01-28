# -*- coding: utf-8 -*-

"""
Enigma Reflectors

UKW     Umkehrwalze 
        Reflector (literally: Reversing wheel)

        REFLECTORS
reflector B         AY BR CU DH EQ FS GL IP JX KN MO TZ VW
reflector C         AF BV CP DJ EI GO HY KR LZ MX NW TQ SU
reflector B Dünn    AE BN CK DQ FU GY HW IJ LO MP RX SZ TV
reflector C Dünn    AR BD CO EJ FN GT HK IV LM PW QZ SX UY
"""

from .AlphaUtils import alpha
from .Exceptions import InvalidReflectorError
from .Rotors import RotorWheel, Greek
#Reflector_B_Dunn = "ENKQAUYWJICOPBLMDXZVFTHRGS"
#Reflector_C_Dunn = "RDOBJNTKVEHMLFCWZAXGYIPSUQ"
#Reflectors = {'B': "YRUHQSLDPXNGOKMIEBFZCWVJAT",
#              'C': "FVPJIAOYEDRZXWGCTKUQSBNMHL"
#            }
#ReflectorIds = Reflectors.keys() #['B','C']
#ReflectorIds.sort()

class ReflectorFixed(object):
    """reflector class for the Enigma I M3 and M4"""
    def __init__(self, machine, reflector):
        """"""
        if reflector in machine['Reflectors']:
            self.reflectorCode = machine[reflector]
        else:
            raise InvalidReflectorError("Cannot find Reflector %s in Machine %s" % (reflector,machine['Name']))
            
        
    def __repr__(self):
        output = "Reflector: %s" % self.reflectorCode
        return output
        
    def __call__(self, ltr, debug=False):
        """encrypt the incoming letter - use: 'reflector(letter)'"""
        encltr = ltr
        
        # ------------------------------------------------------------------
        #         S t a n d a r d   R e f l e c t o r
        encltr = self.reflectorCode[alpha.pos(encltr)]
        if debug: print("reflector - out letter %s" % ( encltr))
        # ------------------------------------------------------------------

        return encltr


class ReflectorSettable(object):
    """reflector class for the Enigma K and derivatives"""
    def __init__(self, machine, reflector, ringSetting, position):
        """"""
        if reflector in machine['Reflectors']:
            self.reflectorCode = machine[reflector]
        else:
            raise InvalidReflectorError("Cannot find Reflector %s in Machine %s" % (reflector,machine['Name']))

        self.ringSetting = ringSetting
        self.position = position
        self.offset = alpha.pos(ringSetting) - alpha.pos(position)
            
    def __repr__(self):
        output = "ReflectorSettable: %s" % self.reflectorCode
        output += " ringSetting: %s position: %s" % (self.ringSetting, self.position)
        return output
        
    def __call__(self, ltr, debug=False):
        """encrypt the incoming letter - use: 'reflector(letter)'"""
        encltr = ltr

        # ------------------------------------------------------------------
        #         R o t a t i n g   R e f l e c t o r  (Railway Enigma)
        # first remove the ring setting offset to find the actual contact letter to encrypt
        encltr = alpha.letter(alpha.normal(alpha.pos(encltr) - self.offset)) 
        if debug: print("\nin letter %s - remove offset(%d) %s " % (ltr, self.offset, encltr))
        
        encltr = self.reflectorCode[alpha.pos(encltr)]
        if debug: print("reflector - out letter %s" % ( encltr))
        
        # re-add the ringsetting offset before returning the answer
        encltr = alpha.letter(alpha.normal(alpha.pos(encltr) + self.offset))
        if debug: print("adding offset(%d) %s" % (self.offset, encltr))
        # ------------------------------------------------------------------

        return encltr


class ReflectorRotating(object):
    """rotating reflector class for the Enigma G"""
    def __init__(self, machine, reflector, ringSetting, position):
        if reflector in machine['Reflectors']:
            self.reflectorCode = machine[reflector]
        else:
            raise InvalidReflectorError("Cannot find Reflector %s in Machine %s" % (reflector,machine['Name']))

        self.ringSetting = ringSetting
        self.position = position
        self.offset = alpha.pos(ringSetting) - alpha.pos(position)
        
        #self.rotor = createRotor(Greek, "uG A A")
        self.rotor = RotorWheel(machine, reflector, Greek, 'A', 'A')

    def rotate(self):
        self.rotor.rotate()

    def __repr__(self):
        output = "ReflectorRotating: %s" % self.reflectorCode
        return output
        
    def __call__(self, ltr, debug=True):
        encltr = ltr
        encltr = self.rotor(encltr)
        return encltr