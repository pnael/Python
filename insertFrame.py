import wx


class InsertFrame(wx.Frame):
	def __init__(self, parent, id):
		wx.Frame.__init__(self, parent, id, 'Frame With Button',
			size=(300, 200))
		panel = wx.Panel(self)
		panel.SetBackgroundColour('White')
		statusBar = self.CreateStatusBar()
		toolbar = self.CreateToolBar()
		toolbar.Realize()
		button = wx.Button(panel, label="Dialog",pos=(125, 10),
			size=(50, 50))
		self.Bind(wx.EVT_BUTTON, self.OnDialog, button)
		self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
		
	def OnDialog(self, event):
		dlg = wx.MessageDialog(None, 'Is this the coolest thing ever!',
			'MessageDialog', wx.YES_NO | wx.ICON_QUESTION)
		result = dlg.ShowModal()
		dlg.Destroy()

	def OnCloseWindow(self, event):
		self.Destroy()

if __name__ == '__main__':
	app = wx.PySimpleApp()
	frame = InsertFrame(parent=None, id=-1)
	frame.Show()
	app.MainLoop()