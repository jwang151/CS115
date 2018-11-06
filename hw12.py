'''
Created on Dec 5, 2017

@author: wangj
Pledge: I pledge my honor that I have abided by the Stevens Honor System. 
'''
class Board(object):
    ''' This is a constructor that takes in two named arguments one for row and one for column'''
    def __init__(self, width=7, height=6):
        self.__width = width
        self.__height = height
        self.__board = []
        
        for row in range(self.__height): 
            row = []
            for col in range(self.__width):
                row += [' ']
            self.__board.append(row)
            
    def __str__(self):
        '''This returns a string (it does not print a string) representing the Board object that calls it'''
        nBoard = ''
        for row in range(self.__height):
            nRow = '|'
            for col in range(self.__width):
                nRow += self.__board[row][col] + '|'
            nRow += '\n'
            nBoard += nRow
        nBoard += '-' * len(nRow) + '\n'
        
            
        for n in range(self.__width):
            nBoard += ' ' + str(n)
        return nBoard
    
    def allowsMove(self,col):
        ''' This method checks that col is in the range from 0 to the last column and makes sure that there is room left in the column.'''
        if col not in range(self.__width):
            return False
        if self.__board[0][col] != ' ':
            return False
        return True
    
    def addMove(self, col, ox):
        '''This method should add an ox checker, where ox is a variable
holding a string that is either "X" or "O", into column col '''
        row = 0
        while row in range(self.__height) and self.__board[row][col] == ' ':
            if row == self.__height:
                self.__board[row][col] = ox
            else:
                row += 1
        self.__board[row - 1][col] = ox
        
    def setBoard(self, move_string):
        """ takes in a string of columns and places
        alternating checkers in those columns,
        starting with 'X'
        For example, call b.setBoard('0123456')
        to see 'X's and 'O's alternate on the
        bottom row, or b.setBoard('000000') to
        see them alternate in the left column.
        moveString must be a string of integers
        """
        nextCh = 'X' # start by playing 'X'
        for colString in move_string:
            col = int(colString)
            if 0 <= col <= self.__width:
                self.addMove(col, nextCh)
            if nextCh == 'X': 
                nextCh = 'O'
            else: 
                nextCh = 'X'
    
    def delMove(self, col):
        '''  This method should do the "opposite" of addMove. That is, it should
remove the top checker from the column col.'''
        row = 0
        while row in range(self.__height):
            if row == self.__height and self.__board[row][col] == ' ':
                pass
            elif self.__board[row][col] == ' ':
                row += 1
            else:
                self.__board[row][col] = ' '

    def winsFor(self, ox):
        ''' This method should return True if the given checker, 'X' or 'O', held
in ox, has won the calling Board'''
        for row in range(self.__height):
            for col in range(self.__width - 3):
                if self.__board[row][col] == ox:
                    if self.__board[row][col + 1] == ox and \
                    self.__board[row][col + 2] == ox and \
                    self.__board[row][col + 3] == ox:
                        return True
        for row in range(self.__height - 3):
            for col in range(self.__width):            
                if self.__board[row][col] == ox:
                    if self.__board[row + 1][col] == ox and \
                        self.__board[row + 2][col] == ox and \
                        self.__board[row + 3][col] == ox:
                        return True
        for row in range(3, self.__height):
            for col in range(self.__width - 3):
                if self.__board[row][col] == ox:
                    if self.__board[row - 1][col + 1] == ox and \
                        self.__board[row - 2][col + 2] == ox \
                        and self.__board[row - 3][col + 3] == ox:
                        return True
        for row in range(3, self.__height):
            for col in range(3, self.__width):
                if self.__board[row][col] == ox:
                    if self.__board[row - 1][col - 1] == ox and \
                        self.__board[row - 2][col - 2] == ox \
                        and self.__board[row - 3][col - 3] == ox:
                        return True
        return False
            
    def hostGame(self):
        '''This is a method that, when called from a connect four board object, will
run a loop allowing the user(s) to play a game. '''
        checker = 'X'
        print('Welcome to Connect Four! \n')
        print(self, '\n')
        
        while self.winsFor(checker) == False:
            choice = int(input(checker + "'s Choice: "))
            if self.allowsMove(choice) == False:
                choice = int(input("Not a valid move. Please Try again: "))
            self.addMove(choice, checker)
            
            if self.winsFor(checker) == True:
                print(checker + " Wins -- Congratulations!")
                print(self, '\n')
            else:
                print(self, '\n')
                if checker == "X":
                    checker = "O"
                else:
                    checker = "X"
                    
if __name__ == "__main__":

    b = Board()
    b.hostGame()

