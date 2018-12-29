'''
Created on October 12, 2017
@author:   Christina Li
Pledge:    I pledge my honor that I have abided by the Stevens Honor System. -cli50

CS115 - Lab 6
'''
def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    return n % 2 == 1
#the binary number for 42 is 101010
#2 ** 5 = 32 -> 1
#2 ** 4 = 16 -> 0
#2 ** 3 = 8 -> 1
#2 ** 2 = 4 -> 0
#2 ** 1 = 2 -> 1
#2 ** 0 = 1 -> 0
"""If N is odd,return the value with 1 at the end.
   If N is even, return the value with 0 at the end. """
"""Integer division the decimal number by 2"""
"""Integer division the decimal number by 2 will find the binary version as the remainder would give us the binary number,
    then reading the answer from back to front."""

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

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s == '':
        return 0
    return 2 * binaryToNum(s[0:-1]) + int(s[-1])

def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    s = numToBinary(binaryToNum(s) + 1)
    if len(s) > 8:
        return s[1:]
    else:
        return (8-len(s)) * '0' + s
    
def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    print(s)
    if n == 0: 
        return
    return count(increment(s),n-1)

"""The ternary value for 59 is 2012 because 2 * (3**0) + 1 * (3**1) + 0 * (3**2) + 2 * (3**3) = 59"""

def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0 the empty string is returned.'''
    if n == 0:
        return ''
    return numToTernary(n//3) + str(n%3)
 
def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    if s == '':
        return 0
    return 3 * ternaryToNum(s[0:-1]) + int(s[-1])
