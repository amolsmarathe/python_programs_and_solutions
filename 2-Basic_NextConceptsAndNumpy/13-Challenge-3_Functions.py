# COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
#
# count_primes(100) --> 25
#
# By convention, 0 and 1 are not prime.

#####################
# Udemy answer below. It is more a math problem than a coding problem.
#####################


def count_primes(num):
    primes = [2]
    x = 3
    if num < 2:  # for the case of num = 0 or 1
        return 0
    while x <= num:
        for y in range(3, x, 2):  # test all odd factors up to x-1
            if x % y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)


# Faster version which uses the prime list itself:


def count_primes2(num):
    primes = [2]
    x = 3
    if num < 2:
        return 0
    while x <= num:
        for y in primes:  # use the primes list!
            if x % y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)
