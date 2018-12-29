'''
Created on Sep 28, 2017

@author: christinali
'''

def knapsack(capacity, itemList):
    '''returns the maximum value and the list of items'''
    if itemList == [] or capacity == 0:
        return[0,[]]
    if capacity < itemList[0][0]:
        return knapsack(capacity,itemList[1:])
    use = knapsack(capacity - itemList[0][0],itemList[1:])
    lose = knapsack(capacity, itemList[1:])
    new = use[0] + itemList[0][1]
    if new > lose[0]:
        return[new, [itemList[0]] + use[1]]
    return lose
