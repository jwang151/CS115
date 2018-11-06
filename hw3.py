'''
Created on 9/25/17
@author:   jwang151@stevens.edu 
Pledge:    I pledge my honor that I have abided by the Stevens Honor System. 

CS115 - Hw 3
'''
# Be sure to submit hw3.py.  Remove the '_template' from the file name.

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 0
' Implement the function giveChange() here:
' See the PDF in Canvas for more details.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
from cs115 import map,reduce,filter
# your code goes here
def giveChange(numberOfCoins,listOfCoins):
    ''' The function takes the same kind of input as change but returns a list whose first item is the minimum number of coins 
and whose second item is a list of the coins in that optimal solution. '''
    if numberOfCoins == 0:
        return [0,[]]
    if listOfCoins == []:
        return [float("inf"),[]]
    if listOfCoins[0] > numberOfCoins:
        return giveChange(numberOfCoins, listOfCoins[1:])
    use_it = giveChange(numberOfCoins- listOfCoins[0], listOfCoins)
    lose_it = giveChange(numberOfCoins, listOfCoins[1:])
    use2 = [1 + use_it[0],use_it[1] + [listOfCoins[0]]]
    lose2 = [lose_it[0],lose_it[1]]
    if use2[0] < lose2[0]:
        return use2
    return lose2
print(giveChange(35, [1, 3, 16, 30, 50]))


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
    def letterScore(letter, scoreList):
        """Returns the score for a single letter by looking it up in the provided scoreList"""
        if scoreList==[]:
            return 0
        first = scoreList[0]
        if first[0] == letter: 
            return first[1]
        return letterScore(letter, scoreList[1:])

    def wordScore(S):
        """Returns the score for the word by taking the score for each letter and adding them up"""
        if S == '':
            return ['',0]
        return [S , letterScore(S[0], scores)+ wordScore(S[1:])[1]]
    return map(wordScore,dct)
print(wordsWithScore(Dictionary,scrabbleScores))
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 2
' For the sake of an exercise, we will implement a function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
n =3
L = [1,2,3,4,6,7,8]
def take(n, L):
    '''Returns the list L[0:n].'''
    if L == [] or n == 0:
        return []
    return [L[0]]+ take(n-1,L[1:])
print(L[0:n])
print(take(n,L))

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 3
' Similar to problem 2, will implement another function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def drop(n, L):
    '''Returns the list L[n:].'''
    # your code goes here
    if n == 0:
        return L
    return drop(n-1,L[1:])
print(L[n:])
print(drop(n,L))

