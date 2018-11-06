'''
Created on Oct 23, 2017

@author: jwang151@stevens.edu
pledge: I pledge my honor that I have abided by the Stevens Honor System
'''
FullAdder = { ('0','0','0') : ('0','0'),
('0','0','1') : ('1','0'),
('0','1','0') : ('1','0'),
('0','1','1') : ('0','1'),
('1','0','0') : ('1','0'),
('1','0','1') : ('0','1'),
('1','1','0') : ('0','1'),
('1','1','1') : ('1','1') }
def numToBaseB(N,B):
    ''' It takes in a non-negative integer N and a base B and 
    returns the string representing N in base B. Returns binary.'''
    if N == 0:
        return ""
    elif N == 1:
        return str(N)
    return numToBaseB(N//B,B) + str(N%B)
print(numToBaseB(5, 3))
def baseBToNum(S,B):
    ''' Takes in the input string S and a base B and
will return an integer representing S in base B.  '''
    def baseToNumhelp(S,B,N):
        if S == "":
            return 0
        return int(S[-1]) * B ** N + baseToNumhelp(S[:-1], B, N+1)
    return baseToNumhelp(S,B,0)
print(baseBToNum("40", 5))
def baseToBase(B1,B2,SinB1):
    '''Takes three inputs;it takes in the base of B1 and
returns its representation in B2 '''
    return numToBaseB(baseBToNum(SinB1, B1), B2)
print(baseToBase(10, 2, "3"))
def add(S,T):
    '''Find the sum of two numbers in binary and returns it in binary'''
    return numToBaseB(baseBToNum(S,2) + baseBToNum(T,2),2)
print(add("11", "01"))
def addB(S,T):
    ''' It takes in two strings as input and
    return a new string representing the sum of the two input strings.'''
    def addBhelp(S,T,carry):
        if S == "" and T == "": 
            if carry == "0":
                return ""
            return "1"
        if S == "":
            sum, carry2 = FullAdder[("0",T[-1], carry)]
        elif T == "":
            sum, carry2 = FullAdder[(S[-1], "0", carry)]
        else: 
            sum, carry2 = FullAdder[S[-1], T[-1], (carry)]
        return addBhelp(S[:-1],T[:-1],carry2) + sum 
    return addBhelp(S,T,"0")
print(addB("11", "1"))






