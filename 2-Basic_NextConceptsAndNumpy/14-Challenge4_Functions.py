
# Check if all the alphabets are present in the given string


import string               # can be used to get all alphabets in english


def fun(str):
    alpha = string.ascii_lowercase          # gets all alphabets in english
    set1 = set(str)                         # create a set so that all elements are unique
    if len(set1) < 26:
        print('NOT all alphabets')
    else:
        for i in range(26):
            if alpha[i] not in set1:
                print('NOT all alphabets')
                break
        else:
            print('ALL alphabets')


fun('dsajads')
