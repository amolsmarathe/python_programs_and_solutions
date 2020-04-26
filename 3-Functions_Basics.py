# Functions can be created to perform certain tasks
# Functions can return nothing, or may return single or multiple values
# Function is to be DEFINED and then CALLED

# Types of arg- Formal (defined in function) and Actual (given while calling a function)
# Types of Actual arg- Position, keyword, default, variable length


def add_sub(x, y):
    c = x + y
    d = x - y
    return c, d


result1, result2 = add_sub(10, 15)

print(result1, result2)

print(add_sub(30, 20))  # this prints the tupple of the function output


# Position and Keywordarguments- the function always considers the default sequence of definition and accepts values
# only in that order while calling the function. If you do not know the order, simply define the the values along with
# the name of arg while calling the function

def person(name, age):
    print('\n Name is-', name)
    print('\n Age is- ', age)


person('Amol', 28)  # This works if you know the exact position of the arguments

person(age=28, name='Amol')  # this works when you dont know the exact position of the arguments


def person2(name, age=18):  # This way, you can define the default value of the argument
    print('\n Name is-', name)
    print('\n Age is- ', age)


person2('Amol')  # In this way, only one argument is sufficient, for the others it takes default value


def sum1(a, *b):  # *b now is a variable which is a 'tuple' to be spcific and user can pass any # of args
    for n in b:
        a = a + n
    print('\n Sum1 is- ', a)


sum1(2, 4, 5, 6)
sum1(5, 9)
sum1(10, 20, 30)


def sum2(*b):  # *b is now a tuple again. This time only one arg would also work. just note that
    # the function definition will change a little bit (we define initial value of a as 0)
    a = 0
    for n in b:
        a = a + n
    print('\n Sum2 is- ', a)


sum2(5)
sum2(2, 5)
sum2(2, 4, 7, 9)


def person2(name, *data):  # this time again *data can have any number of arg which will form a tuple
    print('\n', name)  # Problem with this is, we do not know what is the data coming in as args
    print(data)  # this will print only argument values, we do not know what are they


person2('Amol', 29, 'Pune', 8983495022)


def person3(name, **data):  # Now, **data can take 'key=value' pair in the argument and print in the same way
    print('\n', name)
    print(data)  # This will print argument values, along with the key which is passed while calling function


person3('Amol', age=28, city='Pune', mobile=8983495022)
