import wx

class Solver(wx.Frame):
    def __init__(self, parent, title):
        super(Solver, self).__init__(parent, title=title, size=(792, 820))

        self.my_controls = []
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.InitUI()
        self.Centre()
        self.Show()

    def onClick(self, event):


        print(self.my_controls[0].GetValue())

        row1 = []
        row2 = []
        row3 = []
        row4 = []
        row5 = []
        row6 = []
        row7 = []
        row8 = []
        row9 = []

        for i in range(81):
            if i <= 8:
                row1.append(self.my_controls[i].GetValue())
            elif i <= 17:
                row2.append(self.my_controls[i].GetValue())
            elif i <= 26:
                row3.append(self.my_controls[i].GetValue())
            elif  i<= 35:
                row4.append(self.my_controls[i].GetValue())
            elif i <= 44:
                row5.append(self.my_controls[i].GetValue())
            elif i <= 53:
                row6.append(self.my_controls[i].GetValue())
            elif i <= 61:
                row7.append(self.my_controls[i].GetValue())
            elif i <= 70:
                row8.append(self.my_controls[i].GetValue())
            else:
                row9.append(self.my_controls[i].GetValue())
        #solve puzzle here
        #then reveal in red the answers

    def InitUI(self):
        vbox = wx.BoxSizer(wx.VERTICAL)

        gs = wx.GridSizer(9, 9, 0, 0)

        self.SetFont(wx.Font(28, wx.SWISS, wx.NORMAL, wx.NORMAL, False,'MS Shell Dlg 2'))
        for i in range(81):
            #gs.Add(wx.ComboBox(self, 15, "X", choices=["X", "1", "2", "3", "4", "5", "6", "7", "8", "9"], style = wx.CB_READONLY)
            text_control = wx.TextCtrl(self, id==1, value="", size=(88,88), style = wx.TE_CENTRE)

            self.my_controls.append(text_control)
            #gs.Add(wx.TextCtrl(self, id==1, value="", size=(88,88), style = wx.TE_CENTRE))
            gs.Add(text_control)

        self.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False,'MS Shell Dlg 2'))
        butt = wx.Button(self, wx.ID_ANY, "Click to Solve Puzzle", (320, 730))
        butt.Bind(wx.EVT_BUTTON, self.onClick)



        vbox.Add(gs, proportion=1, flag=wx.EXPAND)
        self.SetSizer(vbox)



    def OnPaint(self, event=None):
        dc = wx.PaintDC(self)
        dc.Clear()
        dc.SetPen(wx.Pen(wx.BLACK, 4))

        x=0
        for i in range(10):

            if i==3 or i==6:
                dc.SetPen(wx.Pen(wx.GREEN, width=4))
            else:
                dc.SetPen(wx.Pen(wx.BLACK, 4))

            dc.DrawLine(x, 0, x, 792)
            x += 88


        y=0
        for j in range(10):

            if j==3 or j==6:
                dc.SetPen(wx.Pen(wx.GREEN, 4))
            else:
                dc.SetPen(wx.Pen(wx.BLACK, 4))

            dc.DrawLine(0, y, 792, y)
            y += 88


app = wx.App()
Solver(None, title="Sudoku Solver")
app.MainLoop()
