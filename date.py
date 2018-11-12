'''
Created on 11/27/17
@author:   jing wang 
Pledge:   I pledge my honor that I have abided by the Stevens Honor System. 

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
        '''This function returns True if the calling object is in a leap year; False
        otherwise.'''
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False
    def copy(self):
        '''This function returns a new object with the same month, day, year
        as the calling object (self).'''
        dnew = Date(self.month, self.day, self.year)
        return dnew
    
    def equals(self, d2):
        '''This function decides if self and d2 represent the same calendar date,
        whether or not they are the in the same place in memory.'''
        return self.year == d2.year and self.month == d2.month and \
            self.day == d2.day
            
    def tomorrow(self):
        ''' This function changes the calling object so that it represents one calendar day after
         the date it originally represented. '''
        DIM = (0,31,28,31,30,31,30,31,31,30,31,30,31)
        if self.month == 12 and self.day == DAYS_IN_MONTH[self.month]:
            self.year += 1
            self.month = 1
            self.day = 1
        elif self.month == 2 and self.day == 28 and self.isLeapYear():
            self.day += 1
        elif self.day >= DAYS_IN_MONTH[self.month]:
            self.month += 1
            self.day = 1
        else:
            self.day += 1
        
    def yesterday(self):
        '''This function Changes the calling object so that it represents one calendar day before
        the date it originally represented'''
        if self.month == 1 and self.day == 1:
            self.year -= 1
            self.month = 12
            self.day = DAYS_IN_MONTH[self.month]
        elif self.month == 3 and self.day == 1 and self.isLeapYear():
            self.month -= 1
            self.day = 29
        elif self.day == 1:
            self.month -= 1
            self.day = DAYS_IN_MONTH[self.month]
        else:
            self.day -= 1
    
    def addNDays(self, N):
        '''This function changes the calling object so that it represents N calendar days after 
        the date it originally represented'''
        print(self)
        while N != 0:
            self.tomorrow()
            print(self)
            N -= 1
    def subNDays(self, N):
        '''This function changes the calling object so that it represents N calendar days before
        the date it originally represented'''
        print(self)
        while N != 0:
            self.yesterday()
            print(self)
            N -= 1
    def isBefore(self, d2):
        '''This function returns True if the calling object is a calendar date before the input d2.
        and it returns False if they are the same date or if self is after d2.'''
        if self.year < d2.year:
            return True
        if self.year == d2.year and self.month < d2.month:
            return True
        if self.year == d2.year and self.month == d2.month and self.day < d2.day:
            return True
        return False
    
    def isAfter(self, d2):
        '''This function returns True if the calling object is a calendar date after the input d2.
            Returns False if they are the same date or if self is before d2.'''
        if self.isBefore(d2):
            return False
        if self.equals(d2):
            return False
        return True
    
    def diff(self, d2):
        '''This function returns an integer representing the number of days between self and d2'''
        first = self.copy()
        second = d2.copy()
        cnt = 0
        while first.isAfter(second):
            first.yesterday()
            cnt += 1
        while first.isBefore(second):
            first.tomorrow()
            cnt -= 1
        return cnt

    def dow(self):
        '''This function returns a string that indicates the day of the week of the object'''
        days = ["Wednesday","Thursday","Friday","Saturday","Sunday","Monday", "Tuesday"]
        return days[self.diff(Date(11,9,2011)) % 7]
d = Date(12, 7, 1941)
print(d.dow())