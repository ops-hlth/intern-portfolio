#
# ps9pr1.py (Problem Set 9, Problem 1)
#
# A Connect Four Board class
#
# Computer Science 111
#

class Board:
    """ a data type for a Connect Four board with arbitrary dimensions
    """   
    ### add your constructor here ###

    def __init__(self, height, width):
        """ constructs a new Board object by initializing the following
            three attributes:
            height - # of rows in the board
            width - # of columns in the board
            slots - a two-dimensional list that stores the current 
                    contents of the board
        """
        self.height = height 
        self.width = width 
        self.slots = [[' '] * self.width for row in range(self.height)]

    def __repr__(self):
        """ Returns a string that represents a Board object.
        """
        s = ''         #  begin with an empty string

        # add one row of slots at a time to s
        for row in range(self.height):
            s += '|'   # one vertical bar at the start of the row

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  # newline at the end of the row

        ### add your code here ###
        s += '--' * self.width
        s+= '-'
        s += '\n'
        for c in range(self.width):
            s += ' '
            s += str(c % 10)
        return s

    def add_checker(self, checker, col):
        """ adds the specified checker (either 'X' or 'O') to the
            column with the specified index col in the called Board.
            inputs: checker is either 'X' or 'O'
                    col is a valid column index
        """
        assert(checker == 'X' or checker == 'O')
        assert(col >= 0 and col < self.width)
        
        ### put the rest of the method here ###
        row = 0 
        while self.slots[row][col] == ' ':
            row += 1
            if self.slots[row][col] == 'X' or self.slots[row][col] == 'O':
                row -= 1
                break
            elif row == self.height-1:
                break  
        self.slots[row][col] = checker 
        
    ### add your reset method here ###
    def reset(self):
        """ resets the Board object by setting all slots to contain
            a space character. 
        """
        self.slots = [[' '] * self.width for row in range(self.height)]

    def add_checkers(self, colnums):
        """ takes a string of column numbers and places alternating
            checkers in those columns of the called Board object,
            starting with 'X'.
            input: colnums is a string of valid column numbers
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    ### add your remaining methods here
    def can_add_to(self, col):
        """ returns True if it is valid to place a checker in the column
            col on the calling Board object. Otherwise, returns False
        """
        count = 0 
        if col > self.width-1 or col < 0:
            return False 
        for row in range(self.height):
            if self.slots[row][col] != ' ':
                count += 1
        if count == self.height:
            return False
        else:
            return True 
        
    
    def is_full(self):
        """ returns True if the called Board object is completley full
            of checkers and False otherwise.
        """
        for row in range(self.height):
            for col in range(self.width):
                if self.can_add_to(col) == True:
                    return False 
        return True 
                
     
    def remove_checker(self, col):
        """ removes the top checker from column col of the called 
            board object
        """
        for row in range(self.height):
            if self.slots[row][col] != ' ':
                self.slots[row][col] = ' '
                break
            
    def is_win_for(self, checker):
        """ returns True if there are four consecutive slots containing
            checker on the board. Otherwise, returns False
        """
        assert(checker == 'X' or checker == 'O')
        
        if self.is_horizontal_win(checker) == True:
            return True 
        elif self.is_vertical_win(checker) == True:
            return True 
        elif self.is_down_diagonal_win(checker) == True:
            return True 
        elif self.is_up_diagonal_win(checker) == True:
            return True 
        else:
            return False 

    ### helper functions ###
    
    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row][col + 1] == checker and \
                   self.slots[row][col + 2] == checker and \
                   self.slots[row][col + 3] == checker:
                       return True          
        return False 
                
    def is_vertical_win(self, checker):
        """ Checks for a vertical win for the specified checker.
        """
        for row in range(self.height - 3):
            for col in range(self.width):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col] == checker and \
                   self.slots[row + 2][col] == checker and \
                   self.slots[row + 3][col] == checker:
                       return True
        return False 
    
    def is_down_diagonal_win(self, checker):
        """ Checks for a downward diagonal win for the specified 
            checker. 
        """
        for row in range(self.height - 3):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col + 1] == checker and \
                   self.slots[row + 2][col + 2] == checker and \
                   self.slots[row + 3][col + 3] == checker:
                       return True
        return False 
                
    def is_up_diagonal_win(self, checker):
        """ Checks for an upward diagonal win for the specified 
            checker. 
        """
        for row in range(3, self.height):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row - 1][col + 1] == checker and \
                   self.slots[row - 2][col + 2] == checker and \
                   self.slots[row - 3][col + 3] == checker:
                       return True
        return False 
                
        
    
    
                