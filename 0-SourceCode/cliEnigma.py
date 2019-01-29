#!/usr/bin/env python

import sys
from enigma import runTests
from Enigma.Rotors import RotorFactory, RotorPos, Left, Middle, Right
from Enigma.Reflectors import ReflectorFixed as Reflector
from Enigma.PlugBoard import PlugBoard
from Enigma.MachineDetails import Machines
from Enigma.EnigmaMachine import EnigmaMachine
from Enigma.Exceptions import InvalidRotorError, InvalidPlugError


def askUser():
    """ask the user to supply Enigma Machine details and the code."""
    print("There are 8 rotors to choose from identified by [I, II, III, IV, V, VI, VII].")
    print("You can set the position of the ring [A-Z] and also the position of the rotor [A-Z].")
    print("There are 2 reflectors to choose from identified by [B, C].")
    print("You can have up to 10 plugs for the plugboard.")
    print()
    
    stop = False
    macine = None
    while False == stop:
        rinput = input("Please Choose an Enigma Machine %s : " % list(Machines.keys()))
        if rinput in list(Machines.keys()):
            stop = True
            machine = rinput
    print(machine)
    RFactory = RotorFactory(Machines[machine])
    
    def createRotor(loc,default):
        stop = False
        while False == stop:
            try:
                rinput = input("Enter the %s Rotor details: ID Ring Rotor [%s] : " % (RotorPos[loc], default))
                if len(rinput) == 0:
                    rinput = default;
                if len(rinput.split(' ')) == 3:
                    #print("[%s]" % rinput)
                    stop = RFactory.createRotor(loc, rinput)
                else:
                    raise InvalidRotorError
            except InvalidRotorError as e:
                print(("Rotor details were invalid. Please try again.", e.value))
                
    for loc, default in ((Left,'I A A'),(Middle,'II A A'),(Right,'III A A')):
        createRotor(loc, default)
        
    def createReflector(default, str):
        if len(str) == 0:
            str = default
        if str in Machines[machine]['Reflectors']:
            return Reflector(Machines[machine], str)
        else:
            print(str,"not a reflector")
    reflector = createReflector('UKW-B', input("Choose a reflector [UKW-B] : "))
    
    def createPlugBoard(PB):
        stop = False
        count = 1
        while False == stop:
            try:
                plug = input("Add a Plug to the Plug Board (empty plug to end) [%s] : " % PB)
                if len(plug) == 2 and count < 10:
                    PB += Plug(plug)
                    count += 1
                else:
                    stop = True
            except (InvalidPlugError) as e:
                print(("Invalid Plug Error",e.value))
        return PB
    if Machines[machine]['Plugboard']:
        PB = createPlugBoard(PlugBoard())
    else:
        PB = createPlugBoard([])
    
    return EnigmaMachine(Machines[machine], RFactory,reflector,PB)
    
def codeMessage(Enigma):
    stop = False
    while False == stop:
        clue = input("\nEnter Message to Encode/Decode :")
        if clue == "":
            stop = True
        else:
            Enigma.reset()
            answer = Enigma.encrypt_message(clue.upper())
            print(("Answer: %s" % answer))
        
def usage():
    print("\nenigma [-h] [-t] [-i]\n")
    print("-i - Interactive. You will be asked a series of question to set the ")
    print("     options and then enter the message.")
    print("     There are 8 rotors to choose from identified by [I, II, III, IV, V, VI, VII].")
    print("     You can set the position of the ring with [A-Z]")
    print("     You can set the position of the rotor [A-Z].")
    print("     There are 2 reflectors to choose from identified by [B, C].")
    print("     You can have up to 10 plugs for the plugboard.")
    print("")
    print("-t - Test. Solve a standard set of test messages.")
    print("")
    print("-h - Help. Display this message.")
    print("")
    
def getOptions():
    import getopt
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hit", ["help", "test", "interactive"])
    except getopt.GetoptError as err:
        # print help information and exit:
        print((str(err))) # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
        
    options = {}
    verbose = False

    for o, a in opts:
        if o == "-v":
            opt['verbose'] = True
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-t", "--test"):
            runTests()
            sys.exit()
        elif o in ("-i", "--interactive"):
            codeMessage(askUser())
            sys.exit()
        else:
            assert False, "unhandled option"

    usage()
    
########################
# MAIN STARTS HERE
########################

if __name__ == '__main__':

    options = getOptions()
    