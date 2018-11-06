'''
Created on Sep 13, 2017
Pledge: I pledge my honor that I have abided by the Stevens Honor System
@author: wangj
'''
from cs115 import map, reduce

def mult(x, y):
    """Returns the product of x and y"""
    return x*y
def factorial(n):
    if n== 0:
        return 1
    else:
        return n*factorial(n-1)

def add(x,y):
    return x+y
def mean(L):
    """takes in a list and returns the average of the numbers"""
    return reduce(add,L)/len(L)
def divides(n):
    def div(k):
        return n % k == 0
    return div
def prime(n):
    """if it is a prime number it returns true, otherwise it returns false"""
    if(reduce(add,(map(divides(n),range(1,n+1))))>2) or (n==1):
        return False
    return True








