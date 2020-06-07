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

        possibilities = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        squares = []
        for i in range(81):
            squares.append(possibilities)
        i=0
        for square in self.my_controls:
            if(square.GetValue() != ""):
                squares[i] = [square.GetValue()]
            i+=1

        for square in squares:
            if len(square) == 1:
                continue
            else:
                row_indices = self.determineRow(51)
                col_indices = self.determineCol(51)
                # box_indices = self.determineBox(80)
                print(row_indices)
                print(col_indices)
                # print(box_indices)

        #solve puzzle here
        #then reveal in red the answers

    def determineCol(self, index):
        col_indices = []
        start_number = 0

        start_number = index % 9


        for i in range(9):
            col_indices.append(start_number)
            start_number += 9

        return col_indices

    def determineRow(self, index):
        row_indices = []
        mult = 0
        if index >= 0 and index <= 8:
            mult = 0
        elif index <= 17:
            mult = 1
        elif index <= 26:
            mult = 2
        elif index <= 35:
            mult = 3
        elif index <= 44:
            mult = 4
        elif index <= 53:
            mult = 5
        elif index <= 62:
            mult = 6
        elif index <= 71:
            mult = 7
        else:
            mult = 8

        for i in range(9):
            row_indices.append(mult*9 + i)

        return row_indices

    def determineBox(self, index):

        box_indices = []

        for i in range(9):
            if i <= 1 or i <= 4 or i <= 7:
                box_indices.append(start_number)
                start_number += 1
            else:
                box_indices.append(start_number)
                start_number += 7

            print(i)

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
