
# QUE: Print all values from 1 to 100 except the ones divisible by 3 or 5.

x = 1

while x <= 100:
    if not((x % 3 == 0) or (x % 5 == 0)):
        print(x)
    x += 1

print('\nEnumerate example-')
# For loop can use enumerate ability to get the index of the current loop along with the value

for i, num in enumerate(range(0, 101, 2)):
    if num%3 != 0 and num%5 != 0 and num <50:
        print(i, num)


