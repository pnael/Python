#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Man class - Type a network device IP to get its neighbours
'''

import wx
import re
import sys
from optparse import OptionParser
from wx.lib.wordwrap import wordwrap
from Ciscocdplib import newSwitch



class LoginPasswordDialog(wx.Dialog):
    def __init__(self, parent, title, username, password):
        style = wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER
        super(LoginPasswordDialog, self).__init__(parent, -1, title, style=style)
        textLogin = wx.StaticText(self, -1, "Tacas Login")
        inputLogin = wx.TextCtrl(self, -1,username)
        textPassword = wx.StaticText(self, -1, "Tacas password")
        inputPassword = wx.TextCtrl(self, -1, password, style=wx.TE_PASSWORD)
        textPasswordCheck = wx.StaticText(self, -1, "Tacas password check")
        inputPasswordCheck = wx.TextCtrl(self, -1, password,style=wx.TE_PASSWORD)

        buttons = self.CreateButtonSizer(wx.OK|wx.CANCEL)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(textLogin, 0, wx.ALL, 5)
        sizer.Add(inputLogin, 1, wx.EXPAND|wx.ALL, 5)
        sizer.Add(textPassword, 0, wx.ALL, 5)
        sizer.Add(inputPassword, 1, wx.EXPAND|wx.ALL, 5)
        sizer.Add(textPasswordCheck, 0, wx.ALL, 5)
        sizer.Add(inputPasswordCheck, 1, wx.EXPAND|wx.ALL, 5)
        sizer.Add(buttons, 0, wx.EXPAND|wx.ALL, 5)
        self.SetSizerAndFit(sizer)

        self.inputLogin = inputLogin
        self.inputPassword = inputPassword
        self.inputPasswordCheck = inputPasswordCheck


    def GetLogin(self):
        return self.inputLogin.GetValue()
    def GetPassword(self):
        return self.inputPassword.GetValue()
    def GetPasswordCheck(self):
        return self.inputPasswordCheck.GetValue()


debug=False

class mainFrame(wx.Frame):
    def __init__(self, parent, username='', password='', switchIP=''):
        wx.Frame.__init__(self, parent,title ='Get Lan Design',size=(900,500))

        self.panel = wx.Panel(self, wx.ID_ANY)

        # tacacs account
        self.username = username
        self.password = password

        #navigation
        self.currentIP=''
        self.prevIP=''
        #liste des switchs déjà visités
        self.switchlist=[]

        menubar = wx.MenuBar()
        # File Menu
        fileMenu = wx.Menu()
        nsitem = fileMenu.Append(wx.ID_NEW, '&New device\tCtrl+N')
        tacacsProperties = fileMenu.Append(wx.ID_PROPERTIES, 'Tacacs &settings')
        qmi = fileMenu.Append(wx.ID_EXIT, '&Quit\tCtrl+W')
        menubar.Append(fileMenu, '&File')

        #file menu Binding
        self.Bind(wx.EVT_MENU, self.getSwitchIP, nsitem)
        self.Bind(wx.EVT_MENU, self.getTacacs, tacacsProperties)
        self.Bind(wx.EVT_MENU, self.OnQuit, qmi)

        #Help Menu
        helpMenu = wx.Menu()
        abtem = helpMenu.Append(wx.ID_ANY, '&About...')
        menubar.Append(helpMenu, '&Help')
        self.SetMenuBar(menubar)
        #Help menu binding
        self.Bind(wx.EVT_MENU, self.OnButton, abtem)
        self.Show()

        #fenètre principale
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.panel.SetSizer(self.sizer)


        if switchIP:
            if self.validateIP(switchIP):
                try:
                    if self.username and self.password:
                        self.OnNewSwitch(switchIP)
                except Exception as inst:
                    print type(inst)     # the exception instance
                    print inst.args      # arguments stored in .args
                    print inst           # __str__ allows args to printed directly:
                    wx.MessageBox("Could not connect to "+switchIP, "Confirm",wx.OK | wx.ICON_ERROR)
            else:
                wx.MessageBox("Invalid address ", "Confirm",wx.OK | wx.ICON_ERROR)


    def validateIP(self,ipAddress):
        ipRegex = r"^([01]?\d\d?|2[0-4]\d|25[0-5])\.([01]?\d\d?|2[0-4]\d|25[0-5])\.([01]?\d\d?|2[0-4]\d|25[0-5])\.([01]?\d\d?|2[0-4]\d|25[0-5])$"
        re_ip = re.compile(ipRegex)
        match = re_ip.match(ipAddress)
        if match:
            return match
        else:
            return None


    def getSwitchIP(self, e):
        dlg = wx.TextEntryDialog(None, "Please type network device IP address?")
        if dlg.ShowModal() == wx.ID_OK:
            response = dlg.GetValue()
            dlg.Destroy()
        else:
            dlg.Destroy()
            return

        if response == '':
            return

        if self.validateIP(response):
            try:
                self.OnNewSwitch(response)
            except:
                wx.MessageBox("Could not connect to "+response, "Confirm",wx.OK | wx.ICON_ERROR)

    def getTacacs(self, e):

        dial = LoginPasswordDialog(None, 'Tacacs Login',self.username,self.password)
        result = dial.ShowModal()

        if result == wx.ID_CANCEL:
            return
        self.username=dial.GetLogin().encode()
        password=dial.GetPassword().encode()
        passwordCheck = dial.GetPasswordCheck().encode()

        while password != passwordCheck:
            wx.MessageBox("Password do not match", "Confirm",wx.OK | wx.ICON_ERROR)
            result = dial.ShowModal()
            if result == wx.ID_CANCEL:
                return
            self.username=dial.GetLogin().encode()
            password=dial.GetPassword().encode()
            passwordCheck = dial.GetPasswordCheck().encode()


        self.password = password

        if debug:
            print self.username
            print self.password

        dial.Destroy()

    def OnNewSwitch(self,response):
        #check if already visited
        ns=None
        for switch in self.switchlist:
            if switch.ip == response:
                #ok already found
                if debug: 
                    print "Switch found in visited list"
                ns = switch
                break

        if ns is None:
            # Connect to switch
            if debug:
                print self.username,self.password,debug

            ns = newSwitch(response,self.username,self.password,debug)
            if debug:
                print "Switch object created",ns.ip
            # get the neighnours
            ns.getNeighbours(debug)
            #save the list as already visited
            self.switchlist.append(ns)


        # got the switch
        self.currentIP=ns.ip
        self.sizer.Clear()
        #print the neighbours
        y=10
        nghbs=[]
        self.sizer.Add(wx.StaticText(self.panel,-1, ns.localName+" "+ns.ip+" :"))
        for k,v in ns.neighbourName.iteritems():
            y = y+20
            nghb = "|- "+v[3][0]+" ---- "+v[3][1]+" -| "+k+" ,"+v[0]+", "+v[2]
            nghbs.append(nghb)
        self.lb = wx.ListBox(self.panel,-1,choices=sorted(nghbs),style=wx.LB_SINGLE)
        self.sizer.Add(self.lb,wx.EXPAND)

        #Boutons
        bsizer = wx.BoxSizer(wx.HORIZONTAL)
        # back button
        mb1 = wx.Button(self.panel,-1,label='Back')
        mb1.Bind(wx.EVT_BUTTON, self.Back)
        bsizer.Add(mb1)
        # refresh button
        mb2 = wx.Button(self.panel,-1,label='Refresh')
        mb2.Bind(wx.EVT_BUTTON, self.Refresh)
        bsizer.Add(mb2)
        # get neighbours button
        mb = wx.Button(self.panel,-1,label='Get neighbours')
        mb.Bind(wx.EVT_BUTTON, self.OnGetNeighbours)
        bsizer.Add(mb)

        self.sizer.Add(bsizer)
        self.panel.Layout()

    def Refresh(self, e):
        # clique sur le bouton back
        # on détruit l'affichage des voisins existants
        if self.lb:
            self.lb.Destroy()

        if self.currentIP:
            if self.validateIP(self.currentIP):
                try:

                    # we remove the switch object from history
                    for switch in self.switchlist:
                        if switch.ip == self.currentIP:
                                #ok found
                                self.switchlist.remove(switch)
                                break

                    self.OnNewSwitch(self.currentIP)
                except Exception as inst:
                    print type(inst)     # the exception instance
                    print inst.args      # arguments stored in .args
                    print inst           # __str__ allows args to printed directly:
                    wx.MessageBox("Could not connect to "+self.currentIP, "Error",wx.OK | wx.ICON_ERROR);
        else:
            wx.MessageBox("No history", "Confirm",wx.OK | wx.ICON_ERROR);   

    def Back(self, e):
        # clique sur le bouton back
        # on détruit les voisins existants
        if self.lb:
            self.lb.Destroy()
        if self.prevIP:
            if self.validateIP(self.prevIP):
                try:
                    self.OnNewSwitch(self.prevIP)
                except Exception as inst:
                    print type(inst)     # the exception instance
                    print inst.args      # arguments stored in .args
                    print inst           # __str__ allows args to printed directly:
                    wx.MessageBox("Could not connect to "+self.prevIP, "Error",wx.OK | wx.ICON_ERROR);
        else:
            wx.MessageBox("No history", "Confirm",wx.OK | wx.ICON_ERROR);

    def OnGetNeighbours(self, e):
        result=self.lb.GetStringSelection().split(',')
        self.lb.Destroy()
        try:
            if result[1] == '':
                return
        except IndexError:
            dlg = wx.MessageDialog(self, 
            "Please select a neighbour",
            "Confirm Exit", wx.OK|wx.ICON_ERROR)
            result = dlg.ShowModal()
            dlg.Destroy()
            return

        if self.validateIP(result[1]):
            try:
                #set the history
                self.prevIP = self.currentIP
                # go to new switch
                self.OnNewSwitch(result[1])
            except Exception as inst:
                print type(inst)     # the exception instance
                print inst.args      # arguments stored in .args
                print inst           # __str__ allows args to printed directly:
                wx.MessageBox("Could not connect to "+result[1], "Confirm",wx.OK | wx.ICON_ERROR);

    def OnQuit(self, e):
        self.Close()

    def OnButton(self, evt):
        # First we create and fill the info object
        info = wx.AboutDialogInfo()
        info.Name = "Get LAN Design"
        info.Version = "5.0"
        info.Copyright = "(C) 2012 Philippe NAEL"
        info.Description = wordwrap(
           "A program that use TACACS account to connect to Cisco devices "
           "It then parses the ascii output to build a neighbours list",
           # change the wx.ClientDC to use self.panel instead of self
           350, wx.ClientDC(self.panel))
        info.WebSite = ("http://www.owenscornign.com", "OC Homepage")
        info.Developers = [ "Philippe NAEL"]

        # change the wx.ClientDC to use self.panel instead of self
        info.License = wordwrap(licenseText, 500, wx.ClientDC(self.panel))

        # Then we call wx.AboutBox giving it that info object
        wx.AboutBox(info)

overview = """<html><body>
    <h2><center>wx.AboutBox</center></h2>

    This function shows the native standard about dialog containing the
    information specified in info. If the current platform has a native
    about dialog which is capable of showing all the fields in info, the
    native dialog is used, otherwise the function falls back to the
    generic wxWidgets version of the dialog.

    </body></html>
"""

licenseText = """ All rights granted under this License are granted for the term of 
copyright on the Program, and are irrevocable provided the stated
conditions are met.  This License explicitly affirms your unlimited
permission to run the unmodified Program.  The output from running a
covered work is covered by this License only if the output, given its
content, constitutes a covered work.  This License acknowledges your
rights of fair use or other equivalent, as provided by copyright law."""



def validateOptions(options):
    global debug
    if options.debug:
        print "Enabling debug mode"
        debug=True
    else:
        debug=False

    if options.username:
        username = options.username
    else:
        username=''

    if options.password:
        password = options.password
    else:
        password=''

    if options.switchip:
        sip = options.switchip
    else:
        sip=''

    if debug:
        print username,password,sip
    return username,password,sip

if __name__ == '__main__':

# Usual verifications and warnings
    options=[]
    if sys.argv[1:]:
        parser = OptionParser()
        parser.add_option("-s", "--switchname",action="store", type="string", dest="switchip",
            help="Cisco switch IP or hostname.")
        parser.add_option("-u", "--username",action="store", type="string", dest="username", default="",
            help="Telnet username")
        parser.add_option("-p", "--password",action="store", type="string", dest="password", default="",
            help="Telnet password")
        parser.add_option("-d", "--debug",action="store_true", dest="debug",help="Set debug mode")
        (options, args) = parser.parse_args()

    app = wx.App(redirect=False)

    username=''
    password=''
    switchip=''

    if options:
        (username, password, switchip) = validateOptions(options)

    mainFrame(None, username, password, switchip)
    app.MainLoop()
