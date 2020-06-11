# using wxpython for GUI
import wx


# need to make puzzle solver work for more advanced puzzles
# need to fix code style/add comments
# make sure default input box row actually works: doesn't work: ....1.82...46.........3..4.7682.5...1.....7...4....2..2.7....1.8.3.........3...5.
# update README

# solves sudoku puzzles
# works on many puzzles (on sudoku.com solves most easy, med, hard puzzles but not all puzzles (yet))
class Solver(wx.Frame):
    def __init__(self, parent, title):
        super(Solver, self).__init__(parent, title=title, size=(792, 820))
        # max and min window size set to the same dimensions
        self.SetSizeHints(792,820,792,820)
        self.my_controls = []
        self.InitUI()
        self.Centre()
        self.Show()

    # resets all squares to be blank
    def clearPuzzle(self, event):
        for i in range(81):
            self.my_controls[i].SetValue("")
            self.my_controls[i].SetForegroundColour(wx.BLACK)

    # can input numbers into window rather directly into squares
    # use '.' for blank squares (must input 81 characters)
    # use https://qqwing.com/generate.html on simple/easy to get puzzles in this format
    def importPuzzle(self, event):
        input_box = wx.TextEntryDialog(self, "Enter 81 values to enter into puzzle (use '.' for blank squares)",'Puzzle Input')
        # default example of input/format
        input_box.SetValue("..12....4..4.....9.........7.582.1..3....7.9..4.31.7.22...319.........8...74....5")
        if input_box.ShowModal() == wx.ID_OK:
            input_box.GetValue()
            self.saveData(input_box.GetValue())
        input_box.Destroy()

    # used when importing puzzle to set the squares to the corresponding values
    def saveData(self, input):
        i = 0
        for char in input:
            if char == ".":
                # blank square
                self.my_controls[i].SetValue("")
            else:
                # filled in square
                self.my_controls[i].SetValue(char)
            self.my_controls[i].SetForegroundColour(wx.BLACK)
            i += 1

    # goes through either the row, column, or quadrant of current square
    # and eliminates possible numbers from that squares
    # EX: square [0,0] rn has possibilities of 1, 2, 4, & 9 butt there is
    # a 9 in the row, so the new possibilities of the square are 1, 2, & 4
    def checkRulesAndEliminate(self, indices, squares, square, i):
        for index in indices:
            # if there is only one numb in a square than remove that num from possibilites
            if len(squares[index]) == 1 and index != i:
                # remove that value from the current square's list
                taken_value = str(squares[index][0])

                try:
                    # need to do this b/c of mutability of lists
                    square = list(square)
                    square.remove(taken_value)
                    square = tuple(square)
                    squares[i] = square
                except ValueError:
                    # gets here if taken value isn't a possibility of current square
                    pass
        return square

    # determines if there exists a 'unique value' for the current square
    # and sets that square's value to the 'unique value' iff so
    # EX: square [0,0] has possibilities 1, 2, & 4 but no other square in the row
    # has a possibility of being a 2, so square [0,0] must be 2
    def testUniqueness(self, indices, squares, square, i):
        for square_value in square:
            if len(square) == 1:
                break
            found_value = False
            for index in indices:
                if index != i:
                    for opponent_value in squares[index]:
                        if opponent_value == square_value:
                            found_value = True

            # found a 'unique value'
            if not found_value:
                square = tuple(square_value)
                squares[i] = square
                break
        return square


    # function called when "Solve Puzzle" button is clicked
    # solves the puzzle and puts answers in red
    def onClick(self, event):
        # each square is inherently given the possibility of being any number
        possibilities = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
        squares = []
        for i in range(81):
            squares.append(possibilities)

        # filled in used to determine when to stop looping through solution
        # if puzzle is unsolvable then use num_of_times_through to stop loop after 100 times
        filled_in = 0
        num_of_times_through = 0

        i=0
        for sq in self.my_controls:
            # setting the square possibilities to only one value if inputted
            if(sq.GetValue() != ""):
                squares[i] = tuple(sq.GetValue())
                filled_in += 1
            i+=1

        while(num_of_times_through <= 100 and filled_in < 81):
            num_of_times_through += 1
            i=0
            for square in squares:
                # if square already has only one value, then go to next iteration
                if len(square) == 1:
                    i+=1
                    continue
                # if square does not have only one value:
                else:
                    # deterimines indices of connected squares to current square
                    row_indices = self.determineRow(i)
                    col_indices = self.determineCol(i)
                    box_indices = self.determineBox(i)

                    # eliminates possibilities from current square's possibilities
                    square = self.checkRulesAndEliminate(row_indices, squares, square, i)
                    square = self.checkRulesAndEliminate(col_indices, squares, square, i)
                    square = self.checkRulesAndEliminate(box_indices, squares, square, i)

                    # determines if current square must be a certain value
                    square = self.testUniqueness(row_indices, squares, square, i)
                    square = self.testUniqueness(col_indices, squares, square, i)
                    square = self.testUniqueness(box_indices, squares, square, i)

                    # iff the # of possible values in current square is one, then set that square
                    if len(square) == 1:
                        # answers are in red
                        self.my_controls[i].SetForegroundColour(wx.RED)
                        self.my_controls[i].SetValue(square[0])
                        filled_in += 1

                    i+=1



    # called whenever text in a square is changed
    # number must be a number 1-9, if not then nothing appears when typing
    def testValidity(self, event):

        index_entered = -1
        value_entered = -1

        # if the square is blank (square was just erased)
        if self.my_controls[event.GetId()].GetValue() == "":
            # determine which quadrant the square is in and set to either White
            # or blue depending on location of square
            if self.getQuadrantColor(event.GetId()) == "Blue":
                self.my_controls[event.GetId()].SetBackgroundColour((211, 232, 245))
            else:
                self.my_controls[event.GetId()].SetBackgroundColour((255, 255, 255))

        # if there is a character placed into square
        else:
            try:
                index_entered = event.GetId()
                # tries to turn current value into an int (if str then error occurs)
                value_entered = int(self.my_controls[index_entered].GetValue())
                # makes sure value entered is a num from 1-9
                if value_entered <= 0 or value_entered >= 10:
                    self.my_controls[index_entered].SetValue("")

            # value entered was not a number
            except ValueError:
                    self.my_controls[index_entered].SetValue("")



    # GUI work
    def InitUI(self):
        vbox = wx.BoxSizer(wx.VERTICAL)

        # makes 9x9 grid
        gs = wx.GridSizer(9, 9, 0, 0)
        self.SetFont(wx.Font(78, wx.SWISS, wx.NORMAL, wx.NORMAL, False,'MS Shell Dlg 2'))
        # goes through all 81 squares and sets bkrnd color, max length, id
        for i in range(81):
            self.text_control = wx.TextCtrl(self, id==i, value="", size=(88,88), style = wx.TE_CENTRE)
            # sets square to white if in TL, TR, BL, BR, or center quadrant
            if (self.getQuadrant(i) == 0 or self.getQuadrant(i) == 6 or self.getQuadrant(i) == 30 or self.getQuadrant(i) == 54 or self.getQuadrant(i) == 60):
                self.text_control.SetBackgroundColour((255, 255, 255))
            # sets square to light blue if in any other quadrant
            else:
                self.text_control.SetBackgroundColour((211, 232, 245))

            self.text_control.SetId(i)
            # allows for only one character in each square
            self.text_control.SetMaxLength(1)
            # fnc testValidity called whenever square value is changed
            self.text_control.Bind(wx.EVT_TEXT, self.testValidity, self.text_control, id=i)
            self.my_controls.append(self.text_control)
            gs.Add(self.text_control)

        # makes the buttons along bottom of window
        self.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False,'MS Shell Dlg 2'))
        butt0 = wx.Button(self, wx.ID_ANY, "Clear Puzzle", (303 ,772))
        butt0.Bind(wx.EVT_BUTTON, self.clearPuzzle)
        butt1 = wx.Button(self, wx.ID_ANY, "Solve Puzzle", (398, 772))
        butt1.Bind(wx.EVT_BUTTON, self.onClick)
        butt2 = wx.Button(self, wx.ID_ANY, "Import puzzle", (493, 772))
        butt2.Bind(wx.EVT_BUTTON, self.importPuzzle)


        vbox.Add(gs, proportion=1, flag=wx.EXPAND)
        self.SetSizer(vbox)


# FOR REFERENCE - view of 'indices' of each box in sudoku puzzle:
# 00 01 02 03 04 05 06 07 08
# 9 10 11 12 13 14 15 16 17
# 18 19 20 21 22 23 24 25 26
# 27 28 29 30 31 32 33 34 35
# 36 37 38 39 40 41 42 43 44
# 45 46 47 48 49 50 51 52 53
# 54 55 56 57 58 59 60 61 62
# 63 64 65 66 67 68 69 70 71
# 72 73 74 75 76 77 78 79 80


# helper functions
    # returns indices of the column the square is in
    def determineCol(self, index):
        col_indices = []
        start_number = index % 9

        for i in range(9):
            col_indices.append(start_number)
            start_number += 9

        return col_indices

    # returns indices of the row the square is in
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

    # returns indices of the box the square is in
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

    # returns the first index number of the box the current square is in
    def getQuadrant(self, index):

        indices = self.determineBox(index)
        start_number = indices[0]

        return start_number

    # uses the first number of the quadrant the square is in to determine color
    def getQuadrantColor(self, index):
        start_number = self.getQuadrant(index)
        if self.getQuadrant(index) == 0 or self.getQuadrant(index) == 6 or self.getQuadrant(index) == 30 or self.getQuadrant(index) == 54 or self.getQuadrant(index) == 60:
            return "White"
        else:
            return "Blue"


app = wx.App()
Solver(None, title="Sudoku Solver")
app.MainLoop()
