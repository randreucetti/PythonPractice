'''
Created on 18 Nov 2014

@author: ross
'''

mylist = ["Linux", "Mac OS" , "Windows"]
# Print the first list element
print(mylist[0])
# Print the last element
# Negativ values starts the list from the end
print(mylist[-1])
# Sublist - first and second element
print(mylist[0:2])
# Add elements to the list
mylist.append("Android")
# Print the content of the list
for element in mylist:
    print(element) 
  
duplicateList = ["Linux", "Linux", "Windows"]
print list(set(duplicateList))