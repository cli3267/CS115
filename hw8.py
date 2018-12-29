'''
Created on Oct 29, 2017
@author:   Christina Li
Pledge:    I pledge my honor that I have abided by the Stevens Honor System. cli50
'''

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s == '':
        return 0
    return 2 * binaryToNum(s[0:-1]) + int(s[-1])

def TcToNum(n):
    '''
    Takes in a string of 8 bits(n) and returns the corresponding integer.
    '''
    if n == "":
        return 0
    if n[0] == "1":
        return binaryToNum(n[1:])-128
    return binaryToNum(n[1:])

def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    return n % 2 == 1

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n == 0:
        return ''
    elif isOdd(n):
        return numToBinary(n//2) +'1'
    else:
        return numToBinary(n//2) + '0'

def pad(s):
    '''
    Returns the zeros of the binary number
    '''
    return (8-len(s)) * '0' + s

def NumToTc(N):
    '''
    Takes in an integer(N) and returns the string representing the two's complement representation of that integer. 
    '''
    if N >= 128 or N < -128:
        return "Error"
    elif N < 0:
        return pad(numToBinary(N+256))
    else:
        return pad(numToBinary(N))
