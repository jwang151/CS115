'''
Created on 10/16/17
@author:   jwang151@stevens.edu and cli50@stevens.edu
Pledge:    I pledge my honor that I have abided by the Stevens Honor System. 
-Jing Wang and Christina Li 
CS115 - Hw 6
'''

# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1
 
def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    return n % 2 == 1
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
    if s == "":
        return 0
    elif int(s[-1]) == 1:
        return 1 + 2*binaryToNum(s[:-1])
    else: 
        return 2 * binaryToNum(s[:-1])
def countRun(s, c, MAXLENGTH):
    '''param s: a string
    param c: what we're counting 
    param maxRun: maximum length of run 
    returns the number of times that string occurs in a row.'''
    var = MAXLENGTH + 1
    if s == "":
        return 0
    if s[0] == c:
        return 1 + countRun(s[1:var - 1],c, MAXLENGTH)
    return 0 
#print(countRun("00000", '0', MAX_RUN_LENGTH))
#print(countRun('0' * 64, '0', MAX_RUN_LENGTH)) #31
#print(countRun('0' * 16 + '1' * 16 + '0' * 16, '0', MAX_RUN_LENGTH)) #16
#print(countRun('0' * 16 + '1' * 16 + '0' * 16, '1', MAX_RUN_LENGTH)) #0


def compress(s):
    '''return compressed string
    param s: string to compress
    count the runs in s switching from counting runs of zeros to counting runs of 1s
    return compressed string
    '''
    def compress_help(s,c):
        if s == "":
            return ""
        runLen = countRun(s, c, MAX_RUN_LENGTH)
        runlenbinary = numToBinary(runLen)
        zeroes = '0'*(COMPRESSED_BLOCK_SIZE - len(runlenbinary))
        nextC = '0'
        if c == '0':
            nextC= '1'
        return zeroes + runlenbinary + compress_help(s[runLen:], nextC)
    return compress_help(s, '0')
def uncompress(s):
    '''return uncompressed string
    take five digits at a time, need a helper
    convert it to number and then it adds it together
    five characters from the string and convert it to a certain number of zero and ones,
     use the binary to ones function, do not even need to modify.
     we take COMPRESSED_BLOCK_SIZE, many characters at a time
     then these characters from the  binary representation of a number into that many
     zeros or ones
     we do this switching from outputting zeros to outputting ones alternatively
     return uncompressed string 
    '''
    def uncompressed_help(s, c):
        if s == "":
            return ""
        nextC = '0'
        first5 = s[:COMPRESSED_BLOCK_SIZE]
        num = binaryToNum(first5)
        if c == '0':
            nextC= '1'
        return c * num + uncompressed_help(s[COMPRESSED_BLOCK_SIZE:], nextC) 
    return uncompressed_help(s,'0')      

def compression(s):
    '''return divide compressed size by original size(length)  '''
    return len(compress(s))/(len(s))
'''1.The largest number of bits used to possibly encode a 64 bit string is 320
because it is the compressed block size times 64 bits.  
'''
print(compression("00011000"+"00111100"*3 +
"01111110"+"11111111"+"00111100"+"00100100")) #penguin
print(compression("0"*8 + "01100110"*2 + "0"*8 + "00001000" + "01000010" + "01111110" + "0"*8)) #smile
print(compression("1"*9 + "0"*7 + "10000000"*2 + "1"*7 + "0" + "00000001"*2 + "1"*7 + "0")) #five
print(compression("0"*11 + "11" + "1"*3 + "0011000"*2 + "01110010"*2 + "0011000"*2)) #triangle 
print(compression("1" + "0"*6 + "11" + "0"*6 + "111" + "1"*4 + "1"*4 + "010" + "1"*5 + "00" + "1"*6 + "0" + "1"*12))#toys
print(compression("00000011000111011010010110100101101111011000000111111111")) #square
'''2.The five tested image were the given samples penguins, smiles,five, and I tested three more which are toy,triangle, and square. 
The compression of those are 1.484375,1.328125,1.015625,1.5833333333333333,
1.2727272727272727, 2.142857142857143
3.This algorithm would not work. First with smaller values it would not work because 
because the algorithm would be unable to encode the smaller bits such as "0"*64.
This algorithm would also not work with larger values because in the algorithm
when "1" or "0" appears it would have to computate the binary of "1" and it would just make the encoding way too long. 
 '''


print(compress("0"* 64))


 




