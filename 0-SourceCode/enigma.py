#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
Enigma Tests
"""
# pylint: disable=trailing-whitespace, superfluous-parens
# pylint: disable=invalid-name, too-few-public-methods


from Enigma.PlugBoard import createPlugBoard
from Enigma.Rotors import RotorFactory
from Enigma.Rotors import Left, Middle, Right
from Enigma.Reflectors import *
from Enigma.MachineDetails import Machines
from Enigma.EnigmaMachine import EnigmaMachine


def Enigma_Test_1():
    """Test 1"""
    print("\n-- Enigma Test 1 --")
    machine = Machines['M3']
    RF = RotorFactory(machine)
    RF.createRotor(Left,   "I A A")
    RF.createRotor(Middle, "II A A")
    RF.createRotor(Right,  "III A A")
    Enigma = EnigmaMachine(machine, RF, Reflector(machine, 'UKW-B'),
                           createPlugBoard([]))
    clue = "AAAAA"
    print(clue)
    answer = Enigma.encrypt_message(clue)
    print(answer)
    assert answer == "BDZGO"
    
def Enigma_Test_2():
    """Test 2"""
    print("\n-- Enigma Test 2 --")
    machine = Machines['M3']
    RF = RotorFactory(machine)
    RF.createRotor(Left,   "I A A")
    RF.createRotor(Middle, "II A A")
    RF.createRotor(Right,  "III A A")
    Enigma = EnigmaMachine(machine, RF, Reflector(machine, 'UKW-B'),
                           createPlugBoard([]))
    clue = "OPGN DXCF WEVT NRSD ULTP" 
    print(clue)
    answer = Enigma.encrypt_message(clue)
    print(answer)
    assert answer == "THISISASECRETMESSAGE"
    # THIS IS A SECRET MESSAGE

def Enigma_Test_3():
    """Test 3
    
    Rotors VII, I, III with no ring settings, Reflector C and no plugs
    """
    print("\n-- Enigma Test 3 --")
    machine = Machines['M3']
    RF = RotorFactory(machine)
    RF.createRotor(Left,   "VII A A")
    RF.createRotor(Middle, "I A A")
    RF.createRotor(Right,  "III A A")
    Enigma = EnigmaMachine(machine, RF, Reflector(machine, 'UKW-C'),
                           createPlugBoard([]))
    clue = "ZUZB PCBG EOGY TRPB VUXG QTIX AWHT ZDZV ITOA "
    print(clue)
    answer = Enigma.encrypt_message(clue)
    print(answer)
    assert answer == "ENIGMAWASUSEDDURINGTHESECONDWORLDWAR"
    # ENIGMA WAS USED DURING THE SECOND WORLD WAR

def Enigma_Test_4():
    """Test 4
    
    Rotors V, VI, I with ring settings of G, G and P, Reflector B and three plugs
    """
    print("\n-- Enigma Test 4 --")
    # Rotor 5 6 1 , Rings G G P, reflector B, plugs E-O F-P L-Y 
    machine = Machines['M3']
    RF = RotorFactory(machine)
    RF.createRotor(Left,   "V G A")
    RF.createRotor(Middle, "VI G A")
    RF.createRotor(Right,  "I P A")
    Enigma = EnigmaMachine(machine, RF, Reflector(machine, 'UKW-B'),
                           createPlugBoard(['EO', 'FP', 'LY']))
    clue = "WGLS CWYJ NLAY YMPW KSPP IKBK QDUA JVKO BLSS HIBO MHWO"
    print(clue)
    answer = Enigma.encrypt_message(clue)
    print(answer)
    assert answer == "DERFUEHRERISTTOTXDERKAMPFGEHTWEITERXDOENITZX"
    #DER FUEHRER IST TOT X DER KAMPF GEHT WEITER X DOENITZ X
    
def runTests():
    """
    Answers

    1. BDZGO

    2. THIS IS A SECRET MESSAGE

    3. ENIGMA WAS USED DURING THE SECOND WORLD WAR

    4. In German: Der Führer ist tot. Der Kampf geht weiter. Dönitz
       Or, translated into English: 
       The Führer is dead. The battle will continue. Dönitz
    """
    Enigma_Test_1()
    Enigma_Test_2()
    Enigma_Test_3()
    Enigma_Test_4()

if __name__ == '__main__':
    runTests()
