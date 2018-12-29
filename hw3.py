'''
Created on September 23, 2017
@author:   Christina Li
Pledge:    I pledge my honor that I have abided by the Stevens Honor System. cli50

CS115 - Hw 3
'''
# Be sure to submit hw3.py.  Remove the '_template' from the file name.
from cs115 import map
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 0
' Implement the function giveChange() here:
' See the PDF in Canvas for more details.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def giveChange(amount,coins):
    if amount == 0:
        return [0,[]]
    if coins == []:
        return[float('inf'),[]]
    if amount < coins[0]:
        return giveChange(amount, coins[1:])
    use = giveChange(amount - coins[0], coins)
    lose = giveChange(amount,coins[1:])
    new = coins[0] + use[0]
    if new < lose[0]:
        return [len([coins[0]] + use[1]),use[1] + [coins[0]]]
    return lose 

# Here's the list of letter values and a small dictionary to use.
# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 1
' Implement wordsWithScore() which is specified below.
' Hints: Use map. Feel free to use some of the functions you did for
' homework 2 (Scrabble Scoring). As always, include any helper
' functions in this file, so we can test it.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def wordsWithScore(dct, scores):
    '''List of words in dct, with their Scrabble score.

    Assume dct is a list of words and scores is a list of [letter,number]
    pairs. Return the dictionary annotated so each word is paired with its
    value. For example, wordsWithScore(Dictionary, scrabbleScores) should
    return [['a', 1], ['am', 4], ['at', 2] ...etc... ]
    '''
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
    return map(lambda word: [word,wordScore(word,scores)],dct)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 2
' For the sake of an exercise, we will implement a function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def take(n, L):
    '''Returns the list L[0:n].'''
    if L == []:
        return []
    if n == 0:
        return []
    else:
        return  [L[0]]+take(n-1,L[1:])

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 3
' Similar to problem 2, will implement another function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def drop(n, L):
    '''Returns the list L[n:].'''
    if L == []:
        return []
    if n == 0:
        return []
    else:
        return drop(n-1,L[1:])



