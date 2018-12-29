'''
Created on Nov 19, 2017

@author: Christina Li
'''
import math 
import sys
class QuadraticEquation(object):
    
    def __init__(self, a=0, b=0, c=0):
        if a == 0:
            raise ValueError("Coefficient 'a' cannot be 0 in a quadratic equation.")
            sys.exit()
        else:
            self.__a = float(a)
            self.__b = float(b)
            self.__c = float(c)
    
    @property
    def a(self):
        return self.__a
    
    @property
    def b(self):
        return self.__b
    
    @property
    def c(self):
        return self.__c
    
    def discriminant(self):
        return (self.b*self.b) - (4*self.a*self.c)
    
    def root1(self):
        if self.discriminant() < 0:
            return None
        return (-1*self.b + math.sqrt(self.discriminant()))/(2*self.a)
    def root2(self):
        if self.discriminant() < 0:
            return None
        return (-1*self.b - math.sqrt(self.discriminant()))/(2*self.a)
    
    def __str__(self):
        if (self.a) == 1:
            if (self.b) == 1:
                if (self.c) == 0:
                    return 'x^2 + x = 0'
                elif self.c < 0:
                    return 'x^2 + x - ' + str(abs(self.c)) + ' = 0' 
                else:
                    return 'x^2 + x + ' + str(abs(self.c)) + ' = 0' 
            elif (self.b) == -1:
                if (self.c) == 0:
                    return 'x^2 - x = 0'
                elif self.c < 0:
                    return 'x^2 - x - ' + str(abs(self.c)) + ' = 0' 
                else:
                    return 'x^2 - x + ' + str(abs(self.c)) + ' = 0'
            elif (self.b) == 0:
                if (self.c) == 0:
                    return 'x^2 = 0'
                elif self.c < 0:
                    return 'x^2 - ' + str(abs(self.c)) + ' = 0' 
                else:
                    return 'x^2 + ' + str(abs(self.c)) + ' = 0'
            elif (self.b) > 0:
                if (self.c) == 0:
                    return 'x^2 + ' + str(self.b) + 'x = 0'
                elif self.c < 0:
                    return 'x^2 + ' + str(self.b) +'x - ' + str(abs(self.c)) + ' = 0' 
                else:
                    return 'x^2 + ' + str(self.b) + 'x + ' + str(abs(self.c)) + ' = 0'
            else:
                if (self.c) == 0:
                    return 'x^2 - ' + str(abs(self.b)) + 'x = 0'
                elif self.c < 0:
                    return 'x^2 - ' + str(abs(self.b)) +'x - ' + str(abs(self.c)) + ' = 0' 
                else:
                    return 'x^2 - ' + str(abs(self.b)) + 'x + ' + str(abs(self.c)) + ' = 0'
        elif (self.a) == -1:
            if (self.b) == 1:
                if (self.c) == 0:
                    return '-x^2 + x = 0'
                elif self.c < 0:
                    return '-x^2 + x - ' + str(abs(self.c)) + ' = 0' 
                else:
                    return '-x^2 + x + ' + str(abs(self.c)) + ' = 0' 
            elif (self.b) == -1:
                if (self.c) == 0:
                    return '-x^2 - x = 0'
                elif self.c < 0:
                    return '-x^2 - x - ' + str(abs(self.c)) + ' = 0' 
                else:
                    return '-x^2 - x + ' + str(abs(self.c)) + ' = 0'
            elif (self.b) == 0:
                if (self.c) == 0:
                    return '-x^2 = 0'
                elif self.c < 0:
                    return '-x^2 - ' + str(abs(self.c)) + ' = 0' 
                else:
                    return '-x^2 + ' + str(abs(self.c)) + ' = 0'
            elif (self.b) > 0:
                if (self.c) == 0:
                    return '-x^2 + ' + str(self.b) + 'x = 0'
                elif self.c < 0:
                    return '-x^2 + ' + str(self.b) +'x - ' + str(abs(self.c)) + ' = 0' 
                else:
                    return '-x^2 + ' + str(self.b) + 'x + ' + str(abs(self.c)) + ' = 0'
            else:
                if (self.c) == 0:
                    return '-x^2 - ' + str(abs(self.b)) + 'x = 0'
                elif self.c < 0:
                    return '-x^2 - ' + str(abs(self.b)) +'x - ' + str(abs(self.c)) + ' = 0' 
                else:
                    return '-x^2 - ' + str(abs(self.b)) + 'x + ' + str(abs(self.c)) + ' = 0'
        elif (self.a) > 0:
            if (self.b) == 1:
                if (self.c) == 0:
                    return str(self.a) + 'x^2 + x = 0'
                elif self.c < 0:
                    return str(self.a) + 'x^2 + x - ' + str(abs(self.c)) + ' = 0' 
                else:
                    return str(self.a) + 'x^2 + x + ' + str(abs(self.c)) + ' = 0' 
            elif (self.b) == -1:
                if (self.c) == 0:
                    return str(self.a) + 'x^2 - x = 0'
                elif self.c < 0:
                    return str(self.a) + 'x^2 - x - ' + str(abs(self.c)) + ' = 0' 
                else:
                    return str(self.a) + 'x^2 - x + ' + str(abs(self.c)) + ' = 0'
            elif (self.b) == 0:
                if (self.c) == 0:
                    return str(self.a) + 'x^2 = 0'
                elif self.c < 0:
                    return str(self.a) + 'x^2 - ' + str(abs(self.c)) + ' = 0' 
                else:
                    return str(self.a) + 'x^2 + ' + str(abs(self.c)) + ' = 0'
            elif (self.b) > 0:
                if (self.c) == 0:
                    return str(self.a) + 'x^2 + ' + str(self.b) + 'x = 0'
                elif self.__c < 0:
                    return str(self.a) + 'x^2 + ' + str(self.b) +'x - ' + str(abs(self.c)) + ' = 0' 
                else:
                    return str(self.a) + 'x^2 + ' + str(self.b) + 'x + ' + str(abs(self.c)) + ' = 0'
            else:
                if (self.__c) == 0:
                    return str(self.a) + 'x^2 - ' + str(abs(self.b)) + 'x = 0'
                elif self.__c < 0:
                    return str(self.a) + 'x^2 - ' + str(abs(self.b)) +'x - ' + str(abs(self.c)) + ' = 0' 
                else:
                    return str(self.a) + 'x^2 - ' + str(abs(self.b)) + 'x + ' + str(abs(self.c)) + ' = 0'
        else:
            if (self.b) == 1:
                if (self.c) == 0:
                    return str(self.a) + 'x^2 + x = 0'
                elif self.c < 0:
                    return str(self.a) + 'x^2 + x - ' + str(abs(self.c)) + ' = 0' 
                else:
                    return str(self.a) + 'x^2 + x + ' + str(abs(self.c)) + ' = 0' 
            elif (self.b) == -1:
                if (self.c) == 0:
                    return str(self.a) + 'x^2 - x = 0'
                elif self.c < 0:
                    return str(self.a) + 'x^2 - x - ' + str(abs(self.c)) + ' = 0' 
                else:
                    return str(self.a) + 'x^2 - x + ' + str(abs(self.c)) + ' = 0'
            elif (self.b) == 0:
                if (self.c) == 0:
                    return str(self.a) + 'x^2 = 0'
                elif self.c < 0:
                    return str(self.a) + 'x^2 - ' + str(abs(self.c)) + ' = 0' 
                else:
                    return str(self.a) + 'x^2 + ' + str(abs(self.c)) + ' = 0'
            elif (self.b) > 0:
                if (self.c) == 0:
                    return str(self.a) + 'x^2 + ' + str(self.b) + 'x = 0'
                elif self.c < 0:
                    return str(self.a) + 'x^2 + ' + str(self.b) +'x - ' + str(abs(self.c)) + ' = 0' 
                else:
                    return str(self.a) + 'x^2 + ' + str(self.b) + 'x + ' + str(abs(self.c)) + ' = 0'
            else:
                if (self.c) == 0:
                    return str(self.a) + 'x^2 - ' + str(abs(self.b)) + 'x = 0'
                elif self.c < 0:
                    return str(self.a) + 'x^2 - ' + str(abs(self.b)) +'x - ' + str(abs(self.c)) + ' = 0' 
                else:
                    return str(self.a) + 'x^2 - ' + str(abs(self.b)) + 'x + ' + str(abs(self.c)) + ' = 0'
        
if __name__ == '__main__':
    pass