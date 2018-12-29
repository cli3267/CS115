'''
Created on Dec 3, 2017

@author: christinali
Pledge: "I pledge my honor that I have abided by the Stevens Honor System." -cli50
'''
class Board(object):
    def __init__(self, width=7, height=6):
        self.__width = width
        self.__height = height
        self.__board = self.createBoard()
      
    def __str__(self):
        """Returns a string representing the Board object that calls it"""
        S = ''
        for row in range(self.__height):
            R = ''
            for col in range(self.__width):
                R += '|' + self.__board[row][col]
            S += R + '|\n'
        S += (self.__width + 1) * 2 * '-'  + '\n'
        for x in range(self.__width):
            S += ' ' + str(x)
        return S  
    
    def createBoard(self):
        '''Returns an empty board with its width and height'''
        board = []
        for row in range(self.__height):
            R = []
            for col in range(self.__width):
                R += [' ']
            board += [R]
        return board
    
    def allowsMove(self, col):
        '''Returns True if the calling Board object can allow a move into col, other returns false.'''
        if col not in range(self.__width) or self.__board[0][col] != " ":
            return False
        return True
        
    def addMove(self, col, ox):
        '''Adds an ox character in the given column if possible.'''
        if self.allowsMove(col) == True:
            addRow = -1
            for row in self.__board:
                if row[col] == ' ':
                    addRow += 1
                else:
                    break
            self.__board[addRow][col] = ox
        
    def setBoard(self,moveString):
        """ takes in a string of columns and places
         alternating checkers in those columns,
         starting with 'X'
        
         For example, call b.setBoard('012345')
         to see 'X's and 'O's alternate on the
         bottom row, or b.setBoard('000000') to
         see them alternate in the left column.
         moveString must be a string of integers
         """
        nextCh = 'X' # start by playing 'X'
        for colString in moveString:
            col = int(colString)
            if 0 <= col <= self.width:
                    self.addMove(col, nextCh)
                    if nextCh == 'X': nextCh = 'O'
                    else: nextCh = 'X'
                    
    def delMove(self, col):
        """Removes the top checker from the col"""
        for row in self.__board:
            if row[col] != ' ':
                row[col] = " "

    
    def winsFor(self, ox):
        """Returns True if the checker, X or O in ox has won the calling board, otherwise returns False"""
        for row in range(self.__height):
            hCount = 0
            for col in range(self.__width):
                if self.__board[row][col] == ox:
                    hCount +=1
                    if hCount >= 4:
                        return True
                else:
                    hCount = 0
        for col in range(self.__width):
            vCount = 0
            for row in range(self.__height):
                if self.__board[row][col] == ox:
                    vCount += 1
                    if vCount >= 4:
                        return True
                else:
                    vCount = 0
        for col in range(self.__width):
            x = col
            y = 0
            count = 0
            while  x < self.__width and y < self.__height:
                if self.__board[y][x] == ox:
                    count += 1
                    if count >= 4:
                        return True
                    else:
                        y += 1
                        x += 1
                else:
                    count = 0
                    y += 1
                    x += 1          
        for row in range(self.__height):
            x = 0
            y = row
            count = 0
            while y < self.__height and x < self.__width:
                if self.__board[y][x] == ox:
                    count += 1
                    if count >= 4:
                        return True
                    else:
                        y += 1
                        x += 1
                else:
                    count = 0
                    y += 1
                    x += 1         
        for col in range(self.__width):
            x = col
            y = self.__height - 1
            count = 0
            while y > -1 and x < self.__width:
                if self.__board[y][x] == ox:
                    count += 1
                    if count >= 4:
                        return True
                    else:
                        y -= 1
                        x += 1
                else:
                    count = 0
                    y -= 1
                    x += 1           
        for row in range(self.__height):
            x = 0
            y = row
            count = 0
            while y > -1 and x < self.__width:
                if self.__board[y][x] == ox:
                    count += 1
                    if count >= 4:
                        return True
                    else:
                        y -= 1
                        x += 1
                else:
                    count = 0
                    y -= 1
                    x += 1  
        return False
    
    def hostGame(self):
        """Runs a loop allowing the user to play a game."""
        print("Welcome to Connect Four!")
        print(self)
        C = "X"
        while self.winsFor(C) == False:
            E = int(input(C + "'s choice: "))
            if self.allowsMove(E) == False:
                E = int(input("You cannot do that. Please enter a different choice: "))
            self.addMove(E, C)
            if self.winsFor(C) == True:
                print(C + " wins -- Congratulations!")
                print(self)
            else:
                print(self)
                if C == "X":
                    C = "O"
                elif C == "O":
                    C = "X"
                                                 
if __name__ == "__main__":

    a = Board(7,6)
    a.hostGame()