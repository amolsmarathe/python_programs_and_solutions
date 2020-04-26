
# QUE: Print first 50 numbers in a fibonacci series. (Series starts with 0 and
# every next number in series is addition of last 2 numbers in the series)

temp1, temp2, next1 = 0, 1, 0

for i in range(30):
    print(next1)
    next1 = temp1 + temp2
    temp1 = temp2
    temp2 = next1

