#!/usr/bin/env python

"""
NOT CURRENTLY USED
"""

from .MachineDetails import Machines
from .Rotors import RotorFactory
from .PlugBoard import PlugBoard
from .Exceptions import *
from .Keyboard import Keyboard
from .EntryDisc import EntryDisc


def createEnigmaMachine(machineId, rotorIds, ringSettings, rotorPositions, reflectorId, plugs):
    """"""
    print(machine)
    print(rotorIds)
    print(ringSettings)
    print(RotorPositions)
    print(reflectorId)
    print(plugs)
    
    if machineId in list(Machines.keys()):
        machine = Machine[machineId]
        
        reflector = Reflector(machine, reflectorId)
        plugboard = createPlugBoard(plugs) #could check for only I,M3,M4 machine have plug boards
        
        rotors = RotorFactory(machine)
        rotors.createRotor(Left,   "%s %s %s" % (rotorIds[0], ringSettings[0], rotorPositions[0]))
        rotors.createRotor(Middle, "%s %s %s" % (rotorIds[1], ringSettings[1], rotorPositions[2]))
        rotors.createRotor(Right,  "%s %s %s" % (rotorIds[2], ringSettings[2], rotorPositions[2]))
        Enigma = EnigmaMachine(machine, rotors, reflector, plugoard)
        
        return Enigma
        
        
class EnigmaMachine:
    """"""
    
    def __init__(self, machine):
        """"""
        self.machine = machine
        # keyboard
        #self.keyboard = Keyboard(machine, rotors, reflector)
        # plugboard
        self.plugboard = PlugBoard()
        # input wheel
        self.EntryDisc = EntryDisc(machine)
        # rotors
        self.rotor = RotorFactory(machine)
        # reflector
        if len(self.machine['Reflectors']) == 1:
            self.setReflector(self.machine['Reflectors'][0])
        
        
    def setRotor(self, loc, rid):
        """pick a rotor for a location"""
        if loc in validLocations and loc not in list(self.rotor.keys()):
            if rid in self.machine['Rotors']:
                self.rotor[loc] = createrid
            else:
                raise InvalidRotorError("Rotor %s not available for Enigma %s" % (rid, self.machine['shortname']))
        else:
            raise RotorLocationException("Location %s is not value." % loc)
            
    def getRotorId(self, loc):
        """get the id of a chosen rotor"""
        if loc in validLocations and loc not in list(self.rotor.keys()):
            if loc in list(self.rotor.keys()):
                return self.rotor[loc]
            else:
                raise InvalidRotorError("Rotor %s not set for Enigma %s" % (rid, self.machine['shortname']))
        else:
            raise RotorLocationException("Location %s is not value." % loc)
            
    def setRotorPosition(self, loc, position):
        """set the initial position of the rotor"""
        pass

    def setRotorRingSetting(self, loc, position):
        """set the ring setting of the rotor"""
        pass

    def addPlugs(self, plugs):
        if self.machine['Plugboard'] == True:
            if self.plugboard == None:
                self.plugboard = PlugBoard()
            for plug in plugs:
                self.plugboard += Plug(plug)
        else:
            raise PlugBoardNotSupported()

    def setReflector(self, refl):
        print(refl,"\n")
        pass


if __name__ == '__main__':
    
    for m in list(Machines.keys()):
        print(m)
        print(Machines[m]['ETW'])
        em = EnigmaMachine(Machines[m])
    
