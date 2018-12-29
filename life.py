#
# life.py - Game of Life lab
#
# Name: Christina Li
# Pledge: I pledge my honor that I have abided by the Stevens Honor System. -cli50
#

import random

def createOneRow(width):
    """Returns one row of zeros of width "width"...  
       You should use this in your
       createBoard(width, height) function."""
    row = []
    for col in range(width):
        row += [0]
    return row

def createBoard(width, height):
    """ returns a 2d array with "height" rows and "width" cols """ 
    A = []
    for row in range(height):
        A += [int(width) * [0]]
    return A

import sys
def printBoard(A):
    """ this function prints the 2d list-of-lists
    A without spaces (using sys.stdout.write)"""
    for row in A:
        for col in row:
            sys.stdout.write(str(col))
        sys.stdout.write( '\n' )

def diagonalize(width,height):
    """ creates an empty board and then modifies it
        so that it has a diagonal strip of "on" cells.
    """
    A = createBoard( width, height )
    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0
    return A

def innerCells(w,h):
    A = createBoard(w,h)
    for row in range(h-1):
        for col in range(w-1):
            if row == 0 or col == 0:
                A[row][col] = 0
            else:
                A[row][col] = 1  
    return A

def randomCells(w,h):
    A = createBoard(w,h)
    for row in range(h-1):
        for col in range(w-1):
            if row == 0 or col == 0:
                A[row][col] = 0
            else:
                A[row][col] = random.choice([0,1]) 
    return A

def copy(A):
    newA = createBoard(len(A[0]), len(A))
    for row in range(len(A)):
        for col in range(len(A[0])):
            newA[row][col] = A[row][col]
    return newA

def innerReverse(A):
    h = len(A)
    w = len(A[0])
    for row in range(h-1):
        for col in range(w-1):
            if row == 0 or col == 0:
                A[row][col] = 0
            elif A[row][col] == 0:
                A[row][col] = 1
            elif A[row][col] == 1:
                A[row][col] = 0
    return A

def countNeighbors(row,col,A):
    count = 0
    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            if A[r][c] == 1:
                count += 1
    if A[row][col] == 1:
        count -=1
    return count

def next_life_generation(A):
    """ makes a copy of A and then advanced one
        generation of Conway's game of life within
        the *inner cells* of that copy.
        The outer edge always stays 0.
    """
    B = copy(A)
    for row in range(len(A[0]) - 1):
        for col in range(len(A) - 1):
            if countNeighbors(row, col, A) < 2 or countNeighbors(row, col, A) > 3:
                B[row][col] = 0
            elif countNeighbors(row, col, A) == 3:
                B[row][col] = 1
            else:
                B[row][col] = A[row][col]
    return B

