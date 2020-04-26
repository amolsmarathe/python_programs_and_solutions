
# Generators will give iterator to iterate through, one at a time, instead of creating whole list in memory at once
# Generators are memory efficient. range(10) is an example of a generator.
# if user needs the list, he can transform the generator into a list  using list(range(10))
# Generator will mostly have a for loop or while loop inside it
# replace 'return' in a function by 'yield'. User for loop to go through values in the generator or use next() function
# Note that the code written after yield is also executed unlike return. Incase of return the loop terminates there.
# Used when instead of getting bunch of values from database, which will consume memory, we work on one value at a time
# Defined in a function NOT at class level unlike iterators

# NOTE: to get next value of generator using next() function, you must first save the generator as a variable and then
# pass that variable (which is now an iterator) to next() function. For example, if generator is a generator,
# next(generator()) is invalid. instead use variable = generator() and next(variable). On the other hand, while using
# for loop on a generator, it is possible to use both "for n in generator()" as well as "for n in variable"


# Example-1:


def gen1():

    yield 1             # iteration 1
    yield 2             # iteration 2
    yield 3             # iteration 3
    yield 4             # iteration 4


values1 = gen1()             # values1 here, is the iterator

print(values1.__next__())    # next value in the values1 iterator

for i in values1:            # This for loop will continue from the second value in the values1 iterator since first was
    print(i)                 # already accessed above. __next__() or next() method stores previous iteration index


print('\nExample-2: ')

# Example-2:


def gen2():

    n = 1

    while n < 10:           # while loop to yield different values
        sq = n*n
        yield sq            # every loop yields new value of sq
        n += 1


values2 = gen2()            # values2 here, it the iterator, it is mandatory when you want to use next() function

print(next(values2))        # next value in the values2 iterator, ONE CANNOT USE next(gen2()), MUST use next(variable)
print(next(values2))        # next value in the values2 iterator
print(next(values2))

print('All numbers in gen2()')
for i in gen2():            # This for loop will continue from the third value in the values2 iterator since first 2were
    print(i)                # already accessed above. __next__() or next() method stores previous iteration index.
    #                         Can use both "for i in gen2()" as well as "for i in values"


# Example-3: Fibonacci series using generator: (Excellent example!)
print('Example-3: ')


def fib(n):
    a, b = 0, 1
    limit = 0
    while limit < n:
        yield a
        a, b = b, a + b
        limit += 1


fibon = fib(20)


print('Print using next() function')
print(next(fibon))              # NOTE reminder- next(fibon) is supported, but NOT next(fib())
print(next(fibon))

print('Print remaining using for loop')
for n in fibon:                 # NOTE reminder- both "for n in fibon" as well as "for n in fib()" are supported
    print(n)



