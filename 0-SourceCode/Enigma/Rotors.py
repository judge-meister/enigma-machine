
"""
Enigma Rotor Wheels

        ROTORS
INPUT           ABCDEFGHIJKLMNOPQRSTUVWXYZ
Rotor I         EKMFLGDQVZNTOWYHXUSPAIBRCJ
Rotor II        AJDKSIRUXBLHWTMCQGZNPYFVOE
Rotor III       BDFHJLCPRTXVZNYEIWGAKMUSQO
Rotor IV        ESOVPZJAYQUIRHXLNFTGKDCMWB
Rotor V         VZBRGITYUPSDNHLXAWMJQOFECK
Rotor VI        JPGVOUMFYQBENHZRDKASXLICTW
Rotor VII       NZJHGRCXMYSWBOUFAIVLPEKQDT
Rotor VIII      FKQHTLXOCBJSPDZRAMEWNIUYGV
Beta rotor      LEYJVCNIXWPBQMDRTAKZGFUHOS
Gamma rotor     FSOKANUERHMBTIYCWLQPZXVGJD

Beta_rotor = "LEYJVCNIXWPBQMDRTAKZGFUHOS"
Gamma_rotor = "FSOKANUERHMBTIYCWLQPZXVGJD"
"""

import unittest
from .MachineDetails import Machines
from .AlphaUtils import ALPHA, alpha
from .Exceptions import InvalidRotorError

Greek = 3
Left = 2
Middle = 1
Right = 0

#Rotor_Perm = {'I':    "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
#              'II':   "AJDKSIRUXBLHWTMCQGZNPYFVOE",
#              'III':  "BDFHJLCPRTXVZNYEIWGAKMUSQO",
#              'IV':   "ESOVPZJAYQUIRHXLNFTGKDCMWB",
#              'V':    "VZBRGITYUPSDNHLXAWMJQOFECK",
#              'VI':   "JPGVOUMFYQBENHZRDKASXLICTW",
#              'VII':  "NZJHGRCXMYSWBOUFAIVLPEKQDT",
#              'VIII': "FKQHTLXOCBJSPDZRAMEWNIUYGV"
#             }
#RotorIds = Rotor_Perm.keys()
#RotorIds.sort()
#Rotor_Notch = {'I': 'R', 'II': 'F', 'III': 'W', 'IV': 'K',
#               'V': 'A', 'VI': 'AN', 'VII': 'AN', 'VIII': 'AN'
#              }
RotorPos = {Greek: "Greek", Left: "Left", Middle: "Middle", Right: "Right"}

# pylint: disable=too-many-instance-attributes
class RotorWheel(object):
    """A Rotor Wheel"""
    def __init__(self, machine, rid, loc, r_setting, offset, verbose=False):
        """initial values for the rotor wheel"""
        self.location = loc                     # position of rotor in enigma machine (L,M,R)
        self.ring_offset = alpha.pos(r_setting) # ring setting value (range 1 to 26)
        self.rotation = alpha.pos(offset)       # current rotation alignment during encryption
        self.default_rotation = self.rotation   # initial rotation alignment, allowing reset() to work
        self.rid = rid                          # rotor id (name eg. I, II, III etc)
        self.rotorCode = machine[rid]['wheel']  # rotor encryprion code
        #self.rotorNotch = machine[rid]['turnover'] # rotor notch locations
        self.rotorNotch = []
        if verbose: print("%s Turnover[%s] %s" % (loc,rid, machine[rid]['turnover']))
        for notch in machine[rid]['turnover']:
            #print notch
            self.rotorNotch.append(alpha.letter(alpha.normal(alpha.pos(notch))))
        self.offset = self.ring_offset - self.rotation # offset is the difference made to the rotor by 
                                                       # moving the ring away from the default location
        self.default_offset = self.offset       # used in reset to go back to the start
        self.forward = True                     # direction of travel of the encryption thru the rotor
        
    def __repr__(self):
        """print the rotor wheel, use: print RotorWheel"""
        ret = "rotor %2s = %s" % (self.rid, self.rotorCode)#Rotor_Perm[self.rid])
        ret += " " + repr(self.location)
        ret += " ring_setting = %d" % (self.ring_offset + 1)
        ret += " rotation = %d" % self.rotation
        return ret

    def __lt__(self, rotor):
        """use: 'if x<y:'"""
        return self.location < rotor.location
        
    def reset(self):
        """reset the position of the rotor wheel"""
        self.offset = self.default_offset
        self.rotation = self.default_rotation
        
    def rotate(self):
        """rotate the rotor 1 notch"""
        self.rotation = (self.rotation+1) % 26
        self.offset = self.ring_offset - self.rotation
        
    def setForward(self, direction):
        """set the circuit direction"""
        self.forward = direction
        
    def inNotchPosition(self):
        """is the rotor in the notch position"""
        return alpha.letter(alpha.normal(self.rotation)) in self.rotorNotch
        #return self.rotation+1 == alpha.pos(self.rotorNotch[0]) or \
        #       (len(self.rotorNotch) == 2 and \
        #        self.rotation + 1 == alpha.pos(self.rotorNotch[1]))
                
    def inNotchPositionG312(self):
        """is the rotor in the notch position"""
        #print "%-6s %s %s" % (RotorPos[self.location], alpha.letter(self.rotation), repr(self.rotorNotch))
        return alpha.letter(alpha.normal(self.rotation)) in self.rotorNotch
        
        
    #def encrypt(self, letter, dir):
    def __call__(self, letter, debug=False): #, dir):
        """use: 'RotorWheel(letter)'
        depending on the value of self.forward the rotor encryption will 
        work in each directions
        """
        encltr = letter
        # first remove the ring setting offset to find the actual contact letter to encrypt
        encltr = alpha.letter(alpha.normal(alpha.pos(encltr) - self.offset)) 
        if debug: print("in letter %s - remove offset(%d) %s " % (letter, self.offset, encltr), end=' ') 
        # encrypt the contact letter - forward or backward as necessary
        if self.forward:
            encltr = self.rotorCode[alpha.pos(encltr)]
        else:
            encltr = alpha.letter(self.rotorCode.index(encltr))
        if debug: print("rotor enc %s " % encltr, end=' ') 
        # re-add the ringsetting offset before returning the answer
        encltr = alpha.letter(alpha.normal(alpha.pos(encltr) + self.offset))
        if debug: print("adding offset(%d) %s" % (self.offset, encltr))
        return encltr
        

class RotorFactory(object):
    """RotorFactory"""
    def __init__(self, machine):
        # Machine should be a dictionary
        if isinstance(machine, dict) == False:
            raise TypeError
        self.machine = machine
        self.RotorList = []
        self.RotorDict = {}
        self.RotorPos = []
        
    def __iadd__(self, rotordetails):
        """use: 'rotorfactory += rotor'"""
        loc, rotor = rotordetails
        self.RotorDict[loc] = rotor
        self.RotorPos.append(loc)
        self.RotorList.append(rotor)
        self.RotorList.sort()
        return self
        
    def __iter__(self):
        """use: 'for x in rotorfactory:'"""
        for rotor in self.RotorList:
            yield rotor
        
    def __reversed__(self):
        """use: 'for x in reversed(rotorfactory)'"""
        for rotor in self.RotorList[::-1]:
            yield rotor
        
    def __getitem__(self, loc):
        """use: rotorfactory[1]"""
        return self.RotorDict[loc]
        
    def __repr__(self):
        return "Rotor Factory - Set Reverse Route"

    def setForward(self):
        """set the circuit direction"""
        for rotor in self.RotorList:
            rotor.setForward(True)
        
    def setBackward(self):
        """set the circuit direction"""
        for rotor in self.RotorList:
            rotor.setForward(False)
        
    def createRotor(self, loc, string):
        """create a rotor"""
        if len(string.split(' ')) != 3:
            raise InvalidRotorError("Not enough details")
        rid, ring, rotor = string.split(' ')
        #print rid, ring, rotor
        if rid in self.machine['Rotors'] and \
            ring in ALPHA and \
            loc not in self.RotorPos \
            and rotor in ALPHA:
            RW = RotorWheel(self.machine, rid, loc, ring, rotor)
            self += (loc, RW)
        else:
            raise InvalidRotorError("Invalid details")
        return True
        
    def __call__(self, ltr, debug=False):
        """use: 'rotorfactory(letter)'"""
        self.setBackward()
        return ltr



class TestRotors(unittest.TestCase):
        
    def testRotorI_P_A_W(self):
        RW = RotorWheel(Machines['M3'],'I',"Right",'P','A') # 16,0
        RW.rotate()
        #print "Rotor I - for - W should become J",RW.encrypt("W",'F')
        self.assertEqual("J",RW("W"))#,'F'))
        
    def testRotorI_P_A_V(self):
        RW = RotorWheel(Machines['M3'],'I',"Right",'P','A') # 16,0
        RW.rotate()
        RW.setForward(False)
        #print "Rotor I - rev - V should become D",RW.encrypt("V",'R'),"\n"
        self.assertEqual("D",RW("V"))#,'R'))
    
    def testRotorVI_G_A_J(self):
        RW = RotorWheel(Machines['M3'],'VI',"Middle",'G','A') # 7,0
        #print "Rotor VI - for - J should become B",RW.encrypt("J",'F')
        self.assertEqual("B",RW("J"))#,'F'))
        
    def testRotorVI_G_A_X(self):
        RW = RotorWheel(Machines['M3'],'VI',"Middle",'G','A') # 7,0
        #print "Rotor VI - rev - X should become V",RW.encrypt("X",'R'),"\n"
        RW.setForward(False)
        self.assertEqual("V",RW("X"))#,'R'))
    
    def testRotorV_G_A_V(self):
        RW = RotorWheel(Machines['M3'],'V',"Left",'G','A') # 7,0
        #RW.printSettings()
        #print "Rotor V - for - B should become U",RW.encrypt("B",'F')
        self.assertEqual("U",RW("B"))#,'F'))
        
    def testRotorV_G_A_C(self):
        RW = RotorWheel(Machines['M3'],'V',"Left",'G','A') # 7,0
        RW.setForward(False)
        #RW.printSettings()
        #print "Rotor V - rev - C should become X",RW.encrypt("C",'R'),"\n"
        self.assertEqual("X",RW("C"))#,'R'))


    def testRotorRotation(self):
        #print "Testing Rotor Rotation roll-over"
        RW = RotorWheel(Machines['M3'],'I','Right','A','A')
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
        RW = RotorWheel(Machines['M3'],'I','Right','A','A')
        ret = "%s" % RW
        self.assertEqual(ret,"rotor  I = EKMFLGDQVZNTOWYHXUSPAIBRCJ 'Right' ring_setting = 1 rotation = 0")
        
    def testRotorWheel_Reset(self):
        RW = RotorWheel(Machines['M3'],'I','Right','A','A')
        RW.rotate()
        self.assertEqual(RW.rotation,1)
        self.assertEqual(RW.offset,-1)
        RW.reset()
        self.assertEqual(RW.rotation,0)
        self.assertEqual(RW.offset,0)
        
    def testRotorFactory_Invalid_Rotor_Details(self):
        RF=RotorFactory(Machines['M3'])
        with self.assertRaises(InvalidRotorError) as e:
            RF.createRotor(Left,   "I A A A")
        exc = e.exception
        self.assertEqual("%s" % exc,"'Not enough details'")
        
    def testRotorFactory_Invalid_Rotor_Id(self):
        RF=RotorFactory(Machines['M3'])
        with self.assertRaises(InvalidRotorError) as e:
            RF.createRotor(Left,   "T A A")
        exc = e.exception
        self.assertEqual("%s" % exc,"'Invalid details'")


if __name__ == '__main__': # pragma: no cover
    
    print("\nUnit Tests for Enigma Rotors\n")
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRotors)
    unittest.TextTestRunner(verbosity=2).run(suite)
    
    
"""    
    2 Turnover[III] AEFHKMNRUWX
    1 Turnover[II] ACDFGHKMNQSTVYZ
    0 Turnover[I] ABCEFGIKLOPQSUVWZ


III A   EF H  K MN   R  U WX
       DE                       
II  A CD FGH  K MN  Q ST V  YZ
         FG                       
I   ABC EFG I KL  OPQ S UVW  Z
          GH                    

BBB
BCC
CDD
CDE
DEF
DFG
EGH
"""
    