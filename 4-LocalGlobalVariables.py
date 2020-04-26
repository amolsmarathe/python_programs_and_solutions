# Local- defined inside the function

# Global- defined outside the function

# Global can always be accessed inside function, given that same variable is not defined inside function, however,
# local variable cannot be accessed outside the function
# Local and global variables are different
# 'global'-Global variable can be recalled inside a function using 'global' function - BUT with such usage, BOTH local &
# GLOBAL variables cannot exist inside a function at the same time. Changes are directly reflected on global
# variable from within the function
# 'globals' - function can be used when we need BOTH local as well as global variables to be accessed in function



# Local and global variables are different

a = 10


def fun():
    a = 15
    print('\n a inside function= ', a, 'with address= ', id(a))


fun()

print(' a outside function= ', a, 'with address= ', id(a))


# 'global'-  Global variable can be recalled inside a function using global function:

a = 10


def fun():
    global a
    a = 15
    print('\n a inside function= ', a, 'with address= ', id(a))


fun()

print(' a outside function= ', a, 'with address= ', id(a))


# 'globals'-  Global as well as local variable can be accessed inside a function using globals function:

a = 10


def fun():
    x = globals()['a']
    a = 15
    print('\n a inside function= ', a, 'with address= ', id(a))
    print(' Value of global variable \'a\' accessed inside function is = ', x)


fun()

print(' a outside function= ', a, 'with address= ', id(a))

