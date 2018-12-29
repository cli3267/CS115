'''
Created on September 17, 2017
@author:   Christina Li, Camille Simon-Al-Araji
Pledge:    I pledge my honor that I have abided by the Stevens Honor System -cli50, csimonal

CS115 - Hw 2
'''
import sys
from cs115 import *
# Be sure to submit hw2.py.  Remove the '_template' from the file name.

# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)

# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

# Implement your functions here.
def remove(letter, letters):
    """Removing letters that have been used already"""
    if letters == []:
        return []
    if letter == letters[0]:
        return letters[1:]
    else:
        return [letters[0]] + remove(letter, letters[1:])
    
def letterScore(letter,scoreList):
    """Returns the score of a certain letter"""
    if scoreList == []:
        return 0
    first = scoreList[0]  
    if first[0]  == letter:
        return first[1]
    return letterScore(letter,scoreList[1:])  

def wordScore(S, scoreList):
    """Returns the output of the scrabble score of that string"""
    if S == "":
        return 0
    return letterScore(S[0], scoreList) + wordScore(S[1:], scoreList)

def codeScore(code, scoreList):
    """Adds up all the letters of the word being created"""
    if code == "":
        return 0
    return letterScore(code[0], scoreList) + codeScore(code[1:], scoreList)

def codePossible(code,letter):
    """Knowing whether a word is possible to create or not, if so, it would use all or almost every letter once"""
    if code =='':
        return True
    if code[0] in letter:
        return codePossible(code[1:], remove(code[0],letter))
    else:
        return False

def codeCreate(dictionary,letter):
    """Listing possible words that can be created based on the letters that are given"""
    return filter(lambda code: codePossible(code, letter), dictionary)

def scoreList(Rack):
    """Takes the input a Rack(list of letters) and returns a list of all the words in the global Dictionary with the score of it"""
    C = codeCreate(Dictionary, Rack)
    return map(lambda code: [code, codeScore(code,scrabbleScores)], C)

    
def bestWord(Rack):
    """Takes a list of letters, and returns a list with two elements: highest possible scoring word and its score"""
    cont = scoreList(Rack)
    if cont == []:
        return ["",0]
    def better(x, y):
        if(x[1]>y[1]):
            return x
        return y
    return reduce(better, cont)



