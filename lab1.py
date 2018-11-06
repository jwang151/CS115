'''
Created on Sep 7, 2017

@author: wangj
I pledge my honor that I have abided by the Stevens Honor System. 
'''
from cs115 import range, map, reduce
import math 
def inverse(n):
    return 1/n 


def add(a,b):
    return a+b
    
def e(n): 
    return reduce(add, map(inverse,map(math.factorial ,range(n+1))))

def error(n):
    return abs(math.e-e(n))

    