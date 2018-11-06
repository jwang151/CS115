'''
Created on 10/1217
@author:   jwang@151@stevens.edu
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Lab 6
'''
def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    return n % 2 == 1
#42 =101010
#It would be one because the right most number is 1 and the second number is 2. 
#It would be zero because it would be a multiple of 2 and the most right number is 1.
#if you delete the least significant bit of the original number, it is changing by floor division of 2 
def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n == 0:
        return ""
    elif isOdd(n):
        return numToBinary(n//2)+ "1"
    else:
        return numToBinary(n/2) + "0"
print(numToBinary(10))
def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    pass  # TODO
    if s == "":
        return 0
    elif int(s[-1]) == 1:
        return 1 + 2*binaryToNum(s[:-1])
    else: 
        return 2 * binaryToNum(s[:-1])
print(binaryToNum("1010"))
    

def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    result = numToBinary(binaryToNum(s)+1) 
    if len(result) > 8: 
        return result[1:]
    elif len(result) == 8:
        return result 
    return (8 - len(result)) * "0" + result 
print(increment("11100111"))

def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    if n == 0:
        print(s) 
    else:
        print(s)
        return count(increment(s), n-1)
count("00000000",4)

def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    if n == 0:
        return ""
    elif n%3 == 1: 
        return numToTernary(n//3) + "1"
    elif n%3 == 2:
        return numToTernary(n//3) + "2"
    else:
        return numToTernary(n//3) + "0"
    
def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    if s == "":
        return 0
    elif int(s[-1]) == 1:
        return 1 + 3*ternaryToNum(s[:-1])
    elif int(s[-1]) == 2:
        return 2 + 3 * ternaryToNum(s[:-1])
    else: 
        return 3 * ternaryToNum(s[:-1])
        
    
    




