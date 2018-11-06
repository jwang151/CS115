'''
Created on Oct 30, 2017

@author: jwang151@stevens.edu
pledge: I pledge my honor that I have abided by the Stevens Honor System
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
def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    result = numToBinary(binaryToNum(s)+1) 
    if len(result) > 8: 
        return result[1:]
    elif len(result) == 8:
        return result 
    return (8 - len(result)) * "0" + result 

def TcToNum(s):
    '''It takes in a string of 8 bits representing an integer
in two's-complement, and returns the corresponding integer. '''
    if s[0] == "0":
        return binaryToNum(s)
    return binaryToNum(s[1:]) - 128
      
def NumToTc(N):
    ''' It takes in an integer N, and returns a string representing the two's-complement representation of that integer.'''
    if N > 127 or N < -128:
        return "Error"
    if N >= 0:
        result = numToBinary(N)
        if len(result) < 8:
            return (8 - len(result)) * "0" + result
        return result 
    result = numToBinary(N+128)
    if len(result) < 7: 
        return "1" + (7 - len(result)) * "0" + result
    return "1" + result
print(NumToTc(100))



