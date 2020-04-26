

def fun1(str1):
    """
    Check the number of upper and lower case characters in a given string
    """

    c_up, c_low = 0, 0
    for i in str1:
        if i.lower() in 'abcdefghijklmnopqrstuvwxyz':
            if i == i.upper():
                c_up += 1
            else:
                c_low += 1
        else:
            continue
    return c_up, c_low


print(fun1('What am I supposed tO dO?45651'))

list1 = [1, 1, 1, 1, 11, 222, 3, 343, 4, 45, 5, 6, 76, 7, 8, 9, 9]

import string  # Imported to use the .ascii_lowercase property which has all alphabets in lowercase


def fun2(str1):
    """
    Check the if the given string contains all the alphabets at least once
    """

    alpha = string.ascii_lowercase
    set1 = set(str1)
    if len(set1) < 26:
        print('NOT all alphabets')
    else:
        for i in range(26):
            if alpha[i] not in set1:
                print('NOT all alphabets')
                break
        else:
            print('ALL alphabets')


fun2('aadkhbhbvuw qwerpoiuuyterlkjhasdfmnbvzxcvewdsfwefvefvmlklhdsffvhjevgjeh gcd')
