'''
Created on Oct 2, 2017

@author:   jwang151@stevens.edu 
Pledge:    I pledge my honor that I have abided by the Stevens Honor System
'''
def helper(l):
    if l == [] or l[1:] == []:
        return []
    return [l[0]+l[1]] + helper(l[1:])

def pascal_row(n):
    '''The pascal row function takes a single integer, which represents a row number and it returns that row. '''
    if n == 0:
        return [1]
    return [1] + helper(pascal_row(n-1)) + [1]

def pascal_triangle(n):
    '''The pascal triangle function takes in a single integer and returns a list 
containing the values of all the rows up to and including row n'''
    if n == 0:
        return [[1]]
    return pascal_triangle(n-1) + [pascal_row(n)] 
    