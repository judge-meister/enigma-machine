
"""
Enigma Machine (M3)

          Notches
Rotor I     at R
Rotor II    at F
Rotor III   at W
Rotor IV    at K
Rotor V     at A
Rotors VI,  at A and N
Rotors VII  at A and N
Rotors VIII at A and N


        ROUTE
Keyboard, PlugBoard, EntryDisc, Rotor 3(R), Rotor 2(R), Rotor 1(R), Reflector,
          Rotor 1, Rotor 2, Rotor 3, EntryDisc(R), PlugBoard(R), LampBoard


Day|Ref|Wheels     |Ring|Ground|Plugs
 1   B  II I IV    |EOE | IYR  |EX FB HP LJ MS QT RO UG YC ZI
 2   C  VII I VI   |ARV | JPM  |IB JP KO NW QE RM US XD YA ZG
 3   B  IV II VI   |LXK | VMX  |BC EM IF LS OY QA UP VK WJ ZH
 4   B  IV V VIII  |WLI | RYF  |BR DQ EK HC LY MF SU TO VJ XW
 5   C  II IV VIII |ZUH | RSN  |CZ GY HN JB LS OK QR UM VI WP
 6   C  III VIII V |ISX | ALK  |AX DR GU HB IP JO NC QY VT ZF
 7   C  II V IV    |MEI | MPS  |IK JH MD NO QR SP TG UF XA ZL
 8   B  IV VI VII  |ZVD | LKW  |BA CQ EH GF KS MI NV UT WY ZD
 9   B  V VII III  |OQO | ABK  |CN HI JR KT PW QO UV XF YD ZL
 10  B  III VII V  |WMF | XNQ  |AX CE DV HM KQ OW RL SI TG ZF
"""

import unittest
from .MachineDetails import Machines
from .PlugBoard import createPlugBoard
from .Rotors import RotorFactory

from .Reflectors import ReflectorFixed, ReflectorSettable
from .Keyboard import Keyboard
from .Rotors import Left, Middle, Right
from .AlphaUtils import alpha
from .EntryDisc import EntryDisc
from .LampBoard import LampBoard

class EnigmaMachine(object):
    """The Enigma Machine - it needs three rotors, a reflector and a plugboard
    """
    def __init__(self, enigma, rotors, reflector, plugboard):
        """
        We implement the enigma machine as the following list of operations;
            plugboard, 
            input (ETW)
            3 rotors, 
            a reflector (UKW), 
            the same 3 rotors in reverse order, 
            the input (ETW) in reverse
            and the plugboard again
        
        Pressing the keys on the keyboard actuates the rotation of the rotors.
        """
        self.debug = False
        self.rotors = rotors
        self.keyboard = Keyboard(enigma, rotors, reflector)
        self.lampboard = LampBoard()
        
        machine = []
        if plugboard:
            machine.append(plugboard)
        machine.append(EntryDisc(enigma))
        for rotor in rotors:
            machine.append(rotor)
        machine.append(reflector)
        machine.append(rotors) # rotors is a RotorFactory which has a call() method 
        for rotor in reversed(rotors):
            machine.append(rotor)
        ed = EntryDisc(enigma)
        ed.setReverse()
        machine.append(ed)
        if plugboard:
            machine.append(plugboard)
        machine.append(self.lampboard)
        self.machine = machine
    
    def enableDebug(self):
        self.debug = True
        self.lampboard.enableDebug(True)
        
    def reset(self): 
        """reset the position of the rotors"""
        for rotor in self.rotors: 
            rotor.reset()
        
    def encrypt_message(self, message, debug=False):
        """plugboard, rotors, reflector, rotors(reversed), plugboard"""
        if debug: print("Key Plug R1  R2  R3 Refl R3  R2  R1 Plug")
        answer = ''
        for msgltr in message:
                if debug: print("[Keyboard Press %s]\n=> %s" % (msgltr, msgltr))
                if msgltr in alpha:
                    encltr = msgltr
                    self.keyboard.press()
                    self.rotors.setForward()
                
                    for encrypt in self.machine:
                        if debug: print("[%s]" % (repr(encrypt)), end=' ')
                        encltr = encrypt(encltr, debug)
                        if debug: print("=> %s" % (encltr))
                    answer += encltr
                elif msgltr != ' ':
                    answer += msgltr
                if debug: print("")
        if debug: print("")
        return answer
        
    def get_rotor_positions(self):
        """"""
        letters = {}
        for rotor in [Left, Middle, Right]:
            letters[rotor] = alpha.letter(self.rotors[rotor].rotation)
        return letters


class TestEnigmaMachine(unittest.TestCase):
    
    def testEnigmaMachine_Encrypt(self):
        #print "\n-- Enigma Test 4 --"
        # Rotor 5 6 1 , Rings G G P, reflector B, plugs E-O F-P L-Y 
        machine = Machines['M3']
        RF=RotorFactory(machine)
        RF.createRotor(Left,   "V G A")
        RF.createRotor(Middle, "VI G A")
        RF.createRotor(Right,  "I P A")
        Enigma = EnigmaMachine (machine, RF, ReflectorFixed(Machines['M3'],'UKW-B'),
                                 createPlugBoard(['EO','FP','LY']) )
        clue="WGLS CWYJ NLAY YMPW KSPP IKBK QDUA JVKO BLSS HIBO MHWO"
        #print clue
        self.assertEqual(Enigma.encrypt_message(clue),
                         "DERFUEHRERISTTOTXDERKAMPFGEHTWEITERXDOENITZX")
        
    def testEnigmaMachine_Reset(self):
        #print "\n-- Enigma Test 4 --"
        # Rotor 5 6 1 , Rings G G P, reflector B, plugs E-O F-P L-Y 
        machine = Machines['M3']
        RF=RotorFactory(machine)
        RF.createRotor(Left,   "V G A")
        RF.createRotor(Middle, "VI G A")
        RF.createRotor(Right,  "I P A")
        Enigma = EnigmaMachine (machine, RF, ReflectorFixed(Machines['M3'],'UKW-B'),
                                 createPlugBoard(['EO','FP','LY']) )
        clue="WGLS CWYJ NLAY YMPW KSPP IKBK QDUA JVKO BLSS HIBO MHWO"
        #print clue
        self.assertEqual(Enigma.encrypt_message(clue),
                         "DERFUEHRERISTTOTXDERKAMPFGEHTWEITERXDOENITZX")
        Enigma.reset()
        self.assertEqual(Enigma.encrypt_message(clue),
                         "DERFUEHRERISTTOTXDERKAMPFGEHTWEITERXDOENITZX")
        


if __name__ == '__main__': # pragma: no cover
    
    print("\nUnit Tests for Enigma Machine\n")
    suite = unittest.TestLoader().loadTestsFromTestCase(TestEnigmaMachine)
    unittest.TextTestRunner(verbosity=2).run(suite)
    

