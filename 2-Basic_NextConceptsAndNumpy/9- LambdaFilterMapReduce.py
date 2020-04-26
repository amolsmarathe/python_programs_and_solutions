# Lambda is a function without name. Or it is called as an expression
# lambda functions/expressions can have only single expression to evaluate and it returns its value
# All Functions are also objects in python
# Lambda functions/expressions return the value of the expression
# Filter, Map, Reduce - filter() and map() return a list whereas reduce() returns a value
# Out of the 3, only reduce() needs specific import from functools


f = lambda a: a * a  # Here, a is variable/argument, a*a is returned
print('\n Print a square using lambda function- ', f(5))

add = lambda b, c: b + c  # Here, b, c are arguments, b+c is returned
print('\n Addition using lambda function is- ', add(3, 4))

# Filter() is a function to filter values in a list e.g. to filter even values as given in below example
# function+filter example-

print('\n Filter the list using function+filter: ')
list1 = [2, 3, 4, 8, 7, 5, 4, 3]

def fun1(n):
    return n % 2 == 0

list2 = list(filter(fun1, list1))
print(list2)


# lambda+filter example-

print('\n Filter the list using lambda+filter: ')
list1 = [2, 3, 4, 8, 7, 5, 4, 3]

list2 = list(filter(lambda n: n%2 == 0, list1))
print(list2)


# Map() is a function to operate on values in a list e.g. to make double of each list value as given in below example
# function+map example-

def fun2(n):
    return n*2

print('\n Double each of the list value using function+map: ')
list2 = list(map(fun2, list1))
print(list2)

# lambda+map example-

print('\n Double each of the list value using lambda+map: ')
list2 = list(map((lambda n: n*2), list1))
print(list2)

# Reduce() is a function to operate on all values in a list to provide one value in return.
# e.g. to add all the list values as given in below example
# NOTE that reduce() function needs a special import
# function+reduce example-

from functools import reduce

print('\n Sum of all elements of the list function+reduce: ')
def fun3(a, b):
    return a + b

sum = reduce(fun3, list1)
print(sum)

# lambda+reduce example-

from functools import reduce

print('\n Sum of all elements of the list lambda+reduce: ')

sum = reduce(lambda a, b: a + b, list1)
print(sum)

