#!/usr/bin/env python


import unittest
from enigma import *

class EnigmaTest(unittest.TestCase):

    def testRotorI_P_A_W(self):
        RW = RotorWheel('I',"Right",'P','A') # 16,0
        RW.rotate()
        #print "Rotor I - for - W should become J",RW.encrypt("W",'F')
        self.assertEqual("J",RW("W"))#,'F'))
        
    def testRotorI_P_A_V(self):
        RW = RotorWheel('I',"Right",'P','A') # 16,0
        RW.rotate()
        RW.setForward(False)
        #print "Rotor I - rev - V should become D",RW.encrypt("V",'R'),"\n"
        self.assertEqual("D",RW("V"))#,'R'))
    
    def testRotorVI_G_A_J(self):
        RW = RotorWheel('VI',"Middle",'G','A') # 7,0
        #print "Rotor VI - for - J should become B",RW.encrypt("J",'F')
        self.assertEqual("B",RW("J"))#,'F'))
        
    def testRotorVI_G_A_X(self):
        RW = RotorWheel('VI',"Middle",'G','A') # 7,0
        #print "Rotor VI - rev - X should become V",RW.encrypt("X",'R'),"\n"
        RW.setForward(False)
        self.assertEqual("V",RW("X"))#,'R'))
    
    def testRotorV_G_A_V(self):
        RW = RotorWheel('V',"Left",'G','A') # 7,0
        #RW.printSettings()
        #print "Rotor V - for - B should become U",RW.encrypt("B",'F')
        self.assertEqual("U",RW("B"))#,'F'))
        
    def testRotorV_G_A_C(self):
        RW = RotorWheel('V',"Left",'G','A') # 7,0
        RW.setForward(False)
        #RW.printSettings()
        #print "Rotor V - rev - C should become X",RW.encrypt("C",'R'),"\n"
        self.assertEqual("X",RW("C"))#,'R'))


    def testRotorRotation(self):
        #print "Testing Rotor Rotation roll-over"
        RW = RotorWheel('I','Right','A','A')
        for x in range(0,26):
            #print(RW.rotation,RW.offset)
            self.assertEqual(RW.rotation,x)
            self.assertEqual(RW.offset,x*-1) 
            RW.rotate()
        for x in range(26,30):
            #print(RW.rotation,RW.offset)
            self.assertEqual(RW.rotation,x-26)
            self.assertEqual(RW.offset,(x-26)*-1) 
            RW.rotate()
    
    def testRotorWheel_Print(self):
        RW = RotorWheel('I','Right','A','A')
        ret = "%s" % RW
        self.assertEqual(ret,"rotor I = EKMFLGDQVZNTOWYHXUSPAIBRCJ 'Right' ring_setting = 1 rotation = 0")
        
    def testRotorWheel_Reset(self):
        RW = RotorWheel('I','Right','A','A')
        RW.rotate()
        self.assertEqual(RW.rotation,1)
        self.assertEqual(RW.offset,-1)
        RW.reset()
        self.assertEqual(RW.rotation,0)
        self.assertEqual(RW.offset,0)
        
    def testKeyboard(self):
        #print "Testing Keyboard"
        RF=RotorFactory()
        RF.createRotor(Left,   "I A A")
        RF.createRotor(Middle, "II A A")
        RF.createRotor(Right,  "III A A")
        KB = Keyboard(RF)
        for x in range(102):#(752):
            KB.press()
            #print(KB.Rotors[Left].rotation,KB.Rotors[Middle].rotation,KB.Rotors[Right].rotation)
            if x == 21:
                #print(KB.Rotors[Left].rotation,KB.Rotors[Middle].rotation,KB.Rotors[Right].rotation)
                self.assertEqual(0, KB.Rotors[Left].rotation)
                self.assertEqual(1, KB.Rotors[Middle].rotation)
                self.assertEqual(22,KB.Rotors[Right].rotation)
            if x == 99:
                #print(KB.Rotors[Left].rotation,KB.Rotors[Middle].rotation,KB.Rotors[Right].rotation)
                self.assertEqual(0, KB.Rotors[Left].rotation)
                self.assertEqual(4, KB.Rotors[Middle].rotation)
                self.assertEqual(22,KB.Rotors[Right].rotation)
            if x == 100:
                #print(KB.Rotors[Left].rotation,KB.Rotors[Middle].rotation,KB.Rotors[Right].rotation)
                self.assertEqual(1, KB.Rotors[Left].rotation)
                self.assertEqual(5, KB.Rotors[Middle].rotation)
                self.assertEqual(23,KB.Rotors[Right].rotation)

    def testPlug_1(self):
        """"""
        plug=Plug('AB')
        self.assertEqual(repr(plug),"AB")
        self.assertEqual(plug('A'),'B')
        self.assertEqual(plug('B'),'A')

    def testPlugBoard_InvalidPlugError_1(self):
        """"""
        PB=PlugBoard()
        PB+=Plug('AB')
        with self.assertRaises(InvalidPlugError) as e:
            PB+=Plug('AB')
        exc = e.exception
        self.assertEqual("%s" % exc,"AB")

    def testPlugBoard_InvalidPlugError_2(self):
        """"""
        PB=PlugBoard()
        PB+=Plug('AB')
        with self.assertRaises(InvalidPlugError) as e:
            PB+=Plug('BA') 
        exc = e.exception
        self.assertEqual("%s" % exc,"AB")

    def testPlugBoard_InvalidPlugError_3(self):
        """"""
        PB=PlugBoard()
        PB+=Plug('AB')
        with self.assertRaises(InvalidPlugError) as e:
            PB+=Plug('AC')
        exc = e.exception
        self.assertEqual("%s" % exc,"AC")

    def testPlugBoard_InvalidPlugError_4(self):
        """"""
        PB=PlugBoard()
        PB+=Plug('AB')
        with self.assertRaises(InvalidPlugError) as e:
            PB+=Plug('AA')
        exc = e.exception
        self.assertEqual("%s" % exc,"'AA'")

    def testPlugBoard_PlugBoardFullError(self):
        """"""
        PB=PlugBoard()
        PB = createPlugBoard(['AB', 'IJ', 'MN', 'TZ', 'QO', 'CP', 'DY', 'EX', 'FW', 'GV'])
        with self.assertRaises(PlugBoardFullError) as e:
            PB+=Plug('KS')
        exc = e.exception
        self.assertEqual("%s" % exc,"10")

    def testPlugBoard_Print(self):
        PB=PlugBoard()
        PB = createPlugBoard(['AB', 'IJ'])
        ret = "%s" % PB
        self.assertEqual(ret,"'AB IJ'")
        #self.assertEqual(ret,"Board=['B', 'A', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']\nPlugs=['A', 'B', 'I', 'J']")
        
    def testPlugBoard_encrypt(self):
        PB=PlugBoard()
        PB = createPlugBoard(['AB', 'IJ', 'MN', 'TZ', 'QO', 'CP', 'DY', 'EX', 'FW', 'GV'])
        self.assertEqual(PB('C'),'P')
        self.assertEqual(PB('P'),'C')
        self.assertEqual(PB('D'),'Y')
        self.assertEqual(PB('U'),'U')
    
    def testEnigmaMachine_Encrypt(self):
        #print "\n-- Enigma Test 4 --"
        # Rotor 5 6 1 , Rings G G P, reflector B, plugs E-O F-P L-Y 
        RF=RotorFactory()
        RF.createRotor(Left,   "V G A")
        RF.createRotor(Middle, "VI G A")
        RF.createRotor(Right,  "I P A")
        Enigma = EnigmaMachine ( RF, Reflectors['B'],
                                 createPlugBoard(['EO','FP','LY']) )
        clue="WGLS CWYJ NLAY YMPW KSPP IKBK QDUA JVKO BLSS HIBO MHWO"
        #print clue
        self.assertEqual(Enigma.encrypt_message(clue),
                         "DERFUEHRERISTTOTXDERKAMPFGEHTWEITERXDOENITZX")
        
    def testEnigmaMachine_Reset(self):
        #print "\n-- Enigma Test 4 --"
        # Rotor 5 6 1 , Rings G G P, reflector B, plugs E-O F-P L-Y 
        RF=RotorFactory()
        RF.createRotor(Left,   "V G A")
        RF.createRotor(Middle, "VI G A")
        RF.createRotor(Right,  "I P A")
        Enigma = EnigmaMachine ( RF, Reflectors['B'],
                                 createPlugBoard(['EO','FP','LY']) )
        clue="WGLS CWYJ NLAY YMPW KSPP IKBK QDUA JVKO BLSS HIBO MHWO"
        #print clue
        self.assertEqual(Enigma.encrypt_message(clue),
                         "DERFUEHRERISTTOTXDERKAMPFGEHTWEITERXDOENITZX")
        Enigma.reset()
        self.assertEqual(Enigma.encrypt_message(clue),
                         "DERFUEHRERISTTOTXDERKAMPFGEHTWEITERXDOENITZX")
        

if __name__ == '__main__':
    
    print("\nUnit Tests for Enigma Machine")
    unittest.main()
    

