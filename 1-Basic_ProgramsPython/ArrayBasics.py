# Arrays in python are same as list but only difference is all elements of array must be of SAME TYPE
# Moreover, array's size it flexible to work with. You can extend or shrink it as per need. WHAT IS THE USE OF THIS????
# It is not available by default, need to IMPORT ARRAY module.
# Use SQUARE brackets to create an array as well as to access its elements.

# Check more on google about the 'type codes' which can be b, B, u, h, H, i, I, l, L, f, d
# where e.g. i is int (2 bytes size) and d is float (8 bytes in size)


# this is in branch to push changes

from array import *

val = array('i', [2, 4, 6, 8, 3])

print(val.buffer_info())        # this gives address and size of the array

print(val.typecode)             # gives the type code of array elements

for i in range(len(val)):       # for loop to print all values in val array
    print(val[i], end=', ')

print()
for e in val:                   # EVEN MORE EFFICIENT WAY to use for loop

    print(e, end='.. ')


newarr = array(val.typecode, (a**2 for a in val))       # Creating new array from the old array
print('\n', newarr)




