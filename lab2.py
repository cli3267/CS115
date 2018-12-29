'''
Created on Sep 14, 2017

@author: christinali
'''

def dot(L,K):
    if L == [] or K == []:
        return 0
    return L[0]*K[0] + dot(L[1:],K[1:])

 
def explode(S):
    return list(S)
    if S == "":
        return []


def ind(e,L):
    if e in L:
        return L.index(e)
    if e not in L:
        def length(L):
            if L == [] or L == "":
                return 0
            else:
                return 1 + length(L[1:])
        return length(L[0:])


def removeAll(e,L):
    if e in L:
        L.remove(e)
        if e in L:
            L.remove(e)
    return list(L)

def even(x):
        if x % 2 == 0 :
            return True
        return False
    
def myFilter(f, L):
    if not L:
        return []
    elif f(L[0]):
        return [(L[0])] + myFilter(f, L[1:]) 
    else:
        return myFilter(f,L[1:])

def deepReverse(L):
    if L == []:
        return L
    if not isinstance(L[0], list):
        return deepReverse(L[1:])+[L[0]]
    else:
        return deepReverse(L[1:])+[deepReverse(L[0])]


    

    