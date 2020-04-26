#
# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
#
#  spy_game([1,2,4,0,0,7,5]) --> True
#  spy_game([1,0,2,4,0,5,7]) --> True
#  spy_game([1,7,2,0,4,5,0]) --> False

#####################
# My answer is:
#####################

list_question1 = [1, 2, 4, 0, 0, 7, 5]
list_question2 = [1, 0, 2, 4, 0, 5, 7]
list_question3 = [1, 7, 2, 0, 4, 5, 0]


def spy(lst):
    count = 0
    for num in lst:
        if num == 0 and count < 2:
            count += 1
        elif num == 7 and count == 2:
            count += 1
            break
        else:
            continue
    if count == 3:
        return True
    else:
        return False


print('\nMy answer: ')
print(spy(list_question1), spy(list_question2), spy(list_question3), '\n')


#####################
# Udemy answer: interesting logic applied! Very less lines of code! Just go through it :)
#####################

def spy_game(nums):
    code = [0, 0, 7, 'x']

    for num in nums:
        if num == code[0]:
            code.pop(0)  # code.remove(num) also works

    return len(code) == 1


print('Udemy answer: ')
print(spy_game(list_question1), spy_game(list_question2), spy_game(list_question3), '\n')
