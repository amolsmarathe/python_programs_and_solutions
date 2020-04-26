#
# SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and
# extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
#
# summer_69([1, 3, 5]) --> 9
# summer_69([4, 5, 6, 7, 8, 9]) --> 9
# summer_69([2, 1, 6, 9, 11]) --> 14

#####################
# Following is my answer:
#####################

list_question = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 2, 3, 6, 7, 8, 9, 5]
list1 = list_question       # We have to do this if the original list have to be kept intact which is the case mostly

print('Original list is: \n', list1)

for i, num in enumerate(list1):
    if num == 6:
        for j, number in enumerate(list1[i + 1:]):
            if number != 9:
                list1[list1.index(number)] = 0
                continue
            else:
                list1[list1.index(number)] = 0
                break
        list1[i] = 0
        continue
    else:
        continue

print('Modified list is: \n', list1)
print('\nExpected addition of numbers is: ', sum(list1))


########################
# Following is Udemy Answer - this is memory efficient answer since it does not need an additional duplicate list
########################


total = 0
add = True
for num in list_question:
    while add:
        if num != 6:
            total += num
            break
        else:
            add = False
    while not add:
        if num != 9:
            break
        else:
            add = True
            break

print('\nAnswer using Udemy solution is: ', total)
