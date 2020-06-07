import wx

class Solver(wx.Frame):
    def __init__(self, parent, title):
        super(Solver, self).__init__(parent, title=title, size=(792, 820))
        # frame = wx.Frame(None, -1,)
        # frame.SetMinSize(wx.Size(750, 750))
        # frame.SetMaxSize(wx.Size(750, 750))

        self.Bind(wx.EVT_PAINT, self.OnPaint)
        # self.OnPaint()
        self.InitUI()
        self.Centre()
        self.Show()

    def onClick(self, event):
        print("here")

    def InitUI(self):
        # menubar = wx.MenuBar()
        # fileMenu = wx.Menu()
        # menubar.Append(fileMenu, "&File")
        # self.SetMenuBar(menubar)
        # wx.StaticText(self, 1, "Use the dropdown boxes to input the numbers of the Sudoku puzzle to solve. Choose 'X' for the blank spaces.")

        vbox = wx.BoxSizer(wx.VERTICAL)
        # self.display = wx.TextCtrl(self, style=wx.TE_READONLY)
        # self.display.AppendText("Use the dropdown boxes to input the numbers of the Sudoku puzzle to solve. Choose 'X' for the blank spaces.")
        # vbox.Add(self.display, flag=wx.EXPAND | wx.TOP | wx.BOTTOM, border=4)
        gs = wx.GridSizer(9, 9, 0, 0)

        # dc = wx.PaintDC(self)
        # dc.Clear()
        # dc.SetPen(wx.Pen(wx.BLUE, 4))
        # dc.DrawLine(10, 10, 50, 50)
        self.SetFont(wx.Font(28, wx.SWISS, wx.NORMAL, wx.NORMAL, False,'MS Shell Dlg 2'))
        for i in range(81):
            #gs.Add(wx.ComboBox(self, 15, "X", choices=["X", "1", "2", "3", "4", "5", "6", "7", "8", "9"], style = wx.CB_READONLY))

            gs.Add(wx.TextCtrl(self, id==1, value="", size=(88,88), style = wx.TE_CENTRE))

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
            j += 1


        # dc.DrawLine(0, 0, 50, 50)
        # dc.DrawRectangle(5, 5, 240, 240)
        # dc.DrawRectangle(5, 250, 240, 240)
        # dc.DrawRectangle(5, 495, 240, 240)
        # dc.DrawRectangle(250, 5, 240, 240)
        # dc.DrawRectangle(250, 250, 240, 240)
        # dc.DrawRectangle(250, 495, 240, 240)
        # dc.DrawRectangle(495, 5, 240, 240)
        # dc.DrawRectangle(495, 250, 240, 240)
        # dc.DrawRectangle(495, 495, 240, 240)
        #
        # dc.SetBrush(wx.Brush('#5f3b00'))
        #
        # dc.DrawLine(5, 80, 735, 80)
        # dc.DrawLine(5, 160, 735, 160)
        # dc.DrawLine(0, 50, 750, 50)
        # dc.DrawLine(0, 130, 750, 130)
        # dc.DrawLine(0, 210, 750, 210)
        #
        # dc.DrawLine(0, 215, 750, 215)
        #
        # dc.DrawLine(0, 290, 750, 290)
        # dc.DrawLine(0, 370, 750, 370)
        # dc.DrawLine(0, 450, 750, 450)
        #
        # dc.DrawLine(0, 455, 750, 455)
        #
        # dc.DrawLine(0, 530, 750, 530)
        # dc.DrawLine(0, 610, 750, 610)
        # dc.DrawLine(0, 690, 750, 690)
        #
        # dc.DrawLine(245, 0, 245, 735)
        #
        # dc.DrawLine(75, 0, 75, 750)
        # dc.DrawLine(160, 0, 160, 750)
        # dc.DrawLine(240, 0, 240, 750)
        #
        # dc.DrawLine(495, 0, 495, 735)
        #
        # dc.DrawLine(325, 0, 325, 750)
        # dc.DrawLine(410, 0, 410, 750)
        # dc.DrawLine(490, 0, 490, 750)
        #
        # dc.DrawLine(575, 0, 575, 750)
        # dc.DrawLine(655, 0, 655, 750)
        # dc.DrawLine(735, 0, 735, 750)
        #
        # dc.DrawRectangle(-5, 690, 760, 60)
        # dc.DrawRectangle(735, -5, 30, 696)

app = wx.App()
Solver(None, title="Sudoku Solver")
app.MainLoop()
