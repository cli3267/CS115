'''
Created on Sep 10, 2017

@author: christinali
'''
from cs115 import map, reduce
'''
I pledge my honor that I have abided by the Stevens Honor System.
cli50 
'''

def mult(x,y):
    return x * y

def factorial(n):
    """
    Taking the factorial of a number, n
    """
    return reduce(mult,range(1,n+1))

def add(x,y):
    return x + y

'''
Try to fix this one
'''
L = [5,6,39,8]
def mean(L):
    """
    Adding up all the numbers on the list, then dividing it by the number of numbers
    on the list. Giving us the average of the list
    """
    return reduce(add,L)/len(L)

def divides(n):
    def div(k):
        return n % k == 0 
    return div


def prime(n):
    """
    Determines if the number is prime or a composite. False if the number is a composite number 
    and True if the number is a prime number. 
    """
    if sum((map(divides(n),range(2,n-1)))) == 0:
        return True
    return False
    
    
    