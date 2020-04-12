# -*- coding: utf-8 -*-
"""
hms.py

Copyright (c) 2020 @RR_Inyo
Released under the MIT license.
https://opensource.org/licenses/mit-license.php
"""

# Definition of the hms class
class hms:
    def __init__(self, t, second = False):
        # When given a single float or integer value as seconds:  
        if (type(t) == float or type(t) == int) and second:
            self.sec = t
        # When given a single float or integer value as hours, convert to seconds:
        elif (type(t) == float or type(t) == int) and not second:
            self.sec = t * 3600
        # When given a sexagesimal list, [hour, minute, second], convert to seconds
        elif type(t) == list and len(t) == 3:
            # Checking the type and value of the hour, minute, and second elements
            ## Hour
            if type(t[0]) == float or type(t[0]) == int and t[0] >= 0:
                self.sec = t[0] * 3600
            else:
                raise ValueError('Invalid value for the hour element.')
            ## Minute
            if (type(t[1]) == float or type(t[1]) == int) and t[1] >= 0:
                self.sec += t[1] * 60
            else:
                raise ValueError('Invalid value for the minute element.')
            ## Second
            if (type(t[2]) == float or type(t[2]) == int) and t[2] >= 0:
                self.sec += t[2]
            else:
                raise ValueError('Invalid value for the second element.')
        else:
            raise ValueError('Invalid value to create an hms class instance.')

    def decimal(self):
        return self.sec / 3600
    
    def sexagesimal(self):
        t = abs(self.sec)
        h = t // 3600
        t %= 3600
        m = t // 60
        t %= 60
        s = t
        return [int(h), int(m), s]
            
    def __str__(self):
        hms = self.sexagesimal()
        hour = self.decimal()
        if self.sec >= 0:
            return '{:d}h {:d}m {:.4f}s\n{:f}'.format(hms[0], hms[1], hms[2], hour)
        else:
            return '-{:d}h {:d}m {:.4f}s\n{:f}'.format(hms[0], hms[1], hms[2], hour) 

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        # When another is the same hms class instance
        if type(other) == hms:
            return hms(self.sec + other.sec, second = True)
        # When given a single float or integer value
        elif type(other) == float or type(other) == int:
            return hms(self.sec + other * 3600, second = True)
        # When given a sexiagesimal list
        elif type(other) == list and len(other) == 3:
            return hms(self.sec + other[0] * 3600 \
                       + other[1] * 60 + other[2], second = True)
        else:
            raise ValueError('Invalid value to add.')
            
    def __sub__(self, other):
        # When another is the same hms class instance
        if type(other) == hms:
            return hms(self.sec - other.sec, second = True)
        # When given a single float or integer value
        elif type(other) == float or type(other) == int:
            return hms(self.sec - other * 3600, second = True)
        # When given a sexiagesimal list
        elif type(other) == list and len(other) == 3:
            return hms(self.sec - other[0] * 3600 \
                       - other[1] * 60 - other[2], second = True)
        else:
            raise ValueError('Invalid value to subtract.')
            
    def __neg__(self):
        return hms(-self.sec, second = True)
    
    def __abs__(self):
        return hms(abs(self.sec), second = True)
    
    def __eq__(self, other):
        if type(other) == hms:
            return self.sec == other.sec
        else:
            raise ValueError('Invalid value to compare.')
            
    def __neq__(self, other):
        if type(other) == hms:
            return self.sec != other.sec
        else:
            raise ValueError('Invalid value to compare.')
            
    def __lt__(self, other):
        if type(other) == hms:
            return self.sec < other.sec
        else:
            raise ValueError('Invalid value to compare.')

    def __le__(self, other):
        if type(other) == hms:
            return self.sec <= other.sec
        else:
            raise ValueError('Invalid value to compare.')
    
    def __gt__(self, other):
        if type(other) == hms:
            return self.sec > other.sec
        else:
            raise ValueError('Invalid value to compare.')

    def __ge__(self, other):
        if type(other) == hms:
            return self.sec >= other.sec
        else:
            raise ValueError('Invalid value to compare.')
    
    ## Workaround for MicroPython in NumWorks
    def neg(self):
        return self.__neg__()
    
    def Abs(self):
        return self.__abs__()