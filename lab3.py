'''
Created on Sep 21, 2017

@author: jwang151
pledge:I pledge my honor that I have abided by the Stevens Honor System. 
'''
def change(amount, coins):
    '''return minimum amount of coins that could be used to make up the amount.''' 
    if amount == 0:
        return 0
    if coins == []:
        return float("inf")
    if coins[0] > amount:
        return change(amount, coins[1:])
    use_it = 1 + change(amount - coins[0], coins)
    lose_it = change(amount, coins[1:])
    
    return min(use_it,lose_it)
