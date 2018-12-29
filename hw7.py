'''
Created on Oct 22, 2017
@author:   Christina Li
Pledge:    I pledge my honor that I have abided by the Stevens Honor System. -cli50
'''
# Each row has (x,y,carry-in) : (sum,carry-out)
FullAdder = \
{ ('0','0','0') : ('0','0'),
('0','0','1') : ('1','0'),
('0','1','0') : ('1','0'),
('0','1','1') : ('0','1'),
('1','0','0') : ('1','0'),
('1','0','1') : ('0','1'),
('1','1','0') : ('0','1'),
('1','1','1') : ('1','1') }

def numToBaseB(N, B):
    """Takes in a non-negative number (N) and a base (B) and returns the string representing N in B"""
    if N == 0:
        return ''
    return numToBaseB(N//B,B) + str(N%B)

def baseBToNum(S, B):
    """Takes in a string(S) and a base(B) and returns an integer in base 10 representing the same number as S """
    if S == "":
        return 0
    return B * baseBToNum(S[0:-1],B) + int(S[-1])

def baseToBase(B1,B2,SinB1):
    """Takes in two bases (B1 and B2) and a string representation of B1 (sinB1) and returns the string representation of B2"""
    if B1 == "" or B2 == "":
        return ""
    return numToBaseB(baseBToNum(SinB1,B1),B2)

def add(S,T):
    """Takes in two binary strings(S and T) and returns their sum"""
    return str(numToBaseB(baseBToNum(S,2) + baseBToNum(T,2), 2))

def addB(S,T):
    """Takes in two binary string(S,T) and returns the sum without conversions"""
    def helper(S,T,carry):
        if S == '' and T == '' and carry == '0':
            return ''
        if S == '' and T == '' and carry == '1':
            return '1'
        elif S == '':
            sum = FullAdder[('0',T[-1],carry)]
        elif T == '':
            sum = FullAdder[(S[-1],'0',carry)]
        else:
            sum = FullAdder[(S[-1],T[-1],carry)]
        return helper(S[:-1],T[:-1],sum[1]) + sum[0]
    return helper(S,T,'0')

print(addB("11", "1"))