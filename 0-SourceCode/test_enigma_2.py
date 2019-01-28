#!/usr/bin/env python2
# -*- coding: utf-8 -*-


import sys
import unittest
#from enigma import *
from Enigma.Exceptions import PlugBoardFullError, InvalidPlugError, InvalidRotorError
from Enigma.Keyboard import Keyboard
from Enigma.Rotors import RotorWheel, RotorFactory
from Enigma.Rotors import Left, Middle, Right, Greek
from Enigma.Reflectors import ReflectorFixed, ReflectorSettable, ReflectorRotating
from Enigma.PlugBoard import PlugBoard, Plug, createPlugBoard
from Enigma.EnigmaMachine import EnigmaMachine
from Enigma.MachineDetails import Machines


def spaceResult(result, groupSize=5):
    return ' '.join(result[i:i+groupSize] for i in xrange(0, len(result), groupSize))


class TestEnigma2(unittest.TestCase):
    """"""
        
    def test_Enigma_Instruction_Manual(self):
        """
        Machine Settings for Enigma I/M3
        Message key: ABL
        Reflector:	A
        Wheel order:	    II I III
        Ring positions: 	24 13 22
        Plug pairs:	AM FI NV PS TU WZ
        This message is taken from a German army instruction manual for the Enigma I (interoperable with the later navy machine, Enigma M3).
        """
        machine = Machines['I']
        plugboard = createPlugBoard(['AM', 'FI', 'NV', 'PS', 'TU', 'WZ'])
        RF = RotorFactory(machine)
        RF.createRotor(Left,    "II X A")
        RF.createRotor(Middle,   "I M B")
        RF.createRotor(Right,  "III V L")
        Enigma = EnigmaMachine (machine, RF, ReflectorFixed(machine, 'UKW-A'), plugboard)

        clue = "GCDSE AHUGW TQGRK VLFGX UCALX VYMIG MMNMF DXTGN VHVRM MEVOU YFZSL RHDRR XFJWC FHUHM UNZEF RDISI KBGPM YVXUZ"
        result = "FEIND LIQEI NFANT ERIEK OLONN EBEOB AQTET XANFA NGSUE DAUSG ANGBA ERWAL DEXEN DEDRE IKMOS TWAER TSNEU STADT"
        test={'name'   : "[I] Enigma Instruction Manual, 1930",
              'enigma' : Enigma,
              'clue'   : spaceResult(clue.replace(' ',''),4),
              'result' : spaceResult(result.replace(' ',''),5)}
        test_result = spaceResult(test['enigma'].encrypt_message(test['clue'], False),5)
        self.assertEqual(test_result, test['result'])


    def test_Enigma_Machine_WGLS(self):
        #print "\n-- Enigma Test 4 --"
        # Rotor 5 6 1 , Rings G G P, reflector B, plugs E-O F-P L-Y 
        machine = Machines['M3']
        plugboard = createPlugBoard(['EO','FP','LY'])
        RF=RotorFactory(machine)
        RF.createRotor(Left,    "V G A")
        RF.createRotor(Middle, "VI G A")
        RF.createRotor(Right,   "I P A")
        Enigma = EnigmaMachine (machine, RF, ReflectorFixed(machine, 'UKW-B'), plugboard )
        clue="WGLS CWYJ NLAY YMPW KSPP IKBK QDUA JVKO BLSS HIBO MHWO"
        result = "DERF UEHR ERIS TTOT XDER KAMP FGEH TWEI TERX DOEN ITZX"
        
        test={'name'   : "[M3] WGLS GGP Ring Setting",
              'enigma' : Enigma,
              'clue'   : clue,
              'result' : result}
        test_result = spaceResult(test['enigma'].encrypt_message(test['clue'], False),4)
        self.assertEqual(test_result, test['result'])
        
        
    @unittest.expectedFailure
    def DISABLED_test_Enigma_Machine_WGLS_no_Ring_Setting(self):
        #print "\n-- Enigma Test 4 --"
        # Rotor 5 6 1 , Rings G G P, reflector B, plugs E-O F-P L-Y 
        machine = Machines['M3']
        plugboard = createPlugBoard(['EO','FP','LY'])
        RF=RotorFactory(machine)
        RF.createRotor(Left,    "V A A")
        RF.createRotor(Middle, "VI A A")
        RF.createRotor(Right,   "I A A")
        Enigma = EnigmaMachine (machine, RF, ReflectorFixed(machine, 'UKW-B'), plugboard)
        clue = "WGLS CWYJ NLAY YMPW KSPP IKBK QDUA JVKO BLSS HIBO MHWO"
        result = "DERF UEHR ERIS TTOT XDER KAMP FGEH TWEI TERX DOEN ITZX"
        
        test={'name'   : "[M3] WGLS No Ring Setting [Without the ring settings this FAILS]",
              'enigma' : Enigma,
              'clue'   : clue,
              'result' : result}
        test_result = spaceResult(test['enigma'].encrypt_message(test['clue'], False),4)
        self.assertEqual(test_result, test['result'])


    def test_U264_Kapitanleutnant_Hartwig_Looks_1942(self):
        """
        U-264 (Kapitänleutnant Hartwig Looks), 1942
        Machine Settings for Enigma M4
        Reflector:			Thin B
        Wheel order:		β II IV I
        Ring positions: 	01 01 01 22
        Plug pairs:	AT BL DF GJ HM NW OP QY RZ VX
        Sent from a U-boat on 25th November 1942, this message was enciphered using their standard-equipment Enigma M4 machine.

        Message key: VJNA

        NCZW VUSX PNYM INHZ XMQX SFWX WLKJ AHSH NMCO CCAK UQPM KCSM HKSE INJU SBLK IOSX CKUB HMLL XCSJ USRR DVKO HULX WCCB GVLI YXEO AHXR HKKF VDRE WEZL XOBA FGYU JQUK GRTV UKAM EURB VEKS UHHV OYHA BCJW MAKL FKLM YFVN RIZR VVRT KOFD ANJM OLBG FFLE OPRG TFLV RHOW OPBE KVWM UQFM PWPA RMFH AGKX IIBG
        """
        machine = Machines['M4']
        plugboard = createPlugBoard(['AT', 'BL', 'DF', 'GJ', 'HM', 'NW', 'OP', 'QY', 'RZ', 'VX'])
        RF = RotorFactory(machine)
        RF.createRotor(Greek, "Beta A V")
        RF.createRotor(Left,    "II A J")
        RF.createRotor(Middle,  "IV A N")
        RF.createRotor(Right,    "I V A")
        Enigma = EnigmaMachine (machine, RF, ReflectorFixed(machine, 'UKW-B'), plugboard )

        clue = "NCZW VUSX PNYM INHZ XMQX SFWX WLKJ AHSH NMCO CCAK UQPM KCSM HKSE INJU SBLK IOSX CKUB HMLL XCSJ USRR DVKO HULX WCCB GVLI YXEO AHXR HKKF VDRE WEZL XOBA FGYU JQUK GRTV UKAM EURB VEKS UHHV OYHA BCJW MAKL FKLM YFVN RIZR VVRT KOFD ANJM OLBG FFLE OPRG TFLV RHOW OPBE KVWM UQFM PWPA RMFH AGKX IIBG"
        result = "VONV ONJL OOKS JHFF TTTE INSE INSD REIZ WOYY QNNS NEUN INHA LTXX BEIA NGRI FFUN TERW ASSE RGED RUEC KTYW ABOS XLET ZTER GEGN ERST ANDN ULAC HTDR EINU LUHR MARQ UANT ONJO TANE UNAC HTSE YHSD REIY ZWOZ WONU LGRA DYAC HTSM YSTO SSEN ACHX EKNS VIER MBFA ELLT YNNN NNNO OOVI ERYS ICHT EINS NULL"
        
        test={'name'   : "[M4] U264, 1942",
              'enigma' : Enigma,
              'clue'   : clue,
              'result' : spaceResult(result.replace(' ',''),4)}
        
        test_result = spaceResult(test['enigma'].encrypt_message(test['clue'], False),4)
        self.assertEqual(test_result, test['result'])
        

    def test_Turings_Treatise_1940(self):
        """
        Turing's Treatise, 1940
        Message included in a document written by Alan Turing for new codebreaker recruits at Bletchley Park.

        Message key: JEZA

        QSZVI DVMPN EXACM RWWXU IYOTY NGVVX DZ---
        
        Machine Settings for Enigma K Railway
        Wheel order:		refl III I II
        Ring positions: 	 26  17 16 13
        
        PROBLEM: The Railway has a rotating reflector
        """
        machine = Machines['R']
        RF = RotorFactory(machine)
        RF.createRotor(Left,   "III Q E")
        RF.createRotor(Middle,   "I P Z")
        RF.createRotor(Right,   "II M A")
        Enigma = EnigmaMachine (machine, RF, ReflectorSettable(machine, 'UKW', 'Z', 'J'), createPlugBoard([]) )

        clue   = "QSZV IDVM PNEX ACMR WWXU IYOT YNGV VXDZ"
        result = "DEUT SQET RUPP ENSI NDJE TZTI NENG LAND"
        
        test={'name'   : "[K] Turing's Treatise, 1940",
              'enigma' : Enigma,
              'clue'   : clue,
              'result' : result}
        test_result = spaceResult(test['enigma'].encrypt_message(test['clue'], False),4)
        self.assertEqual(test_result, test['result'])


    def test_Japanese_Turpitz(self):
        machine = Machines['T']
        RF = RotorFactory(machine)
        RF.createRotor(Left,  "III A A")
        RF.createRotor(Middle, "II A A")
        RF.createRotor(Right,   "I A A")
        Enigma = EnigmaMachine (machine, RF, ReflectorSettable(machine, 'UKW', 'A', 'A'), createPlugBoard([]) )

        clue =   "AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA"
        result = "WLZNV CRJQP PGBDV NXGMG JGXCC IUWOR"
        
        test={'name'   : "[T] Turpitz",
              'enigma' : Enigma,
              'clue'   : clue,
              'result' : result}
        test_result = spaceResult(test['enigma'].encrypt_message(test['clue'], False),5)
        self.assertEqual(test_result, test['result'])


    def test_Norway(self):
        machine = Machines['N']
        RF = RotorFactory(machine)
        RF.createRotor(Left,  "III A A")
        RF.createRotor(Middle, "II A A")
        RF.createRotor(Right,   "I A A")
        Enigma = EnigmaMachine (machine, RF, ReflectorSettable(machine, 'UKW', 'A', 'A'), createPlugBoard([]) )

        clue =   "AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA"
        result = "QWSCM IJHVV VLRHX IGXCW ODDWU WZSJQ"
        
        test={'name'   : "[N] Norenigma",
              'enigma' : Enigma,
              'clue'   : clue,
              'result' : result}
        test_result = spaceResult(test['enigma'].encrypt_message(test['clue'], False),5)
        self.assertEqual(test_result, test['result'])
        

    def test_Sondermaschine(self):
        pass
        

    def test_Zahlwerk(self):
        machine = Machines['A865']
        RF = RotorFactory(machine)
        RF.createRotor(Left,  "III A A")
        RF.createRotor(Middle, "II A A")
        RF.createRotor(Right,   "I A A")
        Enigma = EnigmaMachine (machine, RF, ReflectorRotating(machine, "uG", 'A', 'A'), None)
        
        clue =   "AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA"
        result = "EGWZQ HDDMG KUWQT XHUQV XRZTX KEHJE"
        
        test_result = spaceResult(Enigma.encrypt_message(clue, False),5)
        #print test_result
        self.assertEqual(test_result, result)
        

    #@unittest.expectedFailure
    def test_G312_Rotating_Reflector(self):
        """"""
        machine = Machines['G312']
        RF = RotorFactory(machine)
        RF.createRotor(Left,  "III A A")
        RF.createRotor(Middle, "II A A")
        RF.createRotor(Right,   "I A A")
        Enigma = EnigmaMachine (machine, RF, ReflectorRotating(machine, "uG", 'A', 'A'), None)
        
        clue =   "AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAA"
        result = "GJUIY CMDGU VTTFF QPZMX KVCTZ USOBZ LDZUM HQMJX WTZWM QNNUW IDYEQ PGVFZ ETOLB ZKTPL JPKRK FJGRT BNFBH BFYVK MVPVN HXUFJ OXSXE QTUPX LWKCO RIODF YXIVO ZUZCD SFEKB TXVGU EOGNV KZYTW SOYWK YPS"
        
        test_result = spaceResult(Enigma.encrypt_message(clue, False),5)
        #print test_result
        self.assertEqual(test_result, result)


    def test_G260(self):
        machine = Machines['G260']
        RF = RotorFactory(machine)
        RF.createRotor(Left,  "III A A")
        RF.createRotor(Middle, "II A A")
        RF.createRotor(Right,   "I A A")
        Enigma = EnigmaMachine (machine, RF, ReflectorRotating(machine, "uG", 'A', 'A'), None)
        
        clue =   "AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA"
        result = "CKNUL QYPIE MMXYG HTEGZ CDLVG TYXDB"
        
        test_result = spaceResult(Enigma.encrypt_message(clue, False),5)
        #print test_result
        self.assertEqual(test_result, result)
        

    def test_G111(self):
        machine = Machines['G111']
        RF = RotorFactory(machine)
        RF.createRotor(Left,    "V A A")
        RF.createRotor(Middle, "II A A")
        RF.createRotor(Right,   "I A A")
        Enigma = EnigmaMachine (machine, RF, ReflectorRotating(machine, "UKW", 'A', 'A'), None)
        
        clue =   "AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA"
        result = "QKUIB BGTIS OFZTS JGMXI EFGPI UBEUO"
        
        test_result = spaceResult(Enigma.encrypt_message(clue, False),5)
        #print test_result
        self.assertEqual(test_result, result)
        

    def test_Commercial_D(self):
        machine = Machines['D']
        RF = RotorFactory(machine)
        RF.createRotor(Left,  "III A A")
        RF.createRotor(Middle, "II A A")
        RF.createRotor(Right,   "I A A")
        Enigma = EnigmaMachine (machine, RF, ReflectorSettable(machine, "UKW", 'A', 'A'), None)
        
        clue =   "AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA"
        result = "HLKUD THSYV ICWNZ WWDMW KGEOG ZYEQI"
        
        test_result = spaceResult(Enigma.encrypt_message(clue, False),5)
        #print test_result
        self.assertEqual(test_result, result)
        

    def test_Commercial_K(self):
        machine = Machines['K']
        RF = RotorFactory(machine)
        RF.createRotor(Left,  "III A A")
        RF.createRotor(Middle, "II A A")
        RF.createRotor(Right,   "I A A")
        Enigma = EnigmaMachine (machine, RF, ReflectorSettable(machine, "UKW", 'A', 'A'), None)
        
        clue =   "AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA"
        result = "HLKUD THSYV ICWNZ WWDMW KGEOG ZYEQI"
        
        test_result = spaceResult(Enigma.encrypt_message(clue, False),5)
        #print test_result
        self.assertEqual(test_result, result)
        

    def test_Swiss_Air(self):
        machine = Machines['KS']
        RF = RotorFactory(machine)
        RF.createRotor(Left,  "III A A")
        RF.createRotor(Middle, "II A A")
        RF.createRotor(Right,   "I A A")
        Enigma = EnigmaMachine (machine, RF, ReflectorSettable(machine, "UKW", 'A', 'A'), None)
        
        clue =   "AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA"
        result = "INRKJ YXUKU TPIIL MLQRG DOFUM BXRTZ"
        
        test_result = spaceResult(Enigma.encrypt_message(clue, False),5)
        #print test_result
        self.assertEqual(test_result, result)
        

    def test_KD(self):
        pass
        

if __name__ == '__main__':

    from Enigma.Keyboard import TestKeyboard
    from Enigma.Rotors import TestRotors
    from Enigma.PlugBoard import TestPlugboard
    from Enigma.EnigmaMachine import TestEnigmaMachine

    print("\nUnit Tests for Enigma Machine\n")
    unittest.main()
    #suite = unittest.TestLoader().loadTestsFromTestCase(TestEnigma2)
    #unittest.TextTestRunner(verbosity=2).run(suite)
    #sys.exit()


