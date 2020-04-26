
# QUE: Create an array of n values from user and delete the value at index 2 without using built-in function

from array import *

n = int(input('Enter how many values do you want in the array-  '))
x = array('i', [])

for i in range(n):
    x.append(int(input('Enter the number of your choice- ')))

print(x)

# QUE: Write the code to reverse an array without using built-in function:

arr2 = array('i', [])
for i in range(1, len(x)+1):
    arr2.append(x[len(x)-i])

print('\n Reversed array is: ')
print(arr2)
