#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Command Line Iinterface + Graphical User Interface

choose an enigma machine type
list rotors from chosen machine
find number of rotors to choose
user chooses rotors - check for duplicate rotor wheel choices
list reflectors - standard are easy, I, M3
                - M4 list combinations of static and greek (4 combos)
                - Railway has rotatable reflector (no notches though)
if plugboard supported offer to set up to 10, also check for duplicate letters

----------------------------------------------------------------------------------------
Information in this file is taken from https://cryptomuseum.com/crypto/enigma/wiring.htm
----------------------------------------------------------------------------------------
"""

Machines = {

# -------------------------------------------------------------------------------------------------
# Enigma I: German Army and Air Force (Wehrmacht, Luftwaffe) 

# The Enigma I was the main Enigma machine used by the German Army. The Army and Navy machines were
# the only ones with a plug board. Below is the wiring for each wheel, the ETW and all three known 
# UKWs. UKW-A was used before WWII [1]. UKW-B was the standard reflector during the war and UKW-C
# was only used in the later part of the war. The wiring of the five wheels is identical to the
# wiring of the first 5 wheels of the Enigma M3 (Navy) and the U-Boot Enigma M4.

"I":{
'shortname':'I',
'Name': "Enigma I",
'basetype':'I',
'Plugboard':True,
'ETW':	"ABCDEFGHIJKLMNOPQRSTUVWXYZ",
'I':  {'wheel':	"EKMFLGDQVZNTOWYHXUSPAIBRCJ", 'notch':	'Y', 'turnover':	'Q'},
'II': {'wheel':	"AJDKSIRUXBLHWTMCQGZNPYFVOE", 'notch':	'M', 'turnover':	'E'},
'III':{'wheel':	"BDFHJLCPRTXVZNYEIWGAKMUSQO", 'notch':	'D', 'turnover':	'V'},
'IV': {'wheel':	"ESOVPZJAYQUIRHXLNFTGKDCMWB", 'notch':	'R', 'turnover':	'J'},
'V':  {'wheel':	"VZBRGITYUPSDNHLXAWMJQOFECK", 'notch':	'H', 'turnover':	'Z'},
'UKW-A':	"EJMZALYXVBWFCRQUONTSPIKHGD",
'UKW-B':	"YRUHQSLDPXNGOKMIEBFZCWVJAT",
'UKW-C':	"FVPJIAOYEDRZXWGCTKUQSBNMHL",
'Rotors':['I','II','III','IV','V'],
'Reflectors':['UKW-A','UKW-B','UKW-C']
},




# -------------------------------------------------------------------------------------------------
# Enigma M3: German Navy (Kriegsmarine) 

# The Enigma M1, M2 and M3 machines were used by the German Navy (Kriegsmarine). They are basically
# compatible with the Enigma I. The wiring of the Enigma M3 is given in the table below. Wheels I
# thru V are identical to those of the Enigma I. The same is true for UKW B and C. The three
# additional wheels (VI, VII and VIII) were used exclusively by the Kriegsmarine. The machine is
# also compatible with the Enigma M4 (when the 4th wheel of the M4 is set to position 'A').

# Variation of the Enigma I

"M3":{
'shortname':'M3',
'Name':"Enigma M3",
'basetype':'I',
'Plugboard':True,
'ETW':	"ABCDEFGHIJKLMNOPQRSTUVWXYZ",
'I':	{'wheel':"EKMFLGDQVZNTOWYHXUSPAIBRCJ",	'notch':'Y',	'turnover':'Q'},
'II':	{'wheel':"AJDKSIRUXBLHWTMCQGZNPYFVOE",	'notch':'M',	'turnover':'E'},
'III':	{'wheel':"BDFHJLCPRTXVZNYEIWGAKMUSQO",	'notch':'D',	'turnover':'V'},
'IV':	{'wheel':"ESOVPZJAYQUIRHXLNFTGKDCMWB",	'notch':'R',	'turnover':'J'},
'V':	{'wheel':"VZBRGITYUPSDNHLXAWMJQOFECK",	'notch':'H',	'turnover':'Z'},
'VI':	{'wheel':"JPGVOUMFYQBENHZRDKASXLICTW",	'notch':'HU',	'turnover':'ZM'},
'VII':	{'wheel':"NZJHGRCXMYSWBOUFAIVLPEKQDT",	'notch':'HU',	'turnover':'ZM'},
'VIII':	{'wheel':"FKQHTLXOCBJSPDZRAMEWNIUYGV",	'notch':'HU',	'turnover':'ZM'},
'UKW-B':	"YRUHQSLDPXNGOKMIEBFZCWVJAT",
'UKW-C':	"FVPJIAOYEDRZXWGCTKUQSBNMHL",
'Rotors':['I','II','III','IV','V','VI','VII','VIII'],
'Reflectors':['UKW-B','UKW-C']
},




# -------------------------------------------------------------------------------------------------
# Enigma M4: U-Boot Enigma 

# The Enigma M4 was a further development of the M3 and was used exclusively by the U-boat division 
# of the German Navy (Kriegsmarine). It was introduced unexpectedly on 2 February 1942. Below is 
# the wiring for each wheel, the ETW and all known UKWs. UKW-B was the standard reflector 
# throughout the war and UKW-C was only temporarily used during the war. The wiring of the first 5 
# wheels (I-V)is identical to the wiring of the 5 wheels of the Enigma I used by the Wehrmacht and 
# Luftwaffe. This allowed secure communication between the departments.

# The three extra wheels (VI, VII and VIII) have two notches each, which causes a more frequent 
# wheel turnover, but also introduces another weakness (more about the Wheel turnover). 

"M4":{
'shortname':'M4',
'Name':"Enigma M4",
'basetype':'M4',
'Plugboard':True,
'ETW':	"ABCDEFGHIJKLMNOPQRSTUVWXYZ",
'I':	{'wheel':"EKMFLGDQVZNTOWYHXUSPAIBRCJ",	'notch':'Y',	'turnover':'Q'},
'II':	{'wheel':"AJDKSIRUXBLHWTMCQGZNPYFVOE",	'notch':'M',	'turnover':'E'},
'III':	{'wheel':"BDFHJLCPRTXVZNYEIWGAKMUSQO",	'notch':'D',	'turnover':'V'},
'IV':	{'wheel':"ESOVPZJAYQUIRHXLNFTGKDCMWB",	'notch':'R',	'turnover':'J'},
'V':	{'wheel':"VZBRGITYUPSDNHLXAWMJQOFECK",	'notch':'H',	'turnover':'Z'},
'VI':	{'wheel':"JPGVOUMFYQBENHZRDKASXLICTW",	'notch':'HU',	'turnover':'ZM'},
'VII':	{'wheel':"NZJHGRCXMYSWBOUFAIVLPEKQDT",	'notch':'HU',	'turnover':'ZM'},
'VIII':	{'wheel':"FKQHTLXOCBJSPDZRAMEWNIUYGV",	'notch':'HU',	'turnover':'ZM'},
'Beta': {'wheel':"LEYJVCNIXWPBQMDRTAKZGFUHOS",	'turnover':''},
'Gamma':{'wheel':"FSOKANUERHMBTIYCWLQPZXVGJD",	'turnover':''},
'UKW-B':	"ENKQAUYWJICOPBLMDXZVFTHRGS",
'UKW-C':	"RDOBJNTKVEHMLFCWZAXGYIPSUQ",
'Rotors':['I','II','III','IV','V','VI','VII','VIII','Beta','Gamma'],
'Reflectors':['Beta','Gamma','UKW-B','UKW-C']
},




# -------------------------------------------------------------------------------------------------
# Railway Enigma: Modified Enigma K 

# During WWII, the Germans used a special Enigma machine for the German Railway (Reichsbahn). It
# was basically a standard commercial Enigma K with rewired wheels and a rewired reflector (UKW).
# Furthermore, the position of the notches of wheels I and III were swapped [7]. 

# Variation of the Enigma K
# The K has a combined rotor/reflector. It can have a ring setting and an initial position but 
# input and output are on the same side so it acts like a reflector.

# Reflector is settable but not rotatable, as it has no notches

"R":{
'shortname':'R',
'Name':	"Railway: Modified Enigma K",
'basetype':'K',
'Plugboard':False,
'ETW':	"QWERTZUIOASDFGHJKPYXCVBNML",
'I':	{'wheel':"JGDQOXUSCAMIFRVTPNEWKBLZYH",	'notch':'V',	'turnover':'N'},
'II':	{'wheel':"NTZPSFBOKMWRCJDIVLAEYUXHGQ",	'notch':'M',	'turnover':'E'},
'III':	{'wheel':"JVIUBHTCDYAKEQZPOSGXNRMWFL",	'notch':'G',	'turnover':'Y'},
'UKW':	"QYHOGNECVPUZTFDJAXWMKISRBL", # settable reflector
'Rotors':['I','II','III'],
'Reflectors':['UKW']
},




# -------------------------------------------------------------------------------------------------
# Enigma T: Japanese Enigma (Tirpitz) 

# The Enigma T (Tirpitz) was a special version of the Enigma K that was made for the Japanese Army
# during WWII. The wheels were wired differently and each had five turnover notches [7]. The table
# below shows the wiring of the wheels, the entry disc (ETW) and the reflector (UKW).

# Variation of the Enigma K
# The K has a combined rotor/reflector. It can have a ring setting and an initial position but 
# input and output are on the same side so it acts like a reflector.

# Reflector is settable but not rotatable, as it has no notches

"T":{
'shortname':'T',
'Name':	"Enigma T: Japanese Enigma (Turpitz)",
'basetype':'K',
'Plugboard':False,
'ETW':	"KZROUQHYAIGBLWVSTDXFPNMCJE",
'I':	{'wheel':"KPTYUELOCVGRFQDANJMBSWHZXI",	'notch':'EHMSY',	'turnover':'WZEKQ'},
'II':	{'wheel':"UPHZLWEQMTDJXCAKSOIGVBYFNR",	'notch':'EHNTZ',	'turnover':'WZFLR'},
'III':	{'wheel':"QUDLYRFEKONVZAXWHMGPJBSICT",	'notch':'EHMSY',	'turnover':'WZEKQ'},
'IV':	{'wheel':"CIWTBKXNRESPFLYDAGVHQUOJZM",	'notch':'EHNTZ',	'turnover':'WZFLR'},
'V':	{'wheel':"UAXGISNJBVERDYLFZWTPCKOHMQ",	'notch':'GKNSZ',	'turnover':'YCFKR'},
'VI':	{'wheel':"XFUZGALVHCNYSEWQTDMRBKPIOJ",	'notch':'FMQUY',	'turnover':'XEIMQ'},
'VII':	{'wheel':"BJVFTXPLNAYOZIKWGDQERUCHSM",	'notch':'GKNSZ',	'turnover':'YCFKR'},
'VIII':	{'wheel':"YMTPNZHWKODAJXELUQVGCBISFR",	'notch':'FMQUY',	'turnover':'XEIMQ'},
'UKW':	"GEKPBTAUMOCNILJDXZYFHWVQSR",
'Rotors':['I','II','III','IV','V','VI','VII','VIII'],
'Reflectors':['UKW']
},




# -------------------------------------------------------------------------------------------------
# Norway Enigma: Postwar usage 
#
# In 1945, immediately after WWII, some captured Enigma-I machines were used by the the former 
# Norwegian Police Security Service: Overvaakingspolitiet. They modified the wheel wiring and the 
# wiring of the Umkehrwalze (UKW, reflector). The wiring of the Eintrittzwalze (ETW, entry wheel) 
# and the position of the turnover notches on the wheels were left unaltered. A machine that is 
# modified in this way, is commonly known as a Norway Enigma or Norenigma as suggested by Frode 
# Weierud in 2001 in order to discriminate between the standard and the modified wiring [2].

# Variation of the Enigma I

"N":{
'shortname':'N',
'Name':"Norway Enigma",
'basetype':'I',
'Plugboard':False, # Not sure about this value
'ETW':	"ABCDEFGHIJKLMNOPQRSTUVWXYZ",
'I':	{'wheel':"WTOKASUYVRBXJHQCPZEFMDINLG",	'notch':'Y',	'turnover':'Q'},
'II':	{'wheel':"GJLPUBSWEMCTQVHXAOFZDRKYNI",	'notch':'M',	'turnover':'E'},
'III':	{'wheel':"JWFMHNBPUSDYTIXVZGRQLAOEKC",	'notch':'D',	'turnover':'V'},
'IV':	{'wheel':"ESOVPZJAYQUIRHXLNFTGKDCMWB",	'notch':'R',	'turnover':'J'},
'V':	{'wheel':"HEJXQOTZBVFDASCILWPGYNMURK",	'notch':'H',	'turnover':'Z'},
'UKW':	"MOWJYPUXNDSRAIBFVLKZGQCHET",
'Rotors':['I','II','III','IV','V'],
'Reflectors':['UKW']
},




# -------------------------------------------------------------------------------------------------
# Sonder Enigma: Sondermaschine (special machine) 

# In the late 1980s, a strange Enigma machine was dicovered in the house of a former intelligence
# officer, who used to work for a special unit. Basically, this machine was a standard Enigma-I,
# of which the wiring of the wheels and the UKW had been changed. For this reason, the machine and
# the wheels were marked with the letter 'S', which probably means Sondermaschine (special
# machine). The wooden case is marked A1807S, whilst the machine is labelled 17401S/jla/43. The
# UKW is marked A19872S. The machine was re-discovered in 2017 by Gunter Hutter [9].

# Variation of the Enigma I

"S":{
'shortname':'S',
'Name':"Sonder Enigma: Sondermaschine",
'basetype':'I',
'Plugboard':False, # Not sure about this value
'ETW':	"ABCDEFGHIJKLMNOPQRSTUVWXYZ",
'I':	{'wheel':"VEOSIRZUJDQCKGWYPNXAFLTHMB",	'notch':'Y',	'turnover':'Q'},
'II':	{'wheel':"UEMOATQLSHPKCYFWJZBGVXINDR",	'notch':'M',	'turnover':'E'},
'III':	{'wheel':"TZHXMBSIPNURJFDKEQVCWGLAOY",	'notch':'D',	'turnover':'V'},
'UKW':	"CIAGSNDRBYTPZFULVHEKOQXWJM",
'Rotors':['I','II','III'],
'Reflectors':['UKW']
},
# At the end of WWII, the Enigma with serial number A17245 S was confiscated by a TICOM team and
# transferred to the NSA. It has the same wiring of the UKW as the A17401 S mentioned above. As the
# wheel wiring of the former is known, we were able to complete the table above [10][11]. 




# -------------------------------------------------------------------------------------------------
# Enigma G: Zählwerk Enigma A28 and G31 

# The Zählwerk Enigma was the first machine with a cog-wheel driven stepping mechanism. It is the
# predecessor of the Enigma G. As the Zählwerk Enigma was built as a commercial machine, the
# initial wiring was identical to the wiring of the Enigma D. The machine (and also the later G31)
# was also sold to the military (e.g. to the German secret service, the Abwehr) and to some foreign
# customers. Some of the latter changed the wiring of the cipher wheels, but in most cases the
# wiring of the UKW was left unaltered. Examples of individual Enigma G wiring are given below.

"A865":{
'shortname':'A865',
'Name':"Enigma G: Zählwerk Enigma A28 and G31",
'basetype':'G',
'Plugboard':False, # Not sure about this value
'ETW':	"QWERTZUIOASDFGHJKPYXCVBNML",
'I':	{'wheel':"LPGSZMHAEOQKVXRFYBUTNICJDW",	'notch':'ACDEHIJKMNOQSTWXY',	'turnover':'SUVWZABCEFGIKLOPQ'},
'II':	{'wheel':"SLVGBTFXJQOHEWIRZYAMKPCNDU",	'notch':'ABDGHIKLNOPSUVY',		'turnover':'STVYZACDFGHKMNQ'},
'III':	{'wheel':"CJGDPSHKTURAWZXFMYNQOBVLIE",	'notch':'CEFIMNPSUVZ',			'turnover':'UWXAEFHKMNR'},
'uG':	{'wheel':"IMETCGFRAYSQBZXWLHKDVUPOJN",	'notch':'',                 	'turnover':''},
'Rotors':['I','II','III'],
'Reflectors':['uG']
},




# -------------------------------------------------------------------------------------------------
# Wiring of the G-312: G31 Abwehr Enigma 

# The table below shows the wiring of the G-312. Although the machine is believed to have been
# used by the German Abwehr, it is the only one ever found with this wiring [3]. Different wirings
# were used for different sections of the Abwehr, and also for different radio nets. It is also
# possible that some machines were rewired a number of times during their lifetime.

"G312":{
'shortname':'G312',
'Name':"G-312: G31 Abwehr Enigma",
'basetype':'G',
'Plugboard':False, # Not sure about this value
'ETW':	"QWERTZUIOASDFGHJKPYXCVBNML",
'I':	{'wheel':"DMTWSILRUYQNKFEJCAZBPGXOHV",	'notch':'ACDEHIJKMNOQSTWXY',	'turnover':'ABCEFGIKLOPQSUVWZ'},
'II':	{'wheel':"HQZGPJTMOBLNCIFDYAWVEUSRKX",	'notch':'ABDGHIKLNOPSUVY',		'turnover':'ACDFGHKMNQSTVYZ'},
'III':	{'wheel':"UQNTLSZFMREHDPXKIBVYGJCWOA",	'notch':'CEFIMNPSUVZ',			'turnover':'AEFHKMNRUWX'},
'uG':	{'wheel':"RULQMZJSYGOCETKWDAHNBXPVIF",	'notch':'',                 	'turnover':''},
'Rotors':['I','II','III'],
'Reflectors':['uG']
},

#"AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAA"
#"GJUIY CMDGU VTTFF QPZMX KVCTZ USOBZ LDZUM HQMJX WTZWM QNNUW IDYEQ PGVFZ ETOLB ZKTPL JPKRK FJGRT BNFBH BFYVK MVPVN HXUFJ OXSXE QTUPX LWKCO RIODF YXIVO ZUZCD SFEKB TXVGU EOGNV KZYTW SOYWK YPS"




# -------------------------------------------------------------------------------------------------
# Wiring of the G-260: G31 Abwehr Enigma 

# In March 1945, just before the end of WWII, the Argentine police arrested the German spy Johann
# Siegfried Becker. In his posession was an Enigma model G31 with serial number G-260. Two months
# later, they handed the machine over to the Americans [4]. As Becker was believed to work for the
# German Secret Service, the Abwehr, it is most likely that the G-260 was wired for Abwehr
# communication. The machine is now on public display at the NCM in Fort Meade (Maryland, US).

"G260":{
'shortname':'G260',
'Name':"G-260: G31 Abwehr Enigma",
'basetype':'G',
'Plugboard':False, # Not sure about this value
'ETW':	"QWERTZUIOASDFGHJKPYXCVBNML",
'I':	{'wheel':"RCSPBLKQAUMHWYTIFZVGOJNEXD",	'notch':'ACDEHIJKMNOQSTWXY',	'turnover':'SUVWZABCEFGIKLOPQ'},
'II':	{'wheel':"WCMIBVPJXAROSGNDLZKEYHUFQT",	'notch':'ABDGHIKLNOPSUVY',		'turnover':'STVYZACDFGHKMNQ'},
'III':	{'wheel':"FVDHZELSQMAXOKYIWPGCBUJTNR",	'notch':'CEFIMNPSUVZ',			'turnover':'UWXAEFHKMNR'},
'uG':	{'wheel':"IMETCGFRAYSQBZXWLHKDVUPOJN",	'notch':'',                 	'turnover':''},
'Rotors':['I','II','III'],
'Reflectors':['uG']
},




# -------------------------------------------------------------------------------------------------
# Wiring of the G-111: G31 Hungarian Enigma 

# The G-111 was a special version of the Enigma G (G31 model Ch.15b) [5] that was built for the
# Hungarian Army. It was supplied with five cipher discs. The table below shows the wiring of the
# wheels of the G-111, the entry disc (Eintrittswalze, ETW) and the reflector (Umkehrwalze, UKW).
# Note that only wheels I, II and V were found with this machine.

"G111":{
'shortname':'G111',
'Name':"G-111: Hungry/Munich",
'basetype':'G',
'Plugboard':False,
'ETW':	"QWERTZUIOASDFGHJKPYXCVBNML", #  *1
'I':	{'wheel':"WLRHBQUNDKJCZSEXOTMAGYFPVI",	'notch':'ACDEHIJKMNOQSTWXY',	'turnover':'SUVWZABCEFGIKLOPQ'}, # 17
'II':	{'wheel':"TFJQAZWMHLCUIXRDYGOEVBNSKP",	'notch':'ABDGHIKLNOPSUVY',	'turnover':'STVYZACDFGHKMNQ'}, # 15
#III	?	?	?	11
#IV	?	?	?	?
'V':	{'wheel':"QTPIXWVDFRMUSLJOHCANEZKYBG",	'notch':'AEHNPUY',	'turnover':'SWZFHMQ'}, # 7
'UKW':	{'wheel':"IMETCGFRAYSQBZXWLHKDVUPOJN",	'notch':'',       	'turnover':''}, #  *2
'Rotors':['I','II','V'],
'Reflectors':['UKW']
},
# As we can learn from the above table, the number of notches as well as the turnover positions of
# wheels I and II are identical to those on the same wheels of other Zählwerk machines (17 and 15
# notches respectively). This suggests that the notches of the G-machines were never changed.

# This machine contains the standard wiring of the ETW for a commercial machine.
# The UKW is also wired in the standard fashion for a commercial machine.
# ---
#  1. This machine contains the standard wiring of the ETW for a commercial machine.
#  2. The UKW is also wired as in a commercial machine.




# -------------------------------------------------------------------------------------------------
# Enigma D: Commercial Enigma A26 

# The Enigma D can be considered as the main commercial machine [6]. It was introduced in 1926
# and was the basis for most of the later machines, including the Enigma K, the Enigma I and the
# Zählwerk Enigma. The wiring was identical for all commercial machines, including the later
# Enigma K (A27). Although the wiring of the wheels was changed by some customers, they often
# left the wiring of the UKW intact. As far as we know, the wiring of the ETW was never changed.

# Predecessor of the Enigma K
# The K/D has a combined rotor/reflector. It can have a ring setting and an initial position but 
# input and output are on the same side so it acts like a reflector.

# Reflector is settable but not rotatable, as it has no notches

"D":{
'shortname':'D',
'Name':"Enigma D: Commercial Enigma A26",
'basetype':'K',
'Plugboard':False, # Not sure about this value
'ETW':	"QWERTZUIOASDFGHJKPYXCVBNML", 
'I':	{'wheel':"LPGSZMHAEOQKVXRFYBUTNICJDW",	'notch':'G',	'turnover':'Y'},
'II':	{'wheel':"SLVGBTFXJQOHEWIRZYAMKPCNDU",	'notch':'M',	'turnover':'E'},
'III':	{'wheel':"CJGDPSHKTURAWZXFMYNQOBVLIE",	'notch':'V',	'turnover':'N'},
'UKW':	"IMETCGFRAYSQBZXWLHKDVUPOJN",
'Rotors':['I','II','III'],
'Reflectors':['UKW']
},




# -------------------------------------------------------------------------------------------------
# Enigma K: Commercial Enigma A27 

# The wiring of the wheels of the standard Enigma K was identical to the wiring of the Enigma D.
# This suggests that the machine was initially intended for commercial customers. The standard
# commercial wiring is given in the table below [7].

# The K has a combined rotor/reflector. It can have a ring setting and an initial position but 
# input and output are on the same side so it acts like a reflector.

# Reflector is settable but not rotatable, as it has no notches

"K":{
'shortname':'K',
'Name':"Enigma K: Commercial Enigma A27",
'basetype':'K',
'Plugboard':False, # Not sure about this value
'ETW':	"QWERTZUIOASDFGHJKPYXCVBNML",
'I':	{'wheel':"LPGSZMHAEOQKVXRFYBUTNICJDW",	'notch':'G',	'turnover':'Y'},
'II':	{'wheel':"SLVGBTFXJQOHEWIRZYAMKPCNDU",	'notch':'M',	'turnover':'E'},
'III':	{'wheel':"CJGDPSHKTURAWZXFMYNQOBVLIE",	'notch':'V',	'turnover':'N'},
'UKW':	"IMETCGFRAYSQBZXWLHKDVUPOJN",
'Rotors':['I','II','III'],
'Reflectors':['UKW']
},




# -------------------------------------------------------------------------------------------------
# Swiss-K: Swiss Enigma K variant 

# This was the Swiss variant of the Enigma K. All Enigma K machines were delivered by the Germans
# with the standard commercial wheel wiring, also known from the Enigma D (see the table below).
# Immediately after reception, however, the Swiss changed the wiring of all cipher wheels [7]. 

# Although the Swiss altered the wiring of the cipher wheels (I, II and III), the wiring of the UKW
# (reflector) was left unchanged. This is true for all three users of the Enigma K: the Swiss Army,
# the Air Force and the Foreign Ministry (diplomatic service). In the table below, the only known 
# wiring of the wheels of the Swiss Air Force are given. The wiring of the other services are
# unknown to us.

# Variation of the Enigma K
# The K has a combined rotor/reflector. It can have a ring setting and an initial position but 
# input and output are on the same side so it acts like a reflector.

# Reflector is settable but not rotatable, as it has no notches

# Swiss Air Force

"KS":{
'shortname':'KS',
'Name':"Swiss-KL Swiss Air Force",
'basetype':'K',
'Plugboard':False, # Not sure about this value
'ETW':	"QWERTZUIOASDFGHJKPYXCVBNML",
'I':	{'wheel':"PEZUOHXSCVFMTBGLRINQJWAYDK",	'notch':'G',	'turnover':'Y'},
'II':	{'wheel':"ZOUESYDKFWPCIQXHMVBLGNJRAT",	'notch':'M',	'turnover':'E'},
'III':	{'wheel':"EHRVXGAOBQUSIMZFLYNWKTPDJC",	'notch':'V',	'turnover':'N'},
'UKW':	"IMETCGFRAYSQBZXWLHKDVUPOJN",
'Rotors':['I','II','III'],
'Reflectors':['UKW']
},




# -------------------------------------------------------------------------------------------------
# Enigma KD: Enigma K with UKW-D 

# The Enigma KD was a standard commercial Enigma K machine with a rewirable reflector (UKW-D).
# Below is the wiring if the first three wheels (I, II and III) of the Enigma KD that was found in
# the archives of the FRA in Sweden [8]. This wiring might be identical to the first three wheels
# of the Enigma KD used by Mil Amt during WWII, but this is currently uncertain.

# Variation of the Enigma K
# The K has a combined rotor/reflector. It can have a ring setting and an initial position but 
# input and output are on the same side so it acts like a reflector.

# Reflector is settable but not rotatable, as it has no notches

"KD":{
'shortname':'KD',
'Name':"Enigma KD: Enigma K with UKW-D",
'basetype':'K',
'Plugboard':False, # Not sure about this value
'ETW':	"QWERTZUIOASDFGHJKPYXCVBNML",
'I':	{'wheel':"VEZIOJCXKYDUNTWAPLQGBHSFMR",	'notch':'ACGIMPTVY',	'turnover':'SUYAEHLNQ'},
'II':	{'wheel':"HGRBSJZETDLVPMQYCXAOKINFUW",	'notch':'ACGIMPTVY',	'turnover':'SUYAEHLNQ'},
'III':	{'wheel':"NWLHXGRBYOJSAZDVTPKFQMEUIC",	'notch':'ACGIMPTVY',	'turnover':'SUYAEHLNQ'},
'UKW':	"NSUOMKLIHZFGEADVXWBYCPRQTJ",	#	*1
'Rotors':['I','II','III'],
'Reflectors':['UKW']
},

# ---
# 1. Note that due to the nature of the (rewirable) UKW it does not have a fixed wiring. The table
#    above shows the wiring of the UKW when the machine was discovered at the FRU. The actual wiring
#    will have been changed frequently when the machine was used in an operational context.
#
# 2. Mil Amt changed the order of the wheels and the Ringstellung daily, whilst the Grundstellung (and
#    probably also the wiring of UKW-D) was changed every three weeks [7].

}

description = { # basetype : description
    'K': "3 rotors with 1 to 9 notches, no plugboard, settable reflectors but not rotating",
    'I': "3 rotors with 1 or 2 notches, fixed position reflectors and optional plugboard",
    'G': "3 rotors with many notches, no plugboard, settable and rotatable reflector",
    'M4':"4 rotors with 1 or 2 notches, fixed position reflectors and a plugboard"
    }


if __name__ == '__main__': # pragma: no cover
    
    print(list(Machines.keys()))
    
    for machine in list(Machines.keys()):
        #print "\n",machine,":",Machines[machine]
        print("Name: %s \tBase Type: %s\t%s" % (machine, Machines[machine]['basetype'], description[Machines[machine]['basetype']]))
        #print Machines[machine]
        #print Machines[machine]['Reflectors']
        #print Machines[machine][Machines[machine]['Reflectors'][0]]


