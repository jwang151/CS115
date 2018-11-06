'''
Created on Sep 14, 2017
Pledge: I pledge my honor that I have abided by the Stevens Honor System 
@author: wangj
'''
def mult(x,y):
    return x*y 
def dot(L,K):
    if L == [] or K==[]:
        return 0
    return L[0]*K[0] + dot(L[1:],K[1:])   

def explode(S):
    if S == '':
        return []
    return [S[0]] + explode(S[1:])

def ind(e,L):
    if L[0] == e:
        return 0
    return ind(e,L[1:]) + 1

def removeAll(e,L):
    if L == []:
        return []
    if e == L[0]:
        return removeAll(e,L[1:])
    return [L[0]] +removeAll(e,L[1:])

def myfilter(f,L):
    if L == []:
        return []
    if f(L[0]):
        return [L[0]]+myfilter(L[1:])
    return myfilter(L[1:])

def deepReverse(L):
    if L==[]:
        return []
    if isinstance(L[0],list):
        return deepReverse(L[0])+ deepReverse(L[1:])
    return deepReverse(L[1:])+L[0]
    

    

    
    
    
