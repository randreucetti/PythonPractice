'''
Created on 18 Nov 2014

@author: ross
'''

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return "x-value: " + str(self.x) + " y-value: " + str(self.y)
    def __add__(self, other):
        p = Point()
        p.x = self.x + other.x
        p.y = self.y + other.y
        return p
    
p1 = Point(3,6)
p2 = Point(8,7)
print p1
print p1.y
print (p1 + p2)