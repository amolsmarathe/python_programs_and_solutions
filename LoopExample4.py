# QUE: Print first 20 numbers which are neither divisible by nor by 3.
# Also verify and print that the count is exactly 20.

x, i = 1, 1
l1 = []

while i <= 20:
    if x % 2 == 0 or x % 3 == 0:
        pass
    else:
        l1.append(i)
        print(x, end=', ')
        i += 1
    x += 1
print('\n Count of total numbers printed (using PASS) is: ', l1.__len__())
print('\n')




# Same can be achieved using 'CONTINUE':

x, i = 1, 1
l1.clear()

while i <= 20:
    if x % 2 == 0 or x % 3 == 0:
        x += 1
        continue
    else:
        l1.append(i)
        print(x, end=', ')
        i += 1
    x += 1

print('\n Count of total numbers printed (using CONTINUE) is: ', l1.__len__())
