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

        possibilities = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
        squares = []
        for i in range(81):
            squares.append(possibilities)
        i=0
        for sq in self.my_controls:
            if(sq.GetValue() != ""):
                print("Not a blank square")
                squares[i] = tuple(sq.GetValue())
            else:
                print("Blank square")
            i+=1

        # above is working correctly

        i=0
        for square in squares:
            if len(square) == 1:
                # go to next loop
                print("ONLY one value in current square")
                i+=1
                continue

            else:
                print("MORE than one value in current square")
                row_indices = self.determineRow(i)
                print("ROW INDICES: " + str(row_indices))
                col_indices = self.determineCol(i)
                print("COL INDICES: " + str(col_indices))

                # box_indices = self.determineBox(80)
                # print(row_indices)
                # print(col_indices)
                # print(box_indices)

                # have row indices
                # have list of lists that contain possible numbers for each square
                # square contains list of possibilities for current squares
                # go through row indices and if any are single then get rid of that value from current squares

                for index in row_indices:
                    # print("index" + str(index))
                    if len(squares[index]) == 1 and index != i:
                        # remove that value from the current square's list
                        # this is a list
                        taken_value = str(squares[index][0])
                        # print("Taken Value:" + taken_value)
                        # print("type of taken value: " + str(type(taken_value)))

                        # try:
                        #     print("Removing taken value: " + taken_value)
                        #     square.remove(taken_value)
                        #     print("Getting here")
                        # except ValueError:
                        #     print("GGGGGGetting an error")
                        #     pass
                        try:
                            print("OLD square list: " + str(square))
                            print("Removing taken value: " + taken_value)
                            square = list(square)
                            square.remove(taken_value)
                            square = tuple(square)
                            squares[i] = square
                            # squares[i] = square
                            print("NEW square list: " + str(square))
                        except ValueError:
                            print("Error")
                            pass
                    else:
                        print("No taken value to be done")
                        # for value in square:
                        #     # print("------Value:" + value)
                        #     # print("type of value: " + str(type(value)))
                        #     if value == taken_value:
                        #         print("HOORAH")
                        #     else:
                        #         print("BOOOOO")


                        # square.remove(taken_value)
                for index in col_indices:
                    print("COLIndex: " + str(index))
                    print("COL Value: " + str(squares[index]))
                    # need to add that it's not the current one being tested
                    if len(squares[index]) == 1 and index != i:
                        taken_value = str(squares[index][0])

                        try:
                            print("COL OLD square list: " + str(square))
                            print("COL Removing taken value: " + taken_value)
                            square = list(square)
                            square.remove(taken_value)
                            square = tuple(square)
                            squares[i] = square
                            print("NEW square list: " + str(square))
                        except ValueError:
                            print("Error")
                            pass
                i+=1
        j=1
        # for index in col_indices:
        #     if len(squares[index]) == 1:
        #                 # remove that value from the current square's list
        #         pass
        #         # then do the same for box box_indices
        for square in squares:
            print("____!!!!______{}{}".format(j, square))
            j += 1
                # end of for loop: go to next square and do it all again

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

# helper functions
    def determineCol(self, index):
        col_indices = []
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



app = wx.App()
Solver(None, title="Sudoku Solver")
app.MainLoop()
