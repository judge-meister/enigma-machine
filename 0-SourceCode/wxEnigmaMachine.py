#!/usr/bin/env python

"""
wxEnigmaMachine

dialog inputs

!3x spinCtrl(8 options) : 3 wheels - which rotor
!3x spinCtrl (26 options) : rotor setting
!3x spinCtrl (26 options) : ring setting
1x spinCtrl(2 options) : which reflector
10x textCtrl(2 char) : 10 plugs for plugboard

textCtrl(100 chars) : input text
textCtrl(100 chars) : output text (not editable)
"""


# staticbox.py

import wx
from Enigma.AlphaUtils import ALPHA
from Enigma.Rotors import Left, Middle, Right
from Enigma.Rotors import RotorFactory
from Enigma.Reflectors import ReflectorFixed as Reflector
from Enigma.PlugBoard import createPlugBoard
from Enigma.MachineDetails import Machines
from Enigma.EnigmaMachine import EnigmaMachine


def createSpinCtrlAlpha(sparent, sid, svalue, smax, ssize=45):
    return SpinCtrlAlpha(parent=sparent, id=sid, value=svalue, size=(ssize, -1), min=0, max=smax, 
                         style=wx.SP_WRAP|wx.SP_ARROW_KEYS|wx.ALIGN_CENTRE_HORIZONTAL|wx.TAB_TRAVERSAL)
    
class SpinCtrlAlpha( wx.SpinCtrl ):
    def __init__( self, *args, **kwargs):
        super( SpinCtrlAlpha, self ).__init__( *args, **kwargs)

        self.Bind(wx.EVT_SPINCTRL, self.OnSpin )
        self.Bind(wx.EVT_CHAR_HOOK, self.onKey)
        self.letters = None

    def onKey(self, evt):
        if evt.GetKeyCode() == wx.WXK_DOWN:
            self.SetValue((self.GetValue()+1)%(self.GetMax()+1))
            self.SetValue(self.letters[self.GetValue()])
        elif evt.GetKeyCode() == wx.WXK_UP:
            self.SetValue((self.GetValue()-1)%(self.GetMax()+1))
            self.SetValue(self.letters[self.GetValue()])
        else:
            evt.Skip()
        
    def setLetters(self, letters):
        self.letters = letters
        
    def OnSpin(self, evt):
        #print self.letters[self.GetValue()]
        self.SetValue( self.letters[self.GetValue()] )

    def GetStringValue(self):
        return self.letters[self.GetValue()]
        
        
class EnigmaPanel(wx.Panel):
    def __init__(self, parent, id):
        wx.Panel.__init__(self, parent, id, wx.DefaultPosition, wx.Size(100, 100),
                                             wx.RAISED_BORDER|wx.TAB_TRAVERSAL)
        self.machine = Machines['M3']
        self._do_widgets()
        layoutBox = self._do_layout()
        self._do_bindings()
        self.SetSizerAndFit(layoutBox)
        
        self.enigma = None
        
    def _do_widgets(self):
        #self.rotor = self.rotorPos = self.ringSetting = {}
        #for p in (Left, Middle, Right):
        #    self.rotor[p]=createSpinCtrlAlpha(self, -1, RotorIds[0], smax=7)
        #    self.rotor[p].setLetters(RotorIds)
        #    self.rotorPos[p]=createSpinCtrlAlpha(self, -1, ALPHA[0], smax=25)
        #    self.rotorPos[p].setLetters(ALPHA)
        #    self.ringSetting[p]=createSpinCtrlAlpha(self, -1, ALPHA[0], smax=25)
        #    self.ringSetting[p].setLetters(ALPHA)
        
        self.rotorL=createSpinCtrlAlpha(self, wx.ID_ANY, self.machine['Rotors'][0], smax=7)
        self.rotorM=createSpinCtrlAlpha(self, wx.ID_ANY, self.machine['Rotors'][0], smax=7)
        self.rotorR=createSpinCtrlAlpha(self, wx.ID_ANY, self.machine['Rotors'][0], smax=7)
        self.rotorL.setLetters(self.machine['Rotors'])
        self.rotorM.setLetters(self.machine['Rotors'])
        self.rotorR.setLetters(self.machine['Rotors'])
        self.rotorL.SetValue(self.machine['Rotors'][0])
        self.rotorM.SetValue(self.machine['Rotors'][0])
        self.rotorR.SetValue(self.machine['Rotors'][0])
        
        self.rotorPosL=createSpinCtrlAlpha(self, wx.ID_ANY, ALPHA[0], smax=25)
        self.rotorPosM=createSpinCtrlAlpha(self, wx.ID_ANY, ALPHA[0], smax=25)
        self.rotorPosR=createSpinCtrlAlpha(self, wx.ID_ANY, ALPHA[0], smax=25)
        self.rotorPosL.setLetters(ALPHA)
        self.rotorPosM.setLetters(ALPHA)
        self.rotorPosR.setLetters(ALPHA)
        self.rotorPosL.SetValue(ALPHA[0])
        self.rotorPosM.SetValue(ALPHA[0])
        self.rotorPosR.SetValue(ALPHA[0])
        
        self.ringSettingL=createSpinCtrlAlpha(self, wx.ID_ANY, ALPHA[0], smax=25)
        self.ringSettingM=createSpinCtrlAlpha(self, wx.ID_ANY, ALPHA[0], smax=25)
        self.ringSettingR=createSpinCtrlAlpha(self, wx.ID_ANY, ALPHA[0], smax=25)
        self.ringSettingL.setLetters(ALPHA)
        self.ringSettingM.setLetters(ALPHA)
        self.ringSettingR.setLetters(ALPHA)
        self.ringSettingL.SetValue(ALPHA[0])
        self.ringSettingM.SetValue(ALPHA[0])
        self.ringSettingR.SetValue(ALPHA[0])
        
        self.reflector = createSpinCtrlAlpha(self, wx.ID_ANY, self.machine['Reflectors'][0], smax=1, ssize=90)
        self.reflector.setLetters(self.machine['Reflectors'])
        self.reflector.SetValue(self.machine['Reflectors'][0])
        
        tc_h, tc_font = self._getFont()
        lbl_h, lbl_font = self._getFont(size=11, name='Helvetica')
        
        self.blank85_lbl = wx.StaticText(self, -1, '', size=(85,-1))
        self.Rotorhdr_lbl = wx.StaticText(self, -1, 'Left', size=(45,-1))
        self.Settinghdr_lbl = wx.StaticText(self, -1, 'Middle', size=(45,-1))
        self.Positionhdr_lbl = wx.StaticText(self, -1, 'Right', size=(45,-1))
        self.LeftRotor_lbl = wx.StaticText(self, -1, 'Rotor ID', size=(85,-1))
        self.MiddleRotor_lbl = wx.StaticText(self, -1, 'Rotor Setting', size=(85,-1))
        self.RightRotor_lbl = wx.StaticText(self, -1, 'Rotor Position', size=(85,-1))
        self.PlugBoard_lbl = wx.StaticText(self, -1, 'PlugBoard', size=(85,-1))
        self.Reflector_lbl = wx.StaticText(self, -1, 'Reflector', size=(85,-1))
        self.blank85_lbl.SetFont(lbl_font)
        self.Rotorhdr_lbl.SetFont(lbl_font)
        self.Settinghdr_lbl.SetFont(lbl_font)
        self.Positionhdr_lbl.SetFont(lbl_font)
        self.LeftRotor_lbl.SetFont(lbl_font)
        self.MiddleRotor_lbl.SetFont(lbl_font)
        self.RightRotor_lbl.SetFont(lbl_font)
        self.PlugBoard_lbl.SetFont(lbl_font)
        self.Reflector_lbl.SetFont(lbl_font)
        
        self.plugBox = wx.BoxSizer(wx.HORIZONTAL)
        self.plug = []
        for i in range(10):
            self.plug.append(wx.TextCtrl(self, i, '', size=(25,tc_h+5), style=wx.TE_CENTER|wx.EXPAND|wx.TAB_TRAVERSAL))
            self.Bind(wx.EVT_TEXT, self.onPlug, self.plug[i])
            self.plug[i].SetFont(tc_font)
            self.plugBox.Add(self.plug[i], 1, wx.EXPAND, border=5)
            
        self.inputLabelp1 = wx.StaticText(self, wx.ID_ANY, "Type your message here: ")
        self.inputLabelp1.SetFont(lbl_font)
        self.inputLabelp2 = wx.StaticText(self, wx.ID_ANY, "(0 chars)        ")
        self.inputLabelp2.SetFont(lbl_font)
        self.input = wx.TextCtrl(self, -1, '', size=(400,tc_h+5), style=wx.TE_LEFT|wx.EXPAND|wx.TAB_TRAVERSAL)
        self.output = wx.TextCtrl(self, -1, '', size=(400,tc_h+5), style=wx.TE_LEFT|wx.EXPAND)
        self.output.SetEditable(False)
        self.input.SetFont(tc_font)
        self.output.SetFont(tc_font)
        self.outputLabel = wx.StaticText(self, wx.ID_ANY, "Encrypted/Decrypted Message:")
        self.outputLabel.SetFont(lbl_font)
        
    def _do_layout(self):
        
        rotorHeadersBox = wx.BoxSizer(wx.HORIZONTAL)
        rotorHeadersBox.Add(self.Rotorhdr_lbl, 1, wx.EXPAND, border=5)
        rotorHeadersBox.Add(self.Settinghdr_lbl, 1, wx.EXPAND, border=5)
        rotorHeadersBox.Add(self.Positionhdr_lbl, 1, wx.EXPAND, border=5)
        rotorHdrBox = wx.BoxSizer(wx.HORIZONTAL)
        rotorHdrBox.Add(self.blank85_lbl, 0, wx.EXPAND, border=5)
        rotorHdrBox.Add(rotorHeadersBox, 0, wx.EXPAND, border=5)
        
        rotorSettingsBoxL = wx.BoxSizer(wx.HORIZONTAL)
        rotorSettingsBoxL.Add(self.rotorL, 1, wx.EXPAND, border=5)
        rotorSettingsBoxL.Add(self.rotorM, 1, wx.EXPAND, border=5)
        rotorSettingsBoxL.Add(self.rotorR, 1, wx.EXPAND, border=5)
        #rotorSettingsBoxL.Add(self.rotorPosL, 1, wx.EXPAND, border=5)
        #rotorSettingsBoxL.Add(self.ringSettingL, 1, wx.EXPAND, border=5)
        rotorBoxL = wx.BoxSizer(wx.HORIZONTAL)
        rotorBoxL.Add(self.LeftRotor_lbl, 0, wx.EXPAND, border=5)
        rotorBoxL.Add(rotorSettingsBoxL, 0, wx.EXPAND, border=5)
        
        rotorSettingsBoxM = wx.BoxSizer(wx.HORIZONTAL)
        #rotorSettingsBoxM.Add(self.rotorM, 1, wx.EXPAND, border=5)
        #rotorSettingsBoxM.Add(self.rotorPosM, 1, wx.EXPAND, border=5)
        rotorSettingsBoxM.Add(self.ringSettingL, 1, wx.EXPAND, border=5)
        rotorSettingsBoxM.Add(self.ringSettingM, 1, wx.EXPAND, border=5)
        rotorSettingsBoxM.Add(self.ringSettingR, 1, wx.EXPAND, border=5)
        rotorBoxM = wx.BoxSizer(wx.HORIZONTAL)
        rotorBoxM.Add(self.MiddleRotor_lbl, 0, wx.EXPAND, border=5)
        rotorBoxM.Add(rotorSettingsBoxM, 0, wx.EXPAND, border=5)
        
        rotorSettingsBoxR = wx.BoxSizer(wx.HORIZONTAL)
        #rotorSettingsBoxR.Add(self.rotorR, 1 , wx.EXPAND, border=5)
        rotorSettingsBoxR.Add(self.rotorPosL, 1, wx.EXPAND, border=5)
        rotorSettingsBoxR.Add(self.rotorPosM, 1, wx.EXPAND, border=5)
        rotorSettingsBoxR.Add(self.rotorPosR, 1, wx.EXPAND, border=5)
        #rotorSettingsBoxR.Add(self.ringSettingR, 1, wx.EXPAND, border=5)
        rotorBoxR = wx.BoxSizer(wx.HORIZONTAL)
        rotorBoxR.Add(self.RightRotor_lbl, 0, wx.EXPAND, border=5)
        rotorBoxR.Add(rotorSettingsBoxR, 0, wx.EXPAND, border=5)

        reflectSettingsBox = wx.BoxSizer(wx.HORIZONTAL)
        reflectSettingsBox.Add(self.reflector, 1, wx.EXPAND, border=5)
        reflectBox = wx.BoxSizer(wx.HORIZONTAL)
        reflectBox.Add(self.Reflector_lbl, 0, wx.EXPAND, border=5)
        reflectBox.Add(reflectSettingsBox, 0, wx.EXPAND, border=5)
        
        plugBoardBox = wx.BoxSizer(wx.HORIZONTAL)
        plugBoardBox.Add(self.PlugBoard_lbl, 0, wx.EXPAND, border=5)
        plugBoardBox.Add(self.plugBox, 0, wx.EXPAND, border=5)
        
        inputBox = wx.BoxSizer(wx.HORIZONTAL)
        inputBox.Add(self.input, 1, wx.EXPAND, border=5)
        self.inputLabelBox = wx.BoxSizer(wx.HORIZONTAL)
        self.inputLabelBox.Add(self.inputLabelp1, 0, border=5)
        self.inputLabelBox.Add(self.inputLabelp2, 0, wx.LEFT, border=5)
        
        outputBox = wx.BoxSizer(wx.HORIZONTAL)
        outputBox.Add(self.output, 1, wx.EXPAND, border=5)
        outputLabelBox = wx.BoxSizer(wx.HORIZONTAL)
        outputLabelBox.Add(self.outputLabel, 0, border=5)
        
        layoutBox = wx.BoxSizer(wx.VERTICAL)
        layoutBox.Add(rotorHdrBox, 0, wx.EXPAND|wx.TOP|wx.LEFT, border=5)
        layoutBox.Add(rotorBoxL, 0, wx.EXPAND|wx.TOP|wx.LEFT, border=5)
        layoutBox.Add(rotorBoxM, 0, wx.EXPAND|wx.TOP|wx.LEFT, border=5)
        layoutBox.Add(rotorBoxR, 0, wx.EXPAND|wx.TOP|wx.LEFT, border=5)
        layoutBox.Add(reflectBox, 0, wx.EXPAND|wx.TOP|wx.LEFT, border=5)
        layoutBox.Add(plugBoardBox, 0, wx.EXPAND|wx.TOP|wx.LEFT, border=5)
        layoutBox.Add(self.inputLabelBox, 0, wx.TOP|wx.LEFT, border=5)
        layoutBox.Add(inputBox, 0, wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT, border=5)
        layoutBox.Add(outputLabelBox, 0, wx.TOP|wx.LEFT, border=5)
        layoutBox.Add(outputBox, 0, wx.EXPAND|wx.ALL, border=5)
        
        return layoutBox
        
    def _getFont(self, size=11, name='Consolas'):
        font = wx.Font(size, wx.MODERN, wx.NORMAL, wx.NORMAL, False, name)
        dc = wx.ScreenDC()
        dc.SetFont(font)
        w,h = dc.GetTextExtent("test string")
        return h, font
        

        #order = (control1, control2, control3, ...)
        #for i in xrange(len(order) - 1):
        #    order[i+1].MoveAfterInTabOrder(order[i])
            
    def _do_bindings(self):
        self.Bind(wx.EVT_TEXT, self.onKeyPress, self.input)
        
    def OnClose(self, evt):
        self.Close()

    def onPlug(self, evt):
        plugId = evt.GetId()
        plug = self.plug[plugId]
        Line = plug.GetValue().upper()
        if len(Line) > 2:
            Line = Line[:2]
        if len(Line) == 2:
            if Line[1] == Line[0]:
                Line = Line[0]
        for i in range(10):
            if i != plugId:
                otherLine = self.plug[i].GetValue()
                for l in Line:
                    if l in self.plug[i].GetValue():
                        Line = Line.replace(l, '')
        plug.ChangeValue(Line)
        plug.SetInsertionPointEnd()
        
    def onKeyPress (self, evt):
        Line = self.input.GetValue().upper()
        if self.enigma == None or len(Line) == 0:
            self.createEnigmaMachine()
        if len(Line) > 0:
            kc = Line[-1]
            if kc in ALPHA or kc == ' ':
                self.enigma.reset()
                self.output.ChangeValue(self.formatLine(self.enigma.encrypt_message(Line)))
                self.input.ChangeValue(self.formatLine(Line))
                letters = self.enigma.get_rotor_positions()
                self.rotorPosL.SetValue(letters[Left])
                self.rotorPosM.SetValue(letters[Middle])
                self.rotorPosR.SetValue(letters[Right])
            else:
                self.input.ChangeValue(self.formatLine(Line[:-1]))
            self.inputLabelp2.SetLabel("(%d chars)" % len(Line.replace(' ','')))
            self.inputLabelBox.Layout()
            self.input.SetInsertionPointEnd()
        else:
            self.output.SetValue("")
            self.input.ChangeValue("")
            self.createEnigmaMachine()
            letters = self.enigma.get_rotor_positions()
            self.rotorPosL.SetValue(letters[Left])
            self.rotorPosM.SetValue(letters[Middle])
            self.rotorPosR.SetValue(letters[Right])
        self.inputLabelp2.SetLabel("(%d chars)" % len(Line.replace(' ','')))
        self.inputLabelBox.Layout()
            
    def getPlugs(self):
        plugs = []
        for i in range(10):
            pl = str(self.plug[i].GetValue())
            if pl != '':
                plugs.append(pl)
        #print plugs
        return plugs
        
    def formatLine(self, line):
        """"""
        line = line.replace(' ','')
        lineout = ""
        for i in range(len(line)):
            lineout += line[i]
            if i%4 == 3: lineout += " "
        return lineout.strip()
        
    def createEnigmaMachine(self):
        RF = RotorFactory(self.machine)
        #print("%s %s %s" % (self.rotorL.GetStringValue(), self.rotorPosL.GetStringValue(), self.ringSettingL.GetStringValue()))
        RF.createRotor(Left,   "%s %s %s" % (self.rotorL.GetStringValue(), self.rotorPosL.GetStringValue(), self.ringSettingL.GetStringValue()))
        #print("%s %s %s" % (self.rotorM.GetStringValue(), self.rotorPosM.GetStringValue(), self.ringSettingM.GetStringValue()))
        RF.createRotor(Middle, "%s %s %s" % (self.rotorM.GetStringValue(), self.rotorPosM.GetStringValue(), self.ringSettingM.GetStringValue()))
        #print("%s %s %s" % (self.rotorR.GetStringValue(), self.rotorPosR.GetStringValue(), self.ringSettingR.GetStringValue()))
        RF.createRotor(Right,  "%s %s %s" % (self.rotorR.GetStringValue(), self.rotorPosR.GetStringValue(), self.ringSettingR.GetStringValue()))
        self.enigma = EnigmaMachine(self.machine, RF, Reflector(self.machine, self.reflector.GetStringValue()), createPlugBoard(self.getPlugs()))


class MacFrame(wx.Frame):
    """ This window displays a button """
    def __init__(self, title = "Micro App"):
        wx.Frame.__init__(self, None , -1, title)
        self._do_menu()
        self._do_layout()
        
    def _do_layout(self):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(EnigmaPanel(self, -1), 1, wx.ALIGN_CENTER)
        self.SetSizerAndFit(sizer)
        #self.SetMinSize((300, 300))
        
    def _do_menu(self):
        MenuBar = wx.MenuBar()

        FileMenu = wx.Menu()
        
        item = FileMenu.Append(wx.ID_EXIT, "&Exit")
        self.Bind(wx.EVT_MENU, self.OnQuit, item)

        item = FileMenu.Append(wx.ID_ANY, "&Open")
        self.Bind(wx.EVT_MENU, self.OnOpen, item)

        item = FileMenu.Append(wx.ID_PREFERENCES, "&Preferences")
        self.Bind(wx.EVT_MENU, self.OnPrefs, item)

        MenuBar.Append(FileMenu, "&File")
        
        HelpMenu = wx.Menu()

        item = HelpMenu.Append(wx.ID_HELP, "Test &Help",
                                "Help for this simple test")
        self.Bind(wx.EVT_MENU, self.OnHelp, item)

        ## this gets put in the App menu on OS-X
        item = HelpMenu.Append(wx.ID_ABOUT, "&About",
                                "More information About this program")
        self.Bind(wx.EVT_MENU, self.OnAbout, item)
        MenuBar.Append(HelpMenu, "&Help")

        self.SetMenuBar(MenuBar)

        #btn = wx.Button(self, label = "Quit")

        #btn.Bind(wx.EVT_BUTTON, self.OnQuit )

        self.Bind(wx.EVT_CLOSE, self.OnQuit)

        
    def OnQuit(self, evt):
        self.Destroy()
        
    def OnAbout(self, evt):
        dlg = wx.MessageDialog(self, "This is a small program to test\n"
                                     "the use of menus on Mac, etc.\n",
                                "About Me", wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()

    def OnHelp(self, evt):
        dlg = wx.MessageDialog(self, "This would be help\n"
                                     "If there was any\n",
                                "Test Help", wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()

    def OnOpen(self, evt):
        dlg = wx.MessageDialog(self, "This would be an open Dialog\n"
                                     "If there was anything to open\n",
                                "Open File", wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()

    def OnPrefs(self, evt):
        dlg = wx.MessageDialog(self, "This would be an preferences Dialog\n"
                                     "If there were any preferences to set.\n",
                                "Preferences", wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()


class MacApp(wx.App):
    def __init__(self, *args, **kwargs):
        wx.App.__init__(self, *args, **kwargs)
        
        # This catches events when the app is asked to activate by some other
        # process
        self.Bind(wx.EVT_ACTIVATE_APP, self.OnActivate)

    def OnInit(self):

        frame = MacFrame(title="Enigma Machine")
        frame.Show(True)

        #import sys
        #for f in  sys.argv[1:]:
        #    self.OpenFileMessage(f)

        return True

    def BringWindowToFront(self):
        try: # it's possible for this event to come when the frame is closed
            self.GetTopWindow().Raise()
        except:
            pass
        
    def OnActivate(self, evt):
        # if this is an activate event, rather than something else, like iconize.
        if evt.GetActive():
            self.BringWindowToFront()
        evt.Skip()
    
    def OpenFileMessage(self, filename):
        dlg = wx.MessageDialog(None,
                               "This app was just asked to open:\n%s\n"%filename,
                               "File Dropped",
                               wx.OK|wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()

    def MacOpenFile(self, filename):
        """Called for files droped on dock icon, or opened via finders context menu"""
        #print(filename)
        #print("%s dropped on app"%(filename)) #code to load filename goes here.
        #self.OpenFileMessage(filename)
        
    def MacReopenApp(self):
        """Called when the doc icon is clicked, and ???"""
        self.BringWindowToFront()

    def MacNewFile(self):
        pass
    
    def MacPrintFile(self, file_path):
        pass


app = MacApp(False)
app.MainLoop()

