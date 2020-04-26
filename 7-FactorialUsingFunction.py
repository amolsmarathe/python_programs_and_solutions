# QUE: Print factorial of a number using function.

print(' Welcome to factorial printing service!')
x = int(input(' Enter the number of which you want to calculate a factorial- '))


def fact(n):
    ans = 1
    for i in range(n, 0, -1):
        ans = ans * i

    print(ans)


fact(x)
