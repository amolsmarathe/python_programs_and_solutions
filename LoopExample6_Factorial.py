
# Find a factorial of a given number


# Find what is the most efficient way to do this?

# ANS-1:

next1, prev = 1, 1
for i in range(1, 7):
    next1 = prev * (i + 1)
    prev = next1
print(next1)

# ANS-2:

next2, prev2, x = 1, 7, 7
for i in range(1, 7):
    next2 = prev2 * (x-i)
    prev2 = next2
print(next2)


