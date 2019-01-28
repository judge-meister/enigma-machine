

import sys
import unittest

# Collect all the tests from the other modules and then run them

from .Keyboard import TestKeyboard
from .Rotors import TestRotors
from .PlugBoard import TestPlugboard
from .EnigmaMachine import TestEnigmaMachine


if __name__ == '__main__':
    
    print("\nUnit Tests for Enigma Machine\n")
    unittest.main()
    
    #suite1 = unittest.TestLoader().loadTestsFromTestCase(TestKeyboard)
    #suite2 = unittest.TestLoader().loadTestsFromTestCase(TestRotors)
    #suite3 = unittest.TestLoader().loadTestsFromTestCase(TestPlugboard)
    #suite4 = unittest.TestLoader().loadTestsFromTestCase(TestEnigmaMachine)
    #unittest.TextTestRunner(verbosity=2).run(suite1)
    #unittest.TextTestRunner(verbosity=2).run(suite2)
    #unittest.TextTestRunner(verbosity=2).run(suite3)
    #unittest.TextTestRunner(verbosity=2).run(suite4)
    
