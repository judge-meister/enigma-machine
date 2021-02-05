
"""
Enigma PlugBoard

        PLUG BOARD
10 pairs of letters can be swapped
"""

import unittest
from .AlphaUtils import alpha
from .Exceptions import InvalidPlugError, PlugBoardFullError


class Plug(object):
    """Plug"""
    def __init__(self, pair, debug=False):
        self.pairStr = ''
        self.pairDict = {}
        #self.iter = None
        self._validate(pair)
        self.debug = debug

    def _validate(self, pair):
        """validate the plug"""
        for l in pair:
            if l not in alpha:
                raise InvalidPlugError(pair)
        if pair[0] == pair[1]:
            raise InvalidPlugError(pair)
        self.pairStr = pair
        if pair[0] > pair[1]: 
            self.pairStr = "%s%s" % (pair[1], pair[0])
        self.pairDict = {pair[0]:pair[1], pair[1]:pair[0]}
        
    def __repr__(self):
        """use: 'print plug'"""
        return self.pairStr
        
    def __eq__(self, plug):
        """use: 'if x == y:'"""
        return self.pairStr == repr(plug)
        
    def __getitem__(self, loc):
        """use: 'plug[1]'"""
        if loc in [0, 1]:
            ltr = list(self.pairDict.keys())[loc]
            return self.pairDict[ltr]
        else:
            raise IndexError
            
    def __iter__(self):
        """use: 'for x in Plug:'"""
        #self.iter = iter(self.pairStr)
        #return self.iter
        for pair in self.pairStr:
            yield pair
        
    #def encrypt(self,ltr):
    def __call__(self, ltr, debug=False):
        """encrypt the letter - use: 'plug(letter)'"""
        encltr = self.pairDict[ltr]
        if self.debug: print("Plug In %s - Plug out %s" % (ltr, encltr))
        return encltr



class PlugBoard(object):
    """Plugboard"""
    def __init__(self):
        #self.iter = None
        self.plugs = []
        self.maxPlugs = 10
        self.debug = False
        
    def _partialMatch(self, plug):
        """is it a partial match"""
        for p in self.plugs:
            for l in plug:
                if l in p:
                    raise InvalidPlugError(plug)
                    
    def __iadd__(self, plug):
        """use: 'Plugboard += Plug'"""
        if plug in self.plugs or self._partialMatch(plug):
            raise InvalidPlugError(plug)
        if len(self.plugs) < self.maxPlugs:
            self.plugs.append(plug)
        else:
            raise PlugBoardFullError(self.maxPlugs)
        return self
        
    def __repr__(self):
        """use: 'print plugboard'"""
        plugs = []
        for p in self.plugs:
            plugs.append(repr(p))
        return "PlugBoard: %s" % (repr(' '.join(plugs)))
        
    def __iter__(self):
        """use: 'for plug in plugboard:'"""
        #self.iter = iter(self.plugs)
        #return self.iter
        for plug in self.plugs:
            yield plug
        
    #def encrypt(self, ltr):
    def __call__(self, ltr, debug=False):
        """use: plugboard(letter)""" 
        plug_used = False
        for plug in self.plugs:
            if ltr in plug:
                used = True
                return plug(ltr, debug) # .encrypt(ltr)
        #if self.debug and not plug_used: print("No Plug Used")
        if self.debug and not plug_used: print("PlugBoard return %s" % ltr)
        return ltr
    
    def setDebug(self, debug):
        self.debug = debug


def createPlugBoard(plugs, debug=False):
    """create and populate a plugboard class"""
    PB = PlugBoard()
    PB.setDebug(debug)
    for plug in plugs:
        PB += Plug(plug, debug)
    return PB


class TestPlugboard(unittest.TestCase):
    
    def testPlug_1(self):
        """"""
        plug=Plug('AB')
        self.assertEqual(repr(plug),"AB")
        self.assertEqual(plug('A'),'B')
        self.assertEqual(plug('B'),'A')

    def testPlugBoard_InvalidPlugError_1(self):
        """2 plugs with the same letter are not allowed"""
        PB=PlugBoard()
        PB+=Plug('AB')
        with self.assertRaises(InvalidPlugError) as e:
            PB+=Plug('AB')
        exc = e.exception
        self.assertEqual("%s" % exc,"AB")

    def testPlugBoard_InvalidPlugError_2(self):
        """2 plugs with the same letters are not allowed"""
        PB=PlugBoard()
        PB+=Plug('AB')
        with self.assertRaises(InvalidPlugError) as e:
            PB+=Plug('BA') 
        exc = e.exception
        self.assertEqual("%s" % exc,"AB")

    def testPlugBoard_InvalidPlugError_3(self):
        """plugs with even one letter in common are not allowed"""
        PB=PlugBoard()
        PB+=Plug('AB')
        with self.assertRaises(InvalidPlugError) as e:
            PB+=Plug('AC')
        exc = e.exception
        self.assertEqual("%s" % exc,"AC")

    def testPlugBoard_InvalidPlugError_4(self):
        """plugs that match a letter to itself is not allowed"""
        PB=PlugBoard()
        PB+=Plug('AB')
        with self.assertRaises(InvalidPlugError) as e:
            PB+=Plug('AA')
        exc = e.exception
        self.assertEqual("%s" % exc,"'AA'")

    def testPlugBoard_InvalidPlugError_5(self):
        """only plus with alpha chars are allowed, no numbers"""
        PB=PlugBoard()
        PB+=Plug('AB')
        with self.assertRaises(InvalidPlugError) as e:
            PB+=Plug('22')
        exc = e.exception
        self.assertEqual("%s" % exc,"'22'")

    def testPlugBoard_PlugBoardFullError(self):
        """only 10 plugs are allowed"""
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
        self.assertEqual(ret,"PlugBoard: 'AB IJ'")
        #self.assertEqual(ret,"Board=['B', 'A', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']\nPlugs=['A', 'B', 'I', 'J']")
        
    def testPlugBoard_PlugBoard_Iterator_1(self):
        PB=PlugBoard()
        PB = createPlugBoard(['AB', 'IJ', 'MN', 'TZ', 'QO', 'CP', 'DY', 'EX', 'FW', 'GV'])
        with self.assertRaises(IndexError) as e:
            for plug in PB:
                print(plug[2])
            
    def testPlug_getitem(self):
        P=Plug('AB')
        self.assertEqual('B', P[0])
        self.assertEqual('A', P[1])
            
    def testPlugBoard_encrypt(self):
        PB=PlugBoard()
        PB = createPlugBoard(['AB', 'IJ', 'MN', 'TZ', 'QO', 'CP', 'DY', 'EX', 'FW', 'GV'])
        self.assertEqual(PB('C'),'P')
        self.assertEqual(PB('P'),'C')
        self.assertEqual(PB('D'),'Y')
        self.assertEqual(PB('U'),'U')
    

if __name__ == '__main__': # pragma: no cover
    
    print("\nUnit Tests for Enigma Plugboard\n")
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPlugboard)
    unittest.TextTestRunner(verbosity=1).run(suite)
