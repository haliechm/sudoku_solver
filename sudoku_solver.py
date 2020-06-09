import wx

class Solver(wx.Frame):
    def __init__(self, parent, title):
        super(Solver, self).__init__(parent, title=title, size=(792, 820))

        self.my_controls = []
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.InitUI()
        self.Centre()
        self.Show()

    def clearPuzzle(self, event):
        for i in range(81):
            self.my_controls[i].SetValue("")

    def onClick(self, event):



        possibilities = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
        squares = []
        for i in range(81):
            squares.append(possibilities)

        filled_in = 0
        i=0
        for sq in self.my_controls:
            if(sq.GetValue() != ""):
                # print("Not a blank square")
                squares[i] = tuple(sq.GetValue())
                filled_in += 1
                # print("Blank square")
            i+=1

        print("Filled in: " + str(filled_in))

        # above is working correctly
        num_of_times_through = 0
        while(num_of_times_through < 10 and filled_in < 81):
            print("Filled in: " + str(filled_in))
            print("----dddd----" + str(num_of_times_through))
            num_of_times_through += 1
            i=0
            for square in squares:

                if len(square) == 1:
                    # go to next loop
                    # print("ONLY one value in current square")
                    i+=1
                    continue

                else:
                    # print("MORE than one value in current square")
                    row_indices = self.determineRow(i)
                    # print("ROW INDICES: " + str(row_indices))
                    col_indices = self.determineCol(i)
                    # print("COL INDICES: " + str(col_indices))
                    box_indices = self.determineBox(i)
                    # print("BOX INDICES: " + str(box_indices))

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
                                pass
                                # print("No taken value to be done")
                                # for value in square:
                                #     # print("------Value:" + value)
                                #     # print("type of value: " + str(type(value)))
                                #     if value == taken_value:
                                #         print("HOORAH")
                                #     else:
                                #         print("BOOOOO")


                                # square.remove(taken_value)
                    for index in col_indices:
                        # print("COLIndex: " + str(index))
                        # print("COL Value: " + str(squares[index]))
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

                    for index in box_indices:
                        if (len(square) == 1):
                            break
                        if len(squares[index]) == 1 and index != i:
                            taken_value = str(squares[index][0])

                            try:
                                print("BOX OLD square list: " + str(square))
                                print("BOX Removing taken value: " + taken_value)
                                square = list(square)
                                square.remove(taken_value)
                                square = tuple(square)
                                squares[i] = square
                                print("NEW square list: " + str(square))
                            except ValueError:
                                print("Error")
                                pass


                    # testing row uniqueness
                    for square_value in square:
                        if len(square) == 1:
                            break
                        found_value = False
                        for index in row_indices:
                            if index != i:
                                for opponent_value in squares[index]:
                                    if opponent_value == square_value:
                                        found_value = True

                        if not found_value:
                            print("FOUND UNIQUE ROW VALUE")
                            print("UR OLD Square: " + str(square))
                            # set that square to that value
                            square = tuple(square_value)
                            print("UR NEW square list: " + str(square))
                            squares[i] = square
                            break

                    # testing col uniqueness
                    for square_value in square:
                        if len(square) == 1:
                            break
                        found_value = False
                        for index in col_indices:
                            if index != i:
                                for opponent_value in squares[index]:
                                    if opponent_value == square_value:
                                        found_value = True

                        if not found_value:
                            print("FOUND UNIQUE COL VALUE")
                            print("UC OLD Square: " + str(square))
                            # set that square to that value
                            square = tuple(square_value)
                            print("NEW square list: " + str(square))
                            squares[i] = square
                            break

                    # testing box uniqueness
                    for square_value in square:
                        if len(square) == 1:
                            break
                        found_value = False
                        for index in box_indices:
                            if index != i:
                                for opponent_value in squares[index]:
                                    if opponent_value == square_value:
                                        found_value = True

                        if not found_value:
                            print("FOUND UNIQUE BOX VALUE")
                            print("UB OLD Square: " + str(square))
                            # set that square to that value
                            square = tuple(square_value)
                            print("NEW square list: " + str(square))
                            squares[i] = square
                            break



                    if len(square) == 1:
                        # make it appear
                        self.my_controls[i].SetForegroundColour(wx.RED)
                        self.my_controls[i].SetValue(square[0])
                        print("Adding one to filled in")
                        filled_in += 1


                    i+=1

                    # filled_in += 1





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

    def testValidity(self, event):

        # print(type(event.GetString()))
        # print("ID: " + str(event.GetId()))
        if self.my_controls[event.GetId()].GetValue() == "":
            pass
        else:
            try:
                index_entered = event.GetId()
                value_entered = int(self.my_controls[index_entered].GetValue())
                if value_entered <= 0 or value_entered >= 10:
                    # print("Not allowed")
                    # self.text_control.SetValue("8")
                    self.my_controls[index_entered].SetValue("")
            except ValueError:
                    # make it turn red here
                    # self.text_control.SetValue("")
                    # print("Getting here")
                    self.my_controls[index_entered].SetValue("")
                    # print("Not allowed")

        # go through here and see if not allowed based on rules of row, col, and box


    def InitUI(self):
        vbox = wx.BoxSizer(wx.VERTICAL)

        gs = wx.GridSizer(9, 9, 0, 0)

        self.SetFont(wx.Font(78, wx.SWISS, wx.NORMAL, wx.NORMAL, False,'MS Shell Dlg 2'))
        for i in range(81):
            #gs.Add(wx.ComboBox(self, 15, "X", choices=["X", "1", "2", "3", "4", "5", "6", "7", "8", "9"], style = wx.CB_READONLY)
            self.text_control = wx.TextCtrl(self, id==i, value="", size=(88,88), style = wx.TE_CENTRE)
            # self.text_control.SetForegroundColour(wx.BLACK)

            if (self.getQuadrant(i) == 0 or self.getQuadrant(i) == 6 or self.getQuadrant(i) == 30 or self.getQuadrant(i) == 54 or self.getQuadrant(i) == 60):
                print("I: " + str(i))
                pass
            else:
                self.text_control.SetBackgroundColour((211, 232, 245))

            self.text_control.SetId(i)
            # print("----ffff" + str(self.text_control.GetId()))
            self.text_control.SetMaxLength(1)
            self.text_control.Bind(wx.EVT_TEXT, self.testValidity, self.text_control, id=i)

            self.my_controls.append(self.text_control)
            #gs.Add(wx.TextCtrl(self, id==1, value="", size=(88,88), style = wx.TE_CENTRE))
            gs.Add(self.text_control)

        self.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False,'MS Shell Dlg 2'))
        butt1 = wx.Button(self, wx.ID_ANY, "Clear Puzzle", (303 ,760))
        butt1.Bind(wx.EVT_BUTTON, self.clearPuzzle)
        butt = wx.Button(self, wx.ID_ANY, "Solve Puzzle", (398, 760))
        butt.Bind(wx.EVT_BUTTON, self.onClick)




        vbox.Add(gs, proportion=1, flag=wx.EXPAND)
        self.SetSizer(vbox)



    def OnPaint(self, event=None):
        dc = wx.PaintDC(self)
        dc.Clear()
        dc.SetPen(wx.Pen(wx.BLACK, 4))

        x=0
        for i in range(10):

            # if i==3 or i==6:
            #     dc.SetPen(wx.Pen(wx.GREEN, width=4))
            # else:
            #     dc.SetPen(wx.Pen(wx.BLACK, 4))

            dc.DrawLine(x, 0, x, 792)
            x += 88


        y=0
        for j in range(10):

            # if j==3 or j==6:
            #     dc.SetPen(wx.Pen(wx.GREEN, 4))
            # else:
            #     dc.SetPen(wx.Pen(wx.BLACK, 4))

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

        mod9 = index % 9
        start_number = -1

        if mod9 <= 2:
            if index <= 20:
                start_number = 0
            elif index <= 47:
                start_number = 27
            else:
                start_number = 54
        elif mod9 <= 5:
            if index <= 23:
                start_number = 3
            elif index <= 50:
                start_number = 30
            else:
                start_number = 57
        elif mod9 <= 8:
            if index <= 26:
                start_number = 6
            elif index <= 53:
                start_number = 33
            else:
                start_number = 60

        box_indices = []

        for i in range(9):
            if i != 2 and i != 5 and i != 8:
                # print("here")
                box_indices.append(start_number)
                start_number += 1
            else:
                # print("now here")
                box_indices.append(start_number)
                start_number += 7

        return box_indices

    def getQuadrant(self, index):

        indices = self.determineBox(index)
        start_number = indices[0]

        return start_number









app = wx.App()
Solver(None, title="Sudoku Solver")
app.MainLoop()
