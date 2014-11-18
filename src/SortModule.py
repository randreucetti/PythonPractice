'''
Created on 18 Nov 2014

@author: ross
'''

def mergeSort(numbers):
    if len(numbers) <= 1:
        return numbers
    left = []
    right = []
    result = []
    
    middle = len(numbers) / 2
    
    i = 0
    
    while i < middle:
        left.append(numbers[i])
        i += 1
    
    while i < len(numbers):
        right.append(numbers[i])
        i += 1
    
    left = mergeSort(left)
    right = mergeSort(right)
    result = merge(left, right)
    return result

def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        elif len(left) > 0:
            result.append(left.pop(0))
        elif len(right) > 0:
            result.append(right.pop(0))
    
    return result

def bubbleSort(numbers):
    for i in range(len(numbers)):
        for k in range(len(numbers) - 1, i, -1):
            if numbers[k] < numbers[k - 1]:
                swap(numbers, k, k - 1)
               
def swap(numbers, x , y):
    tmp = numbers[x]
    numbers[x] = numbers[y]
    numbers[y] = tmp
                

f = open('../resources/numbers.txt', 'r')

numbers = []

for line in f:
    numbers.append(int(line.rstrip()))
    
print numbers

print mergeSort(numbers)

bubbleSort(numbers)

print numbers


    
    
