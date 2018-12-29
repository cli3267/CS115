'''
Created on Sep 6, 2017

@author: christinali
'''
from cs115 import map, reduce
def inverse(n):
    return 1 / n

import math
def e(n):
    return sum(map(inverse,map(math.factorial, range(0,n+1))))


def sub(a,b):
    return a - b

def error(n):
    return abs(sub(math.e,e(n)))


   
    