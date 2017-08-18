import wx


class Example(wx.Frame):
           
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, 
            size=(500, 450))
        self.myList = [['AC','CE','%','/'],['7','8','9','*'],['4','5','6','-']
                  ,['1','2','3','+'],['.','0','ANS','=']]
        self.InitUI()
        self.Centre()
        self.Show()     
        
    def InitUI(self):   
        
        vbox = wx.BoxSizer(wx.VERTICAL)
        self.display = wx.TextCtrl(self, style=wx.TE_RIGHT)
        vbox.Add(self.display, flag=wx.EXPAND|wx.TOP|wx.BOTTOM, border=4)
        gs = wx.GridSizer(5, 4, 5, 5)
        for i in range(0,5):
            for j in range(0,4):
                id = i*4+j
                gs.Add(wx.Button(self, label=self.myList[i][j],id=id), 0, wx.EXPAND)
                self.Bind(wx.EVT_BUTTON,self.doCal,id=id)
                
        vbox.Add(gs, proportion=1, flag=wx.EXPAND)
        self.SetSizer(vbox)

    def doCal(self,e):
        btn = e.GetEventObject()
        text = btn.Label
        if text=="=":
            r=str(eval(self.display.GetValue()))
            self.display.SetValue(r)
        elif text=="AC":
            self.display.Clear()
        elif text=="CE":
            pass
        elif text=="ANS":
            pass
        else:
            self.display.AppendText(text)
        

          
        
if __name__ == '__main__':
  
    app = wx.App()
    Example(None, title='Calculator')
    app.MainLoop()