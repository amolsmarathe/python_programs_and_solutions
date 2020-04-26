
# 2D Arrays

# Operations supported on arrays:

# Attributes: dtype, ndim, shape, size
# Functions: flatten(), reshape(rows, cols), reshape(#of matrices, rows, cols), matrix(), diagonal(matrix), min(), max()
import numpy
from numpy import *

arr1 = array([[2,4,5,], [6,4,3,]])
print(arr1)

print('\n', arr1.dtype)         # get type of the elements in array

print('\n', arr1.ndim)          # get dimensions of array

print('\n', arr1.flatten())       # get single dim array from 2D/3D array

print('\n', arr1.size)          # get size of the array i.e. total number of elements

arr2 = array([[2,4,5,4,5,6], [6,4,3,7,3,9]])

print('\n', arr2.reshape(2,3,2))    # reshape matrix into 2 matrices of 3 rows and 2 cols each

print('\n Converted Matrix is- \n', matrix(arr2))  # to convert array into matrix. Some issue with this usage, google it
m1 = matrix(arr2)

m2 = matrix('2,3,4; 4,5,3; 8,3,5')        # Simply create a matrix with numbers
print('\n created Matrix is M2- \n', m2)

print('\n Diagonal elements are M2(diagonal)- \n', diagonal(m2))               # get diagonal elements of matrix

print('\n Min value in the matrix is M2(min)- ', m2.min())               # get min value

print('\n Max value in the matrix is M2(max)- ', m2.max())               # get max value


m3 = matrix('6,4,7; 3,8,7; 3,2,5')

m4 = m2 + m3            # Simply add 2 matrices
print('\n Addition of matrices is M4- \n', m4)

m5 = m2 * m3            # Simply multiply 2 matrices
print('\n Multiplication of matrices is M5- \n', m5)


# Multiplication without using in built function:

# m8 = m6(3x4) * m7 (4x5)


m6 = matrix('2,4,5,7; 7,4,7,6; 4,9,8,0')
m7 = matrix('6,7,3,3,4; 5,8,9,9,5; 3,3,1,1,5; 6,7,9,0,0')
m8 = numpy.zeros((3,5)).astype(int)

print('\n BY DEFAULT, zeros matrix is FLOAT. Check if the matrix is converted to int M8- \n', m8)

temp = 0

for i in range(3):
    for j in range(5):
        for k in range(4):
            temp = temp + m6[[i], [k]] * m7[[k], [j]]
        m8[[i], [j]] = temp
        temp = 0
print('\n Multiplication without using in build function is- \n', m8)
print('\n Multiplication using in built function is- \n', m6*m7)

