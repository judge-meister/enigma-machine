#!/usr/bin/env python

import sys


class colors:
    
    BLACK='\033[0;30m'
    DARKRED='\033[0;31m'
    DARKGREEN='\033[0;32m'
    BROWN='\033[0;33m'
    DARKBLUE='\033[0;34m'
    PURPLE='\033[0;35m'
    CYAN='\033[0;36m'
    LIGHTGREY='\033[0;37m'

    DARKGREY='\033[01;30m'
    RED='\033[01;31m'
    GREEN='\033[01;32m'
    YELLOW='\033[01;33m'
    BLUE='\033[01;34m'
    PINK='\033[01;35m'
    LIGHTCYAN='\033[01;36m'
    WHITE='\033[01;37m'

    NOCOL='\033[00m'
    
cdict = {
    "BLACK":colors.BLACK,
    "DARKRED":colors.DARKRED,
    "DARKGREEN":colors.DARKGREEN,
    "BROWN":colors.BROWN,
    "DARKBLUE":colors.DARKBLUE,
    "PURPLE":colors.PURPLE,
    "CYAN":colors.CYAN,
    "LIGHTGREY":colors.LIGHTGREY,
    "DARKGREY":colors.DARKGREY,
    "RED":colors.RED,
    "GREEN":colors.GREEN,
    "YELLOW":colors.YELLOW,
    "BLUE":colors.BLUE,
    "PINK":colors.PINK,
    "LIGHTCYAN":colors.LIGHTCYAN,
    "WHITE":colors.WHITE,
    "NOCOL":colors.NOCOL
}



print "["+colors.BLACK+"BLACK"+colors.NOCOL+"]",
print "["+colors.DARKRED+"DARKRED"+colors.NOCOL+"]",
print "["+colors.DARKGREEN+"DARKGREEN"+colors.NOCOL+"]",
print "["+colors.BROWN+"BROWN"+colors.NOCOL+"]",
print "["+colors.DARKBLUE+"DARKBLUE"+colors.NOCOL+"]",
print "["+colors.PURPLE+"PURPLE"+colors.NOCOL+"]",
print "["+colors.CYAN+"CYAN"+colors.NOCOL+"]",
print "["+colors.LIGHTGREY+"LIGHTGREY"+colors.NOCOL+"]",
print "["+colors.DARKGREY+"DARKGREY"+colors.NOCOL+"]",
print "["+colors.RED+"RED"+colors.NOCOL+"]",
print "["+colors.GREEN+"GREEN"+colors.NOCOL+"]",
print "["+colors.YELLOW+"YELLOW"+colors.NOCOL+"]",
print "["+colors.BLUE+"BLUE"+colors.NOCOL+"]",
print "["+colors.PINK+"PINK"+colors.NOCOL+"]",
print "["+colors.LIGHTCYAN+"LIGHTCYAN"+colors.NOCOL+"]",
print "["+colors.WHITE+"WHITE"+colors.NOCOL+"]",
print "["+colors.NOCOL+"NOCOL"+"]",


data = """
============================================================
                  Ring
                 Setting
Left   Rotor V    +0 (A)      This is a default ring setting
Middle Rotor VI   +0 (A)      of 0 for each rotor. Ring Setting
Right  Rotor I    +0 (A)      has no effect. Standard Behaviour.
Plug Board EO FP LY

Keyboard Press 'W'
Lights UP 'N'
                         [N]      [W]  
                          ^        V   
PlugBoard:   ABCDEFGHIJKLMNOPQRSTUV$BLUE$W$NOCOL$XYZ
             ABCDOPGHIJKYMNEFQRSTUV$BLUE$W$NOCOL$XLZ
                          ^        V   
             --------------------------
                         ^         V   
             bcdefghijklmnopqrstuvw$BLUE$x$NOCOL$yza <- 1 step makes W become X
Ring +0      BCDEFGHIJKLMNOPQRSTUVW$BLUE$X$NOCOL$YZA
                         ^         V   
             BCDEFGHIJKLMNOPQRSTUVW$BLUE$X$NOCOL$YZA <- 1 step makes W become X
Rotor I:     KMFLGDQVZNTOWYHXUSPAIB$BLUE$R$NOCOL$CJE <- returning route also makes O becomes W 
                         ^         V   
                          ^  V        
Ring +0      BCDEFGHIJKLMNOPQ$BLUE$R$NOCOL$STUVWXYZA
             bcdefghijklmnopq$BLUE$r$NOCOL$stuvwxyza
                          ^  V        
             --------------------------
                           ^  V        
             abcdefghijklmnopqrstuvwxyz
Ring +0      ABCDEFGHIJKLMNOPQRSTUVWXYZ
                           ^  V        
             ABCDEFGHIJKLMNOPQRSTUVWXYZ
Rotor VI:    JPGVOUMFYQBENHZRDKASXLICTW
                           ^  V        
                       V              ^
Ring +0      ABCDEFGHIJKLMNOPQRSTUVWXYZ
             abcdefghijklmnopqrstuvwxyz
                       V              ^
             --------------------------
                       V              ^
             abcdefghijklmnopqrstuvwxyz
Ring +0      ABCDEFGHIJKLMNOPQRSTUVWXYZ
                       V              ^
             ABCDEFGHIJKLMNOPQRSTUVWXYZ
Rotor V:     VZBRGITYUPSDNHLXAWMJQOFECK
                       V              ^
                       ^       V       
Ring +0      ABCDEFGHIJKLMNOPQRSTUVWXYZ
             abcdefghijklmnopqrstuvwxyz
                       ^       V       
             --------------------------
                       ^       V       
             ABCDEFGHIJKLMNOPQRSTUVWXYZ
Reflector B: LEYJVCNIXWPBQMDRTAKZGFUHOS

============================================================
                  Ring
                 Setting
Left   Rotor V    +6 (G)      Now with a positive ring
Middle Rotor VI   +6 (G)      setting we add more complexity
Right  Rotor I   +15 (P)
Plug Board EO FP LY

Keyboard Press 'W'
Lights UP 'D'
               [D]                [W]  
                ^                  V   
PlugBoard:   ABCDEFGHIJKLMNOPQRSTUVWXYZ
             ABCDOPGHIJKYMNEFQRSTUVWXLZ
                ^                  V   
             --------------------------  interface between plugboard and rotor
               ^                   V  
             bcdefghijklmnopqrstuvwxyza  <- 1 step makes W become X
Ring +15     MNOPQRSTUVWXYZABCDEFGHIJKL 
               ^                   V   
                     V     ^           
             ABCDEFGHIJKLMNOPQRSTUVWXYZ  <- 1 step makes W become X
Rotor I:     EKMFLGDQVZNTOWYHXUSPAIBRCJ
                     V     ^         
                       V  ^            
Ring +15     LMNOPQRSTUVWXYZABCDEFGHIJK
             bcdefghijklmnopqrstuvwxyza
                       V  ^            
             --------------------------  interface between rotors
                       V  ^             
             abcdefghijklmnopqrstuvwxyz
Ring +6      UVWXYZABCDEFGHIJKLMNOPQRST
                       V  ^            
                 V  ^                  
             ABCDEFGHIJKLMNOPQRSTUVWXYZ
Rotor VI:    JPGVOUMFYQBENHZRDKASXLICTW
                 V  ^                  
                        ^        V     
Ring +6      UVWXYZABCDEFGHIJKLMNOPQRST
             abcdefghijklmnopqrstuvwxyz
                        ^        V     
             --------------------------  interface between rotors
                        ^        V     
             abcdefghijklmnopqrstuvwxyz
Ring +6      UVWXYZABCDEFGHIJKLMNOPQRST
                        ^        V     
                  ^        V           
             ABCDEFGHIJKLMNOPQRSTUVWXYZ
Rotor V:     VZBRGITYUPSDNHLXAWMJQOFECK
                  ^        V           
                     ^  V              
             abcdefghijklmnopqrstuvwxyz
Ring +6      UVWXYZABCDEFGHIJKLMNOPQRST
                     ^  V              
             --------------------------  interface between rotor and reflector
               ^  V                    
             ABCDEFGHIJKLMNOPQRSTUVWXYZ
Reflector B: LEYJVCNIXWPBQMDRTAKZGFUHOS
             --------------------------

"""

for x in cdict.keys():
    data=data.replace("$%s$"%x,cdict[x])
    
print data