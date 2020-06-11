import wx


# need to make puzzle solver work for more advanced puzzles
# need to fix code style/add comments
# make sure default input box row actually works
# update README

class Solver(wx.Frame):
    def __init__(self, parent, title):
        super(Solver, self).__init__(parent, title=title, size=(792, 820))
        self.SetSizeHints(792,820,792,820)
        self.my_controls = []
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.InitUI()
        self.Centre()
        self.Show()

    def clearPuzzle(self, event):
        for i in range(81):
            self.my_controls[i].SetValue("")
            self.my_controls[i].SetForegroundColour(wx.BLACK)

    def importPuzzle(self, event):
        # Create text input

        input_box = wx.TextEntryDialog(self, "Enter 81 values to enter into puzzle (use '.' for blank squares)",'Puzzle Input')
        input_box.SetValue("....1.82...46.........3..4.7682.5...1.....7...4....2..2.7....1.8.3.........3...5.")
        if input_box.ShowModal() == wx.ID_OK:
            print('You entered: %s\n' % input_box.GetValue())
            input_box.GetValue()
            self.saveData(input_box.GetValue())
        input_box.Destroy()



    def saveData(self, input):
        i = 0
        for char in input:
            if char == ".":
                self.my_controls[i].SetValue("")
            else:
                self.my_controls[i].SetValue(char)
            self.my_controls[i].SetForegroundColour(wx.BLACK)
            i += 1

    def checkRulesAndEliminate(self, indices, squares, square, i):


        for index in indices:
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
                    # print("Error")
                    pass
        return square

    def testUniqueness(self, indices, squares, square, i):
        for square_value in square:
            if len(square) == 1:
                break
            found_value = False
            for index in indices:
                print("----------------------------------INDEX:" + str(index))
                if index != i:
                    for opponent_value in squares[index]:
                        if opponent_value == square_value:
                            found_value = True

            if not found_value:
                    # print("FOUND UNIQUE ROW VALUE")
                    # print("UR OLD Square: " + str(square))
                    # set that square to that value
                square = tuple(square_value)
                    # print("UR NEW square list: " + str(square))
                squares[i] = square
                break
        return square


            # for square_value in square:
            #     if len(square) == 1:
            #         break
            #     found_value = False
            #     for index in row_indices:
            #         if index != i:
            #             for opponent_value in squares[index]:
            #                 if opponent_value == square_value:
            #                     found_value = True
            #
            #     if not found_value:
            #         print("FOUND UNIQUE ROW VALUE")
            #         print("UR OLD Square: " + str(square))
            #         # set that square to that value
            #         square = tuple(square_value)
            #         print("UR NEW square list: " + str(square))
            #         squares[i] = square
            #         break


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
        while(num_of_times_through < 100 and filled_in < 81):
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

                    # for index in row_indices:
                    #     # print("index" + str(index))
                    #     if len(squares[index]) == 1 and index != i:
                    #         # remove that value from the current square's list
                    #         # this is a list
                    #         taken_value = str(squares[index][0])
                    #         # print("Taken Value:" + taken_value)
                    #         # print("type of taken value: " + str(type(taken_value)))
                    #
                    #         # try:
                    #         #     print("Removing taken value: " + taken_value)
                    #         #     square.remove(taken_value)
                    #         #     print("Getting here")
                    #         # except ValueError:
                    #         #     print("GGGGGGetting an error")
                    #         #     pass
                    #         try:
                    #             # print("OLD square list: " + str(square))
                    #             # print("Removing taken value: " + taken_value)
                    #             square = list(square)
                    #             square.remove(taken_value)
                    #             square = tuple(square)
                    #             squares[i] = square
                    #             # squares[i] = square
                    #             # print("NEW square list: " + str(square))
                    #         except ValueError:
                    #             # print("Error")
                    #             pass
                    square = self.checkRulesAndEliminate(row_indices, squares, square, i)
                    square = self.checkRulesAndEliminate(col_indices, squares, square, i)
                    square = self.checkRulesAndEliminate(box_indices, squares, square, i)

                    square = self.testUniqueness(row_indices, squares, square, i)
                    square = self.testUniqueness(col_indices, squares, square, i)
                    square = self.testUniqueness(box_indices, squares, square, i)



                                # square.remove(taken_value)
                    # for index in col_indices:
                    #     # print("COLIndex: " + str(index))
                    #     # print("COL Value: " + str(squares[index]))
                    #     # need to add that it's not the current one being tested
                    #     if len(squares[index]) == 1 and index != i:
                    #         taken_value = str(squares[index][0])
                    #
                    #         try:
                    #             print("COL OLD square list: " + str(square))
                    #             print("COL Removing taken value: " + taken_value)
                    #             square = list(square)
                    #             square.remove(taken_value)
                    #             square = tuple(square)
                    #             squares[i] = square
                    #             print("NEW square list: " + str(square))
                    #         except ValueError:
                    #             print("Error")
                    #             pass
                    #
                    # for index in box_indices:
                    #     if (len(square) == 1):
                    #         break
                    #     if len(squares[index]) == 1 and index != i:
                    #         taken_value = str(squares[index][0])
                    #
                    #         try:
                    #             print("BOX OLD square list: " + str(square))
                    #             print("BOX Removing taken value: " + taken_value)
                    #             square = list(square)
                    #             square.remove(taken_value)
                    #             square = tuple(square)
                    #             squares[i] = square
                    #             print("NEW square list: " + str(square))
                    #         except ValueError:
                    #             print("Error")
                    #             pass


                    # testing row uniqueness
                    # for square_value in square:
                    #     if len(square) == 1:
                    #         break
                    #     found_value = False
                    #     for index in row_indices:
                    #         if index != i:
                    #             for opponent_value in squares[index]:
                    #                 if opponent_value == square_value:
                    #                     found_value = True
                    #
                    #     if not found_value:
                    #         print("FOUND UNIQUE ROW VALUE")
                    #         print("UR OLD Square: " + str(square))
                    #         # set that square to that value
                    #         square = tuple(square_value)
                    #         print("UR NEW square list: " + str(square))
                    #         squares[i] = square
                    #         break
                    #
                    # # testing col uniqueness
                    # for square_value in square:
                    #     if len(square) == 1:
                    #         break
                    #     found_value = False
                    #     for index in col_indices:
                    #         if index != i:
                    #             for opponent_value in squares[index]:
                    #                 if opponent_value == square_value:
                    #                     found_value = True
                    #
                    #     if not found_value:
                    #         print("FOUND UNIQUE COL VALUE")
                    #         print("UC OLD Square: " + str(square))
                    #         # set that square to that value
                    #         square = tuple(square_value)
                    #         print("NEW square list: " + str(square))
                    #         squares[i] = square
                    #         break
                    #
                    # # testing box uniqueness
                    # for square_value in square:
                    #     if len(square) == 1:
                    #         break
                    #     found_value = False
                    #     for index in box_indices:
                    #         if index != i:
                    #             for opponent_value in squares[index]:
                    #                 if opponent_value == square_value:
                    #                     found_value = True
                    #
                    #     if not found_value:
                    #         print("FOUND UNIQUE BOX VALUE")
                    #         print("UB OLD Square: " + str(square))
                    #         # set that square to that value
                    #         square = tuple(square_value)
                    #         print("NEW square list: " + str(square))
                    #         squares[i] = square
                    #         break



                    if len(square) == 1:
                        # make it appear
                        self.my_controls[i].SetForegroundColour(wx.RED)
                        self.my_controls[i].SetValue(square[0])
                        # print("Adding one to filled in")
                        # print("------------------------------GOT IT" + str(square[0]))
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


        index_entered = -1
        value_entered = -1

        if self.my_controls[event.GetId()].GetValue() == "":
            # do blue or white here
            # print("BLANK VALUE")
            if self.getQuadrantColor(event.GetId()) == "Blue":
                # print("AYYYYE")
                self.my_controls[event.GetId()].SetBackgroundColour((211, 232, 245))
            else:
                # print("NAY")
                self.my_controls[event.GetId()].SetBackgroundColour((255, 255, 255))

            # for num in range(9):
            #     current_num = num + 1
            #     current_match_list = []
            #
            #     row_indices = self.determineRow(event.GetId())
            #     col_indices = self.determineCol(event.GetId())
            #     box_indices = self.determineBox(event.GetId())
            #
            #     for index in row_indices:
            #         if str(current_num) == self.my_controls[index].GetValue():
            #             current_match_list.append(index)
            #             print("Current match list: " + str(current_match_list))
            #
            #     if len(current_match_list) == 1:
            #         # do blue or white here
            #         if self.getQuadrantColor(current_match_list[0]) == "Blue":
            #             self.my_controls[current_match_list[0]].SetBackgroundColour((211, 232, 245))
            #         else:
            #             self.my_controls[current_match_list[0]].SetBackgroundColour((255, 255, 255))
            #
            #     current_match_list = []
            #     for index in col_indices:
            #         if str(current_num) == self.my_controls[index].GetValue():
            #             current_match_list.append(index)
            #             print("col Current match list: " + str(current_match_list))
            #     if len(current_match_list) == 1:
            #         # do blue or white here
            #         if self.getQuadrantColor(current_match_list[0]) == "Blue":
            #             self.my_controls[current_match_list[0]].SetBackgroundColour((211, 232, 245))
            #         else:
            #             self.my_controls[current_match_list[0]].SetBackgroundColour((255, 255, 255))
            #
            #     current_match_list = []
            #     for index in box_indices:
            #         if str(current_num) == self.my_controls[index].GetValue():
            #             current_match_list.append(index)
            #             print("box Current match list: " + str(current_match_list))
            #
            #     if len(current_match_list) == 1:
            #         # do blue or white here
            #         if self.getQuadrantColor(current_match_list[0]) == "Blue":
            #             self.my_controls[current_match_list[0]].SetBackgroundColour((211, 232, 245))
            #         else:
            #             self.my_controls[current_match_list[0]].SetBackgroundColour((255, 255, 255))




            # need to turn back
        else:
            try:
                index_entered = event.GetId()
                # print("index entered: " + str(event.GetId()))
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

        # if value_entered >= 1 and value_entered <= 9:
        # # go through here and see if not allowed based on rules of row, col, and box
        # # row:
        #     row_indices = self.determineRow(index_entered)
        #     list_of_matching = []
        #
        #     row_dup = False
        #     for index in row_indices:
        #         if self.my_controls[index].GetValue() == str(value_entered):
        #             print("1 There's a match")
        #             list_of_matching.append(index)
        #     for index in list_of_matching:
        #         if len(list_of_matching) > 1:
        #             self.my_controls[index].SetBackgroundColour((182, 108, 121))
        #             print("RED")
        #             row_dup = True
        #         else:
        #             if self.getQuadrantColor(index) == "Blue":
        #                 print("1 Turning blue")
        #                 self.my_controls[index].SetBackgroundColour((211, 232, 245))
        #             else:
        #                 self.my_controls[index].SetBackgroundColour((255, 255, 255))
        #                 print("1 Turning white")
        #
        #     # col:
        #     col_indices = self.determineCol(index_entered)
        #     list_of_matching = []
        #
        #     col_dup = False
        #     for index in col_indices:
        #         if self.my_controls[index].GetValue() == str(value_entered):
        #             list_of_matching.append(index)
        #             print("2 There's a match")
        #     for index in list_of_matching:
        #         if len(list_of_matching) > 1:
        #             self.my_controls[index].SetBackgroundColour((182, 108, 121))
        #             print("2 RED")
        #             col_dup = True
        #         else:
        #             if self.getQuadrantColor(index) == "Blue" and not index == index_entered:
        #                 self.my_controls[index].SetBackgroundColour((211, 232, 245))
        #                 print("2 Turning blue")
        #             elif self.getQuadrantColor(index) == "White" and not index == index_entered:
        #                 self.my_controls[index].SetBackgroundColour((255, 255, 255))
        #                 print("2 Turning white")
        #
        #
        #     # box:
        #     box_indices = self.determineBox(index_entered)
        #     list_of_matching = []
        #     for index in box_indices:
        #         if self.my_controls[index].GetValue() == str(value_entered):
        #             list_of_matching.append(index)
        #             print("3 There's a match")
        #     for index in list_of_matching:
        #         if len(list_of_matching) > 1:
        #             self.my_controls[index].SetBackgroundColour((182, 108, 121))
        #             print("3 RED")
        #         else:
        #             if self.getQuadrantColor(index) == "Blue" and not index == index_entered:
        #                 self.my_controls[index].SetBackgroundColour((211, 232, 245))
        #                 print("3 Turning blue")
        #             elif self.getQuadrantColor(index) == "White" and not index == index_entered:
        #                 self.my_controls[index].SetBackgroundColour((255, 255, 255))
        #                 print("3 Turning white")




            # num_the_same = 0
            # for index in row_indices:
            #     if (self.my_controls[index].GetValue() == str(value_entered)):
            #         num_the_same += 1
            #         if num_the_same > 1:
            #             self.my_controls[event.GetId()].SetBackgroundColour((182, 108, 121))
            #             print("yep that's a no go")
            #             break
            #         else:
            #             # need to determine quadrant for this
            #             self.my_controls[event.GetId()].SetBackgroundColour((255, 255, 255))

        # col:

            # col_indices = self.determineCol(index_entered)
            # num_the_same = 0
            # for index in col_indices:
            #     if (self.my_controls[index].GetValue() == str(value_entered)):
            #         num_the_same += 1
            #         if num_the_same > 1:
            #             self.my_controls[event.GetId()].SetBackgroundColour((182, 108, 121))
            #             print("yep that's a no go")
            #             break
            #         else:
            #             # need to determine quadrant for this
            #             self.my_controls[event.GetId()].SetBackgroundColour((255, 255, 255))

        # box:
            # box_indices = self.determineBox(index_entered)
            # num_the_same = 0
            # for index in box_indices:
            #     if (self.my_controls[index].GetValue() == str(value_entered)):
            #         num_the_same += 1
            #         if num_the_same > 1:
            #             self.my_controls[event.GetId()].SetBackgroundColour((182, 108, 121))
            #             print("yep that's a no go")
            #             break
            #         else:
            #             # need to determine quadrant for this
            #             self.my_controls[event.GetId()].SetBackgroundColour((255, 255, 255))
        # else:
        #     self.my_controls[event.GetId()].SetBackgroundColour((255, 255, 255))

            # how to turn back white upon exit

            # need to test to make sure it's not referring to current box


        # col:

        # box:


    def InitUI(self):
        vbox = wx.BoxSizer(wx.VERTICAL)

        gs = wx.GridSizer(9, 9, 0, 0)

        self.SetFont(wx.Font(78, wx.SWISS, wx.NORMAL, wx.NORMAL, False,'MS Shell Dlg 2'))
        for i in range(81):
            #gs.Add(wx.ComboBox(self, 15, "X", choices=["X", "1", "2", "3", "4", "5", "6", "7", "8", "9"], style = wx.CB_READONLY)
            self.text_control = wx.TextCtrl(self, id==i, value="", size=(88,88), style = wx.TE_CENTRE)
            # self.text_control.SetForegroundColour(wx.BLACK)

            if (self.getQuadrant(i) == 0 or self.getQuadrant(i) == 6 or self.getQuadrant(i) == 30 or self.getQuadrant(i) == 54 or self.getQuadrant(i) == 60):
                # print("I: " + str(i))
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
        butt0 = wx.Button(self, wx.ID_ANY, "Clear Puzzle", (303 ,772))
        butt0.Bind(wx.EVT_BUTTON, self.clearPuzzle)
        butt1 = wx.Button(self, wx.ID_ANY, "Solve Puzzle", (398, 772))
        butt1.Bind(wx.EVT_BUTTON, self.onClick)
        butt2 = wx.Button(self, wx.ID_ANY, "Import puzzle", (493, 772))
        butt2.Bind(wx.EVT_BUTTON, self.importPuzzle)




        vbox.Add(gs, proportion=1, flag=wx.EXPAND)
        self.SetSizer(vbox)



    def OnPaint(self, event=None):
        dc = wx.PaintDC(self)
        dc.Clear()
        # dc.SetPen(wx.Pen(wx.BLACK, 4))

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

    def getQuadrantColor(self, index):
        start_number = self.getQuadrant(index)
        if self.getQuadrant(index) == 0 or self.getQuadrant(index) == 6 or self.getQuadrant(index) == 30 or self.getQuadrant(index) == 54 or self.getQuadrant(index) == 60:
            return "White"
        else:
            return "Blue"


app = wx.App()
Solver(None, title="Sudoku Solver")
app.MainLoop()
