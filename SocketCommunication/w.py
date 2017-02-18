import wx


class SocketServerUI(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent , title = 'SocketServer',size=wx.Size(574, 456), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)


        self.ShowText = wx.TextCtrl(self , wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE | wx.TE_READONLY)
        self.InputText = wx.TextCtrl(self, id = wx.ID_ADD )
        self.TextSend = wx.Button(self, label = ' Send ')
        self.StaticText = wx.StaticText(self,label = 'enter:')
        self.StaticText.Wrap(-1)

        boxSizer1 = wx.BoxSizer(wx.HORIZONTAL)
        boxSizer2 = wx.BoxSizer(wx.HORIZONTAL)
        boxSizer3 = wx.BoxSizer(wx.VERTICAL)


        boxSizer1.Add(self.ShowText ,1,wx.ALL|wx.EXPAND |wx.ALIGN_CENTER_VERTICAL,5)
        boxSizer2.Add(self.StaticText,1,wx.ALL | wx.ALIGN_CENTER_VERTICAL,5)
        boxSizer2.Add(self.InputText,9,wx.ALL | wx.ALIGN_CENTER_VERTICAL,5)
        boxSizer2.Add(self.TextSend,2,wx.ALL | wx.ALIGN_CENTER_VERTICAL,5)
        boxSizer3.Add(boxSizer1,5,wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL,5)
        boxSizer3.Add(boxSizer2,1,wx.EXPAND,5)


        self.SetSizer(boxSizer3)
        self.Layout()
        self.Centre(wx.BOTH)
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = SocketServerUI(parent=None)
    frame.Show(True)
    app.MainLoop()
