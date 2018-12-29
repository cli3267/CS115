'''
Created on November 22, 2017
@author:   Christina Li
Pledge:    "I pledge my honor that I have abided by the Stevens Honor System." -cli50

CS115 - Hw 11 - Date class
'''
DAYS_IN_MONTH = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

class Date(object):
    '''A user-defined data structure that stores and manipulates dates.'''

    # The constructor is always named __init__.
    def __init__(self, month, day, year):
        '''The constructor for objects of type Date.'''
        self.month = month
        self.day = day
        self.year = year

    # The 'printing' function is always named __str__.
    def __str__(self):
        '''This method returns a string representation for the
           object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.'''
        return '%02d/%02d/%04d' % (self.month, self.day, self.year)

    # Here is an example of a 'method' of the Date class.
    def isLeapYear(self):
        '''Returns True if the calling object is in a leap year; False
        otherwise.'''
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False
    
    def copy(self):
        '''Returns a new object with the same month, day, year
           as the calling object (self).'''
        dnew = Date(self.month, self.day, self.year)
        return dnew
    
    def equals(self, d2):
        '''Decides if self and d2 represent the same calendar date,
        whether or not they are the in the same place in memory.''' 
        return self.year == d2. year and self.month == d2.month and self.day == d2.day
    
    def tomorrow(self):
        """Changes the calling object so that it represents on day after the date it was originally represented."""
        if self.month ==  12 and self.day == DAYS_IN_MONTH[self.month]:
            self.month = 1
            self.day = 1
            self.year += 1
        elif self.month == 2 and self.day == DAYS_IN_MONTH[self.month] and self.isLeapYear() == False:
            self.month += 1
            self.day = 1
        elif self.month == 2 and self.day == DAYS_IN_MONTH[self.month] and self.isLeapYear() == True:
            self.day += 1
        elif self.month == 2 and self.day == 29:
            self.month += 1
            self.day = 1
        elif self.day == DAYS_IN_MONTH[self.month]:
            self.month += 1
            self.day = 1
        else:
            self.day += 1

    def yesterday(self):
        """Changes the calling object so that it represents on day before the date it was originally represented."""
        if self.month == 1 and self.day == 1:
            self.month = 12
            self.day = 31
            self.year -= 1
        elif self.month == 3 and self.day == 1 and self.isLeapYear() == True:
            self.month = 2
            self.day = 29
        elif self.day == 1:
            self.month -=1
            self.day = DAYS_IN_MONTH[self.month]
        else:
            self.day -= 1
    
    def addNDays(self, N):
        """Changes the calling object so that it represents N days after the date it was originally represented."""
        print(self)
        for x in range(N):
            self.tomorrow()
            print(self)  
    
    def subNDays(self, N):
        """Changes the calling object so that it represents N days before the date it was originally represented."""
        print(self)
        for x in range(N):
            self.yesterday()
            print(self)
    
    def isBefore(self, d2):
        """Returns True if the calling object is a date before d2. Returns False if the calling object is a date after d2."""
        if self.year < d2.year:
            return True
        elif self.year == d2.year and self.month < d2.month:
            return True
        elif self.year == d2.year and self.month == d2.month and self.day < d2.day:
            return True
        else:
            return False
    
    def isAfter(self, d2):
        """Returns True if the calling object is a date after d2. Returns False if the calling object is a date before d2."""
        if self.year > d2.year:
            return True
        elif self.year == d2.year and self.month > d2.month:
            return True
        elif self.year == d2.year and self.month == d2.month and self.day > d2.day:
            return True
        else:
            return False

    def diff(self,d2): 
        """Returns the number of days between the calling object and d2 date."""
        count = 0
        s = self.copy()
        d = d2.copy()
        while s.isAfter(d):
            s.yesterday()
            count += 1
        while s.isBefore(d):
            s.tomorrow()
            count -= 1
        return count  

    def dow(self):
        """Returns a string that indicates the day of the week of the date that is being called."""
        d = self.diff(Date(11,9,2011))
        if d % 7 == 0:
            return 'Wednesday'
        if d % 7 == 1:
            return 'Thursday'
        if d % 7 == 2:
            return 'Friday'
        if d % 7 == 3:
            return 'Saturday'
        if d % 7 == 4:
            return 'Sunday'
        if d % 7 == 5:
            return 'Monday'
        else:
            return 'Tuesday'


  
        