import wx,urlparse,socket

from wx.lib.wordwrap import wordwrap
class HttpAnswer:
        def SendHttpRequest(self,hostname,path):
                #Debug
                #print 'GET '+path+' HTTP/1.0\n'
                #print 'Host: '+hostname
                self.s.send('GET '+path+' HTTP/1.0\n')
                self.s.send('Host: '+hostname+'\n')
                self.s.send('User-Agent: Mozilla/5.0 (Windows; U; Windows NT 5.1; fr; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5\n')
                self.s.send('Accept: */*\n')
                self.s.send('Accept: image/gif\n')
                self.s.send('Accept: image/x-xbitmap\n')
                self.s.send('Accept: image/jpeg\n')
                self.s.send('\n')

        def ParseHttpReader(self):
                self.data = self.s.recv(1500)
                self.s.close()

        def __init__(self, hostname, port, path):
                self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.s.connect((hostname, port))
                self.SendHttpRequest(hostname,path)
                self.ParseHttpReader()
                
        def PrintHeader(self):
                return self.data
                
class Frame(wx.Frame):
        def __init__(self, image, parent=None, id=-1,pos=wx.DefaultPosition,title='HttpDebug'):
                #self.panel = wx.Panel(self, wx.ID_ANY)
                wx.Frame.__init__(self, parent, id, title, pos)
                # change the button's parent to refer to my panel
                self.lblname = wx.StaticText(self, -1, "URL:",wx.Point(5,10))
                self.httpurl = wx.TextCtrl(self, 20, "http://www.google.fr/", wx.Point(30, 10), wx.Size(140,-1))
                self.Go = wx.Button(self, -1, "Go", (300,10))
                self.answer = wx.TextCtrl(self, 1, "",wx.Point(30, 50), wx.Size(300,150),wx.TE_MULTILINE | wx.TE_READONLY)
                
                self.statusbar = self.CreateStatusBar()
                
                #Sizer
                #box = wx.BoxSizer(wx.VERTICAL)
                #box.Add(self.answer, 0, wx.EXPAND)
                #self.SetSizer(box)

                #Bind event
                self.Bind(wx.EVT_BUTTON, self.OnButton, self.Go)

                #and show
                self.Show()

        def OnButton(self, evt): 
                st = self.httpurl.GetValue()
                urlparsed = urlparse.urlparse(st)
                hostname = urlparsed.hostname
                if urlparsed.port is None:
                        port=80
                else:
                        port = int(urlparsed.port)

                ans = HttpAnswer(hostname,port,urlparsed.path)
                self.answer.SetValue(ans.PrintHeader())

class App(wx.App):
        def __init__(self, redirect=True, filename=None):
                wx.App.__init__(self, redirect, filename)
                
        def OnInit(self):
                self.frame = Frame(wx.ID_ANY)
                self.frame.Show()
                self.SetTopWindow(self.frame)
                return True
        
if __name__ == '__main__':
        app = App()
        app.MainLoop()

