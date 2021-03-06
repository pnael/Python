#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Man class - Type a network device IP to get its neighbours
'''

import wx
from wx.lib.wordwrap import wordwrap
from Ciscocdplib import newSwitch




class mainFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent,title ='Get Lan Design',size=(900,500))
       
        self.panel = wx.Panel(self, wx.ID_ANY)

       
        menubar = wx.MenuBar()
        # File Menu
        fileMenu = wx.Menu()
        nsitem = fileMenu.Append(wx.ID_NEW, '&New device\tCtrl+N')
        qmi = fileMenu.Append(wx.ID_EXIT, '&Quit\tCtrl+W')
        menubar.Append(fileMenu, '&File')
      
        #file menu Binding
        self.Bind(wx.EVT_MENU, self.OnNewSwitch, nsitem)
        self.Bind(wx.EVT_MENU, self.OnQuit, qmi)
       
        #Help Menu
        helpMenu = wx.Menu()
        abtem = helpMenu.Append(wx.ID_ANY, '&About...')
        menubar.Append(helpMenu, '&Help')
        self.SetMenuBar(menubar)
        #Help menu binding
        self.Bind(wx.EVT_MENU, self.OnButton, abtem)

        self.Show()

    def OnNewSwitch(self, e):
        dlg = wx.TextEntryDialog(None, "Please type network device IP address?")
        if dlg.ShowModal() == wx.ID_OK:
            response = dlg.GetValue()
            dlg.Destroy()
        else: 
            dlg.Destroy()
            return
              
        if response == '':
            return
        
        # Connect to switch
        ns = newSwitch(response)
        # get the neighnours
        ns.getNeighbours()
        #print the neighbours
        y=10
        i=0
        nghbs=[]
        sizer = wx.BoxSizer(wx.VERTICAL)
        #sizer.Add(wx.StaticText(self.panel,-1, ns.localName+" "+ns.ip+" :",pos=(20, y)))
        sizer.Add(wx.StaticText(self.panel,-1, ns.localName+" "+ns.ip+" :"))
        for k,v in ns.neighbourName.iteritems():
            y = y+20
            nghb = "|- "+v[3][0]+" ---- "+v[3][1]+" -| "+k+" ("+v[0]+") "+v[2]
            nghbs.append(nghb)
            i=i+1
          
        lb = wx.ListBox(self.panel,-1,choices=nghbs,style=wx.LB_SINGLE)
        sizer.Add(lb,wx.EXPAND)
        mb = wx.Button(self.panel,-1,label='Get neighbours')
        sizer.Add(mb)
        self.panel.SetSizer(sizer)

    

    def OnQuit(self, e):
        self.Close()

    def OnButton(self, evt):
        # First we create and fill the info object
        info = wx.AboutDialogInfo()
        info.Name = "Hello World"
        info.Version = "1.2.3"
        info.Copyright = "(C) 2006 Programmers and Coders Everywhere"
        info.Description = wordwrap(
           "A \"hello world\" program is a software program that prints out "
           "\"Hello world!\" on a display device. It is used in many introductory "
           "tutorials for teaching a programming language."
                     "\n\nSuch a program is typically one of the simplest programs possible "
           "in a computer language. A \"hello world\" program can be a useful "
           "sanity test to make sure that a language's compiler, development "
           "environment, and run-time environment are correctly installed.",
           # change the wx.ClientDC to use self.panel instead of self
           350, wx.ClientDC(self.panel))
        info.WebSite = ("http://en.wikipedia.org/wiki/Hello_world", "Hello World home page")
        info.Developers = [ "Joe Programmer",
                           "Jane Coder",
                           "Vippy the Mascot" ]

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

licenseText = "blah " * 250 + "\n\n" +"yadda " * 100

if __name__ == '__main__':
   app = wx.App(redirect=False)
   mainFrame(None)
   app.MainLoop()
