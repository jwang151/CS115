'''
Created on Sep 28, 2017

@author: jwang151
Pledge: I pledge my honor that I have abided by the Stevens Honor System. 
'''
def knapsack(capacity, itemList):
    if capacity == 0:
        return [0,[]]
    if itemList== []:
        return [0,[]]
    if itemList[0][0] > capacity:
        return knapsack(capacity, itemList[1:])
    use_it = knapsack(capacity- itemList[0][0], itemList[1:])
    lose_it = knapsack(capacity, itemList[1:])
    use2 = [itemList[0][1] + use_it[0],[itemList[0]]+ use_it[1]]
    lose2 = [lose_it[0],lose_it[1]]
    if use2[0] > lose2[0]:
        return use2
    return lose2
print(knapsack(76, [[36, 35], [10, 28], [39, 47], [8, 1], [7, 24]]))
   '''The pascal_row function take a single integer as input, which represents the row number, and
 it returns that row of the pascal triangle.'''
 
 
   '''The pacal_triangle function takes in a single integer n and returns a list of lists containing the values of the all the rows up to and including row n. '''