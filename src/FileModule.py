'''
Created on 18 Nov 2014

@author: ross
'''

f = open('../resources/input.txt', 'r')
print f

output = open('../resources/output.txt', 'w')
for line in f:
    output.write(line.rstrip() + '\n')

f.close()