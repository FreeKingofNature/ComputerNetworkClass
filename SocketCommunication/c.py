import socket ,time,wx
import threading
from wx.lib.pubsub import Publisher
host = socket .gethostname()
num = 5
max_data = 2024
port = 1234


#################################################################################################################
class SocketServerUI(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent , title = 'Client',size=wx.Size(574, 456), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

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
        self.Centre(wx.BOTH)
##################################################################################################################
class threadsocket(threading.Thread):
    def __init__(self, s):
        super(threadsocket, self).__init__()
        self.s = s
        self.start()

    def run(self):
        data = ''
        while 1:
            try:
                data = self.s.recv(1024)
            except Exception:
                pass
            if data:
                wx.CallAfter(Publisher().sendMessage('update', data))
                time.sleep(0.01)
#####################################################################################################################
class server(SocketServerUI):
    def __init__(self,host, port):
        super(server, self).__init__(parent = None)
        Publisher().subscribe(self.update, 'update')
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.adr = (host, port)
        self.sock.connect(self.adr)
        self.sock.setblocking(5)
        self.TextSend.Bind(wx.EVT_BUTTON,self.send)
        self.th = threadsocket(self.sock)

    def update(self,mesage):
        self.ShowText.AppendText('\nreciving from %s:%s'% (self.adr , mesage.data))

    def send(self,event):
        data = self.InputText.GetValue()
        self.InputText.Clear()
        if len(data):
            try:
                self.sock.sendall(data)
                self.ShowText.AppendText('\n%s send:%s' % (host, data))
            except socket.error, e:
                print e

#######################################################################################################################
if __name__ == '__main__':
    app = wx.PySimpleApp()
    s = server(host = host, port=port)
    s.Show()
    app.MainLoop()


