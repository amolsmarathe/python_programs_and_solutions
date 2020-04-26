# Recursion is calling function inside a function. Simple!

# QUE: Create program to print factorial of a given number using recursion.


def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


print(fact(7))

# QUE: Another example- Print 1-5 values using recursion in function


x = 1


def p():
    global x
    print(x)
    if x < 5:
        x += 1
        p()


p()
