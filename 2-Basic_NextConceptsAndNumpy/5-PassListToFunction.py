
# We can pass a list as argument to a function.

# QUE: pass a list to a function and print the even and add numbers of the list.


def fun(lst):
    even, odd = 0, 0
    for n in lst:
        if n % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd


list1 = [1, 2, 3, 4, 5, 6, 7]

even, odd = fun(list1)
print(even, odd)

print('\n Even numbers count is {} and Odd numbers count is {}'.format(even, odd))


#                            # adding proper format to the print function


# QUE: Take 10 names from the user and print only those who have length more than 5


def count():
    x = int(input('\n How many names would you like to test? '))
    list2 = []
    for i in range(x):
        list2.append(input('\n Enter the name{}- '.format(i)))

    count1 = 0
    for e in list2:
        if len(e) > 5:
            count1 += 1
    print('\n Count of names having length greater than 5 is- ', count1)


count()

