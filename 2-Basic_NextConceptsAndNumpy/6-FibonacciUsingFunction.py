# QUE: A program should ask for user input about how many numbers of the Fibonacci series does he want to print?
# Then asks do you want to set a upper limit for the maximum number where you should stop?
# Accordingly print the fibonacci series.

n = int(input('How many numbers do you want to print from the Fibonacci series? '))

limit = input('Do you want to set upper limit for the last number to print yes/no? ')

if limit == 'yes':
    x = int(input('Enter the upper limit- '))


def fib(**data):
    n1 = int(data['count'])
    if len(data) == 2:
        x1 = int(data['lim'])

    a = 0
    b = 1
    if n1 <= 2:
        if n1 == 1:
            print(a, '.')
        else:
            print(a, ', ', b, '.')
    else:
        print(a, ', ', b, end='')

        for i in range(n1 - 2):
            c = a + b
            a = b
            b = c

            if len(data) == 2:
                if c > x1:
                    print('.')
                    break
                else:
                    if i == n1-3:
                        print(', ', c, end='.')
                    else:
                        print(', ', c, end='')
            else:
                print(' ', c, end='')
                if i == n1 - 3:
                    print('.')
                else:
                    print(', ', end='')


if limit == 'yes':
    fib(count=n, lim=x)
else:
    fib(count=n)
