'''
Created on 18 Nov 2014

@author: ross
'''

#This is a comment
def add(a,b):
    return a+b

#Adds 5 to parameter
def addFixedValue(a):
    return 5 + a

print add(4,5)

print addFixedValue(5)

# Python is dynamically typed

a = "Hello"
b = 15

print a

print b

assert(1==1)

# For Looping

i = 1

for i in range(1 ,10):
    if i < 5:
        print "Smaller or equal than 5.\n"
    else:
        print "Larger than 5\n"
        