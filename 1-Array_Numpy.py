
# Creating arrays in numpy possible using 6 ways:
# array()
# linspace()
# logspace()
# arrange()
# zeros()
# ones()

# numpy array()- it is not mandatory to give 'type' of an array element while creating an array, unlike in normal python
# numpy array()- if anyone of the array element is float, all other elements are converted into float by default

from numpy import *
newarr1 = array([2,4,5,6.0,87])

print('Array using array(): ', newarr1, '\n')
print('Type of the array elements is: ', newarr1.dtype, '\n')

# linspace()- break the range into number of "equal" parts
# it is like range (including both endpoints), by default creates 50 parts or you can mention the
# required parts as third argument


arr2 = linspace(0, 16, 16)
print('Array using linspace() with set number of parts of the range- \n', arr2, '\n')
arr3 = linspace(0, 16)
print('Array using linspace() without setting number of parts of the range (it creates 50 parts by default)- \n', arr3, '\n')

# arange()- it is also a range with third argument for the step of increament

arr3 = arange(0,16, 2)
print('Array using arange() with range 0-16 and step of 2- ', arr3, type(arr3))

# Operations on Arrays:

arr4 = arr3 + 5        # cretes new array by adding 5 to each element of newarr3
print('\n New copied array is- ', arr4, type(arr4))

arr5 = arr3 + arr4     # Addition of 2 arrays, also called 'Vectorized operation'
print('\n New addition arrays is: ', arr5, type(arr5))


# sin, cos, tan, log, sum, min, max, square root, find unique, sort, concatenate operations on array

print(sin(arr4))        # sin of each element of arr4

print (cos(arr4))       # cos od each element of array 4

print(tan(arr4))

print(log(arr4))

print(sum(arr4))

print(min(arr4), max(arr4))

print(sqrt(arr4))

print(unique(arr4))

print(sort(arr4))

# arr6 = concatenate(arr4, arr5)
# print(arr6)


# Copying Arrays:

arr7 = arr5             # this is not a copy but only different alias for 2 arrays with same address (id)
print('\n Check the address(id) of arr7: ', id(arr7), ' and the address (id) of arr5: ', id(arr5), ' are EQUAL.')

arr8 = arr7.view()      # this is SHALLOW COPY of the array, i.e. different id for but but they are dependent on
                        # each other i.e. changes in one are also reflected in the other
print('\n Check the address(id) of arr8: ', id(arr8), ' and the address (id) of arr7: ', id(arr7), ' are DISCRETE')
print('Any change in the elements of arr8 will automatically reflect in arr7 and vie versa')

arr9 = arr8.copy()      # this is DEEP COPY, i.e. they are totally different arrays with different ids & are independent

# For Practice:Addition of 2 arrays without using in built function
# How to achieve this ???????????? Following code fails!!!!!!!

# arr10 = array([])
# for i in range(len(arr8)):
#    arr10.append(arr8[i]+arr9[i])
# print('\n Addition of arr8 and arr9 without in built function is- ', arr10)

# Find a max number in an array without using built in function:

max = arr9[0]

for n in arr9:
    if n > max:
        max = n
print(max)


