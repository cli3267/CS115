'''
Created on Sep 21, 2017

@author: christinali
'''
def change(amount,coins):
    if amount == 0:
        return 0
    elif coins == []:
        return float('inf')
    else:
        if coins[0] > amount:
            return change(amount,coins[1:])
        else:
            use = 1 + change(amount - coins[0], coins)
            lose = change(amount, coins[1:])
        return min(use,lose)        

