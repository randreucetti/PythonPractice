'''
Created on 18 Nov 2014

@author: ross
'''

s = "This is a string"

# Prints the length of a string (or any object?)
print len(s)

# Gets a char within a string
print s[5]
print s[-5]
print s[3:9]

# integer string concatation
a = 1
b = 2
c = 3

print `a` + `b` + `c`

# some other useful bits
print s.lower()
print s.upper()

print s.startswith('T')
