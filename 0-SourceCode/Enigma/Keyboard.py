
"""
Enigma Keyboard
"""

import unittest
from .Rotors import Left, Middle, Right
from .AlphaUtils import alpha

def Keyboard(machine, rotors, reflector):
    if machine['basetype'] == 'G':
        return KeyboardGear(rotors, reflector)
    else:
        return KeyboardPawl(rotors, reflector)
    

class KeyboardPawl(object):
    """
    Keyboard class for a machine with a pawl based wheel turnover mechanism.
    
    The Keyboard - When a key is pressed the pawls push any rotor wheels they 
    are engaged with. 
    Pawl 1 is only resting against the ratchet of the left rotor.
    Pawl 2 is resting against the notch of the right rotor and the ratchet of 
    the middle rotor.
    Pawl 3 is resting against the notch of the middle rotor and the ratchet of 
    the left rotor.
    """
    def __init__(self, Rotors, Reflector=None):
        self.Rotors = Rotors
        self.Reflector = Reflector
        
    def press(self):
        """Always rotate the right rotor. Check whether middle or left rotors 
        should also rotate."""
        rotateMiddle = rotateLeft = False
        
        if self.Rotors[Right].inNotchPosition(): #rotate middle and right rotors
            rotateMiddle = True 
            
        if self.Rotors[Middle].inNotchPosition(): #rotate left and middle rotors
            rotateLeft = True 
            rotateMiddle = True
            
        self.Rotors[Right].rotate()
        
        if rotateMiddle: 
            self.Rotors[Middle].rotate()
            
        if rotateLeft: 
            self.Rotors[Left].rotate()


class KeyboardGear(object):
    """
    Keyboard class for a machine with a cog based wheel turnover mechanism.
    
    The Keyboard - When a key is pressed the right most rotor is moved by 1
    position and if it was previously aligned with a notch then causes the
    movement of the middle rotor.  If the middle rotor moves and is also
    aligned with a notch then the left rotor moves.  The left rotor can only
    move if both the right and middle rotor are aligned and move together.
    Lastly if the left rotor moves and is aligned with a notch then the 
    Reflector will move.
    """
    def __init__(self, Rotors, Reflector=None):
        self.Rotors = Rotors
        self.Reflector = Reflector
        
    def press(self):
        """Always rotate the right rotor. Check whether middle or left rotors 
        should also rotate."""
        rotateMiddle = rotateLeft = rotateReflector = False
        
        RinNotch = self.Rotors[Right].inNotchPositionG312()
        #print "Right  rotor in notch:", inNotch
        if RinNotch: #rotate middle and right rotors
            rotateMiddle = True 
            
        MinNotch = self.Rotors[Middle].inNotchPositionG312()
        #print "Middle rotor in notch:", inNotch
        if RinNotch and MinNotch: #rotate left and middle rotors
            rotateLeft = True 
            #rotateMiddle = True 
            
        LinNotch = self.Rotors[Left].inNotchPositionG312()
        if LinNotch and MinNotch and RinNotch:
            rotateReflector = True
            
        # always more the right
        self.Rotors[Right].rotate()
        
        if rotateMiddle: 
            self.Rotors[Middle].rotate()
            
        if rotateLeft: 
            self.Rotors[Left].rotate()

        #print rotateReflector, self.Reflector
        if rotateReflector and self.Reflector != None:
            self.Reflector.rotate()


class TestKeyboard(unittest.TestCase):
    
    def createMachine(self):
        from .Rotors import RotorFactory
        from .MachineDetails import Machines
        RF=RotorFactory(Machines['M3'])
        RF.createRotor(Left,   "I A A")   # notch Q (17)
        RF.createRotor(Middle, "II A A")  # notch E (5)
        RF.createRotor(Right,  "III A A") # notch V (22)
        KB = KeyboardPawl(RF)
        return KB
        

    def test_middle_rotor_notch(self):
        #print "Testing Keyboard"
        KB = self.createMachine()
        results = ["A A B", "A A C", "A A D", "A A E", "A A F", "A A G", "A A H", "A A I", "A A J", "A A K", "A A L", "A A M", "A A N", "A A O", "A A P", "A A Q", "A A R", "A A S", "A A T", "A A U", "A A V", "A B W", "A B X", "A B Y", "A B Z", "A B A", "A B B", "A B C", "A B D", "A B E", "A B F", "A B G", "A B H", "A B I", "A B J", "A B K", "A B L", "A B M", "A B N", "A B O", "A B P", "A B Q", "A B R", "A B S", "A B T", "A B U", "A B V", "A C W", "A C X", "A C Y", "A C Z", "A C A", "A C B", "A C C", "A C D", "A C E", "A C F", "A C G", "A C H", "A C I", "A C J", "A C K", "A C L", "A C M", "A C N", "A C O", "A C P", "A C Q", "A C R", "A C S", "A C T", "A C U", "A C V", "A D W", "A D X", "A D Y", "A D Z", "A D A", "A D B", "A D C", "A D D", "A D E", "A D F", "A D G", "A D H", "A D I", "A D J", "A D K", "A D L", "A D M", "A D N", "A D O", "A D P", "A D Q", "A D R", "A D S", "A D T", "A D U", "A D V", "A E W", "B F X", "B F Y"]
        for x in range(102):#(752):
            KB.press()
            letters = "%s %s %s" % (alpha.letter(KB.Rotors[Left].rotation),alpha.letter(KB.Rotors[Middle].rotation),alpha.letter(KB.Rotors[Right].rotation))
            #print "%2d - %s" % (x, letters)
            #print '"%s",' %(letters),
            self.assertEqual(letters, results[x])
            
            if x == 20:
                #print(KB.Rotors[Left].rotation,KB.Rotors[Middle].rotation,KB.Rotors[Right].rotation)
                self.assertEqual(0, KB.Rotors[Left].rotation)
                self.assertEqual(0, KB.Rotors[Middle].rotation) 
                self.assertEqual(21,KB.Rotors[Right].rotation)
            if x == 21:
                #print(KB.Rotors[Left].rotation,KB.Rotors[Middle].rotation,KB.Rotors[Right].rotation)
                self.assertEqual(0, KB.Rotors[Left].rotation)
                self.assertEqual(1, KB.Rotors[Middle].rotation)
                self.assertEqual(22,KB.Rotors[Right].rotation)
            if x == 46:
                #print(KB.Rotors[Left].rotation,KB.Rotors[Middle].rotation,KB.Rotors[Right].rotation)
                self.assertEqual(0, KB.Rotors[Left].rotation)
                self.assertEqual(1, KB.Rotors[Middle].rotation) 
                self.assertEqual(21,KB.Rotors[Right].rotation)
            if x == 47:
                #print(KB.Rotors[Left].rotation,KB.Rotors[Middle].rotation,KB.Rotors[Right].rotation)
                self.assertEqual(0, KB.Rotors[Left].rotation)
                self.assertEqual(2, KB.Rotors[Middle].rotation)
                self.assertEqual(22,KB.Rotors[Right].rotation)
            if x == 72:
                #print(KB.Rotors[Left].rotation,KB.Rotors[Middle].rotation,KB.Rotors[Right].rotation)
                self.assertEqual(0, KB.Rotors[Left].rotation)
                self.assertEqual(2, KB.Rotors[Middle].rotation)
                self.assertEqual(21,KB.Rotors[Right].rotation)
            if x == 73:
                #print(KB.Rotors[Left].rotation,KB.Rotors[Middle].rotation,KB.Rotors[Right].rotation)
                self.assertEqual(0, KB.Rotors[Left].rotation)
                self.assertEqual(3, KB.Rotors[Middle].rotation)
                self.assertEqual(22,KB.Rotors[Right].rotation)
            if x == 98:
                #print(KB.Rotors[Left].rotation,KB.Rotors[Middle].rotation,KB.Rotors[Right].rotation)
                self.assertEqual(0, KB.Rotors[Left].rotation)
                self.assertEqual(3, KB.Rotors[Middle].rotation)
                self.assertEqual(21,KB.Rotors[Right].rotation)
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
        
        
    def test_left_rotor_notch(self):
        #print "Testing Keyboard"
        KB = self.createMachine()
        results = ["A A B", "A A C", "A A D", "A A E", "A A F", "A A G", "A A H", "A A I", "A A J", "A A K", "A A L", "A A M", "A A N", "A A O", "A A P", "A A Q", "A A R", "A A S", "A A T", "A A U", "A A V", "A B W", "A B X", "A B Y", "A B Z", "A B A", "A B B", "A B C", "A B D", "A B E", "A B F", "A B G", "A B H", "A B I", "A B J", "A B K", "A B L", "A B M", "A B N", "A B O", "A B P", "A B Q", "A B R", "A B S", "A B T", "A B U", "A B V", "A C W", "A C X", "A C Y", "A C Z", "A C A", "A C B", "A C C", "A C D", "A C E", "A C F", "A C G", "A C H", "A C I", "A C J", "A C K", "A C L", "A C M", "A C N", "A C O", "A C P", "A C Q", "A C R", "A C S", "A C T", "A C U", "A C V", "A D W", "A D X", "A D Y", "A D Z", "A D A", "A D B", "A D C", "A D D", "A D E", "A D F", "A D G", "A D H", "A D I", "A D J", "A D K", "A D L", "A D M", "A D N", "A D O", "A D P", "A D Q", "A D R", "A D S", "A D T", "A D U", "A D V", "A E W", "B F X", "B F Y", "B F Z", "B F A", "B F B", "B F C", "B F D", "B F E", "B F F", "B F G", "B F H", "B F I", "B F J", "B F K", "B F L", "B F M", "B F N", "B F O", "B F P", "B F Q", "B F R", "B F S", "B F T", "B F U", "B F V", "B G W", "B G X", "B G Y", "B G Z", "B G A", "B G B", "B G C", "B G D", "B G E", "B G F", "B G G", "B G H", "B G I", "B G J", "B G K", "B G L", "B G M", "B G N", "B G O", "B G P", "B G Q", "B G R", "B G S", "B G T", "B G U", "B G V", "B H W", "B H X", "B H Y", "B H Z", "B H A", "B H B", "B H C", "B H D", "B H E", "B H F", "B H G", "B H H", "B H I", "B H J", "B H K", "B H L", "B H M", "B H N", "B H O", "B H P", "B H Q", "B H R", "B H S", "B H T", "B H U", "B H V", "B I W", "B I X", "B I Y", "B I Z", "B I A", "B I B", "B I C", "B I D", "B I E", "B I F", "B I G", "B I H", "B I I", "B I J", "B I K", "B I L", "B I M", "B I N", "B I O", "B I P", "B I Q", "B I R", "B I S", "B I T", "B I U", "B I V", "B J W", "B J X", "B J Y", "B J Z", "B J A", "B J B", "B J C", "B J D", "B J E", "B J F", "B J G", "B J H", "B J I", "B J J", "B J K", "B J L", "B J M", "B J N", "B J O", "B J P", "B J Q", "B J R", "B J S", "B J T", "B J U", "B J V", "B K W", "B K X", "B K Y", "B K Z", "B K A", "B K B", "B K C", "B K D", "B K E", "B K F", "B K G", "B K H", "B K I", "B K J", "B K K", "B K L", "B K M", "B K N", "B K O", "B K P", "B K Q", "B K R", "B K S", "B K T", "B K U", "B K V", "B L W", "B L X", "B L Y", "B L Z", "B L A", "B L B", "B L C", "B L D", "B L E", "B L F", "B L G", "B L H", "B L I", "B L J", "B L K", "B L L", "B L M", "B L N", "B L O", "B L P", "B L Q", "B L R", "B L S", "B L T", "B L U", "B L V", "B M W", "B M X", "B M Y", "B M Z", "B M A", "B M B", "B M C", "B M D", "B M E", "B M F", "B M G", "B M H", "B M I", "B M J", "B M K", "B M L", "B M M", "B M N", "B M O", "B M P", "B M Q", "B M R", "B M S", "B M T", "B M U", "B M V", "B N W", "B N X", "B N Y", "B N Z", "B N A", "B N B", "B N C", "B N D", "B N E", "B N F", "B N G", "B N H", "B N I", "B N J", "B N K", "B N L", "B N M", "B N N", "B N O", "B N P", "B N Q", "B N R", "B N S", "B N T", "B N U", "B N V", "B O W", "B O X", "B O Y", "B O Z", "B O A", "B O B", "B O C", "B O D", "B O E", "B O F", "B O G", "B O H", "B O I", "B O J", "B O K", "B O L", "B O M", "B O N", "B O O", "B O P", "B O Q", "B O R", "B O S", "B O T", "B O U", "B O V", "B P W", "B P X", "B P Y", "B P Z", "B P A", "B P B", "B P C", "B P D", "B P E", "B P F", "B P G", "B P H", "B P I", "B P J", "B P K", "B P L", "B P M", "B P N", "B P O", "B P P", "B P Q", "B P R", "B P S", "B P T", "B P U", "B P V", "B Q W", "B Q X", "B Q Y", "B Q Z", "B Q A", "B Q B", "B Q C", "B Q D", "B Q E", "B Q F", "B Q G", "B Q H", "B Q I", "B Q J", "B Q K", "B Q L", "B Q M", "B Q N", "B Q O", "B Q P", "B Q Q", "B Q R", "B Q S", "B Q T", "B Q U", "B Q V", "B R W", "B R X", "B R Y", "B R Z", "B R A", "B R B", "B R C", "B R D", "B R E", "B R F", "B R G", "B R H", "B R I", "B R J", "B R K", "B R L", "B R M", "B R N", "B R O", "B R P", "B R Q", "B R R", "B R S", "B R T", "B R U", "B R V", "B S W", "B S X", "B S Y", "B S Z", "B S A", "B S B", "B S C", "B S D", "B S E", "B S F", "B S G", "B S H", "B S I", "B S J", "B S K", "B S L", "B S M", "B S N", "B S O", "B S P", "B S Q", "B S R", "B S S", "B S T", "B S U", "B S V", "B T W", "B T X", "B T Y", "B T Z", "B T A", "B T B", "B T C", "B T D", "B T E", "B T F", "B T G", "B T H", "B T I", "B T J", "B T K", "B T L", "B T M", "B T N", "B T O", "B T P", "B T Q", "B T R", "B T S", "B T T", "B T U", "B T V", "B U W", "B U X", "B U Y", "B U Z", "B U A", "B U B", "B U C", "B U D", "B U E", "B U F", "B U G", "B U H", "B U I", "B U J", "B U K", "B U L", "B U M", "B U N", "B U O", "B U P", "B U Q", "B U R", "B U S", "B U T", "B U U", "B U V", "B V W", "B V X", "B V Y", "B V Z", "B V A", "B V B", "B V C", "B V D", "B V E", "B V F", "B V G", "B V H", "B V I", "B V J", "B V K", "B V L", "B V M", "B V N", "B V O", "B V P", "B V Q", "B V R", "B V S", "B V T", "B V U", "B V V", "B W W", "B W X", "B W Y", "B W Z", "B W A", "B W B", "B W C", "B W D", "B W E", "B W F", "B W G", "B W H", "B W I", "B W J", "B W K", "B W L", "B W M", "B W N", "B W O", "B W P", "B W Q", "B W R", "B W S", "B W T", "B W U", "B W V", "B X W", "B X X", "B X Y", "B X Z", "B X A", "B X B", "B X C", "B X D", "B X E", "B X F", "B X G", "B X H", "B X I", "B X J", "B X K", "B X L", "B X M", "B X N", "B X O", "B X P", "B X Q", "B X R", "B X S", "B X T", "B X U", "B X V", "B Y W", "B Y X", "B Y Y", "B Y Z", "B Y A", "B Y B", "B Y C", "B Y D", "B Y E", "B Y F", "B Y G", "B Y H", "B Y I", "B Y J", "B Y K", "B Y L", "B Y M", "B Y N", "B Y O", "B Y P", "B Y Q", "B Y R", "B Y S", "B Y T", "B Y U", "B Y V", "B Z W", "B Z X", "B Z Y", "B Z Z", "B Z A", "B Z B", "B Z C", "B Z D", "B Z E", "B Z F", "B Z G", "B Z H", "B Z I", "B Z J", "B Z K", "B Z L", "B Z M", "B Z N", "B Z O", "B Z P", "B Z Q", "B Z R", "B Z S", "B Z T", "B Z U", "B Z V", "B A W", "B A X", "B A Y", "B A Z", "B A A", "B A B", "B A C", "B A D", "B A E", "B A F", "B A G", "B A H", "B A I", "B A J", "B A K", "B A L", "B A M", "B A N", "B A O", "B A P", "B A Q", "B A R", "B A S", "B A T", "B A U", "B A V", "B B W", "B B X", "B B Y", "B B Z", "B B A", "B B B", "B B C", "B B D", "B B E", "B B F", "B B G", "B B H", "B B I", "B B J", "B B K", "B B L", "B B M", "B B N", "B B O", "B B P", "B B Q", "B B R", "B B S", "B B T", "B B U", "B B V", "B C W", "B C X", "B C Y", "B C Z", "B C A", "B C B", "B C C", "B C D", "B C E", "B C F", "B C G", "B C H", "B C I", "B C J", "B C K", "B C L", "B C M", "B C N", "B C O", "B C P", "B C Q", "B C R", "B C S", "B C T", "B C U", "B C V", "B D W", "B D X", "B D Y", "B D Z", "B D A", "B D B", "B D C", "B D D", "B D E", "B D F", "B D G", "B D H", "B D I", "B D J", "B D K", "B D L", "B D M", "B D N", "B D O", "B D P", "B D Q", "B D R", "B D S", "B D T", "B D U", "B D V", "B E W", "C F X", "C F Y"]
        for x in range(752):#102):#(752):
            KB.press()
            letters = "%s %s %s" % (alpha.letter(KB.Rotors[Left].rotation),alpha.letter(KB.Rotors[Middle].rotation),alpha.letter(KB.Rotors[Right].rotation))
            #print "%2d - %s" % (x, letters)
            #print '"%s",' %(letters),
            self.assertEqual(letters, results[x])
            
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
            if x == 748:
                #print(KB.Rotors[Left].rotation,KB.Rotors[Middle].rotation,KB.Rotors[Right].rotation)
                self.assertEqual(1, KB.Rotors[Left].rotation)   
                self.assertEqual(3, KB.Rotors[Middle].rotation) 
                self.assertEqual(21,KB.Rotors[Right].rotation)
            if x == 749:
                #print(KB.Rotors[Left].rotation,KB.Rotors[Middle].rotation,KB.Rotors[Right].rotation)
                self.assertEqual(1, KB.Rotors[Left].rotation)
                self.assertEqual(4, KB.Rotors[Middle].rotation)
                self.assertEqual(22,KB.Rotors[Right].rotation)
            if x == 750:
                #print(KB.Rotors[Left].rotation,KB.Rotors[Middle].rotation,KB.Rotors[Right].rotation)
                self.assertEqual(2, KB.Rotors[Left].rotation)
                self.assertEqual(5, KB.Rotors[Middle].rotation)
                self.assertEqual(23,KB.Rotors[Right].rotation)
        

    def create_G312_Machine(self):
        """"""
        from .Rotors import RotorFactory
        from .MachineDetails import Machines
        #print "Create G312 Machine\n"
        machine = Machines['G312']
        #print "Left  ", machine['III']['turnover']
        #print "Middle", machine['II']['turnover']
        #print "Right ", machine['I']['turnover']
        RF = RotorFactory(machine)
        RF.createRotor(Left,  "III A A")
        RF.createRotor(Middle, "II A A")
        RF.createRotor(Right,   "I A A")
        KB = KeyboardGear(RF)
        #Enigma = EnigmaMachine (machine, RF, ReflectorRotating(machine, "uG", 'A', 'A'), None)
        return KB


    def test_G312_rotors(self):
        from .AlphaUtils import alpha
        KB = self.create_G312_Machine()
        #RIGHT  -  A B C   E F G   I   K L     O P Q   S   U V W     Z
        #MIDDLE -  A   C D   F G H     K   M N     Q   S T   V     Y Z
        #print "R - A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
        #print "M - A B C D D E F F G G H I I I J K L L M M N O P P P Q"
        #print "L - A B B C C D D E E F F G G G G G H H H I I J J J J K"
        results = ["A A A", "B B B", "B C C", "C D D", "C D E", "D E F", "D F G", "E G H", "E G I", "F H J", 
                   "F H K", "G I L", "G J M", "G J N", "G J O", "G K P", "H L Q", "H M R", "H M S", "I N T", 
                   "I N U", "J O V", "J P W", "J Q X", "J Q Y", "J Q Z", "K R A"]
        #print " 0 -",alpha.letter(KB.Rotors[Left].rotation),alpha.letter(KB.Rotors[Middle].rotation),alpha.letter(KB.Rotors[Right].rotation)
        for x in range(1,27):#102):#(752):
            KB.press()
            letters = "%s %s %s" % (alpha.letter(KB.Rotors[Left].rotation),alpha.letter(KB.Rotors[Middle].rotation),alpha.letter(KB.Rotors[Right].rotation))
            #print "%2d - %s" % (x, letters)# KB.Rotors[Left].rotation, KB.Rotors[Middle].rotation, KB.Rotors[Right].rotation,
            #print letters
            self.assertEqual(letters, results[x])



if __name__ == '__main__': # pragma: no cover
    
    print("\nUnit Tests for Enigma Notch Rotation\n")
    suite = unittest.TestLoader().loadTestsFromTestCase(TestKeyboard)
    unittest.TextTestRunner(verbosity=1).run(suite)
