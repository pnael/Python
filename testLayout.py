#!/usr/bin/python

# layout3.py

import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, (-1, -1), wx.Size(450, 300))

        panel = wx.Panel(self, -1)
        box = wx.BoxSizer(wx.HORIZONTAL)
        box.Add(wx.Button(panel, -1, 'Button1'), 1, wx.ALL, 5)
        box.Add(wx.Button(panel, -1, 'Button2'), 0, wx.EXPAND)
        box.Add(wx.Button(panel, -1, 'Button3'), 0, wx.ALIGN_CENTER)
        panel.SetSizer(box)
        self.Centre()

class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, -1, 'layout3.py')
        frame.Show(True)
        return True

app = MyApp(0)
app.MainLoop()