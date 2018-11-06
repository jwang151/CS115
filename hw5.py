'''
Created on 10/10/17
@author:   jwang151@stevens.edu
Pledge:   I pledge my honor that I have abided by the Stevens Honor System. 

CS115 - Hw 5
'''
import turtle  # Needed for graphics
# Ignore 'Undefined variable from import' errors in Eclipse.

def sv_tree(trunkLength, letters):
    '''Using turtle drawing functions to draw a tree with a specific number of levels using two inputs; trunkLength and letters''' 
    def sv_helper(trunkLength, letters): 
        ''' The helper function makes it easier to read and call the draw function '''
        if letters == 0:
            return       
        turtle.forward(trunkLength)       
        turtle.left(45)          
        sv_helper(trunkLength * 0.5,letters - 1)      
        turtle.right(90)        
        sv_helper(trunkLength * 0.5, letters - 1)     
        turtle.left(45)          
        turtle.backward(trunkLength)
    sv_helper(trunkLength, letters) 
    turtle.done()                    

def fast_lucas(n):
    '''Returns the nth Lucas number using the memoization technique
    shown in class and lab. The Lucas numbers are as follows:
    [2, 1, 3, 4, 7, 11, ...]'''
    def lucas_helper(n, memo):
        '''returns the numbers in order using memo'''
        if n in memo: 
            return memo[n]
        if n == 0:
            result = 2
        elif n == 1:
            result = n
        else: 
            result = lucas_helper(n-1, memo) + lucas_helper(n-2, memo)
        memo[n] = result
        return result
    return lucas_helper(n, {})

def fast_change(amount, coins):
    '''Takes an amount and a list of coin denominations as input.
    Returns the number of coins required to total the given amount.
    Use memoization to improve performance.'''
    
    def fast_change_helper(amount, coins, memo):
        '''return minimum amount of coins that could be used to make up the amount.'''
        if (amount, coins) in memo:
            return memo[(amount, coins)]  
        elif amount == 0:
            result = 0
        elif coins == ():
            result = float("inf")
        elif coins[0] > amount:
            result = fast_change_helper(amount, coins[1:], memo)
        else:
            use_it = 1 + fast_change_helper(amount - coins[0], coins, memo)
            lose_it = fast_change_helper(amount, coins[1:], memo)
            result = min(use_it,lose_it)
        memo[(amount, coins)] = result
        return result 
    # Call the helper. Note we converted the list to a tuple.
    return fast_change_helper(amount, tuple(coins), {})

# If you did this correctly, the results should be nearly instantaneous.
print(fast_lucas(3))  # 4
print(fast_lucas(5))  # 11
print(fast_lucas(9))  # 76
print(fast_lucas(24))  # 103682
print(fast_lucas(40))  # 228826127
print(fast_lucas(50))  # 28143753123

print(fast_change(131, [1, 5, 10, 20, 50, 100]))
print(fast_change(292, [1, 5, 10, 20, 50, 100]))
print(fast_change(673, [1, 5, 10, 20, 50, 100]))
print(fast_change(724, [1, 5, 10, 20, 50, 100]))
print(fast_change(888, [1, 5, 10, 20, 50, 100]))

# Should take a few seconds to draw a tree.
sv_tree(100, 4)
