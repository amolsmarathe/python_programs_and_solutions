# Print the list of prime numbers in 1-100


# Below Code works but is not an efficient way!
# ????? In the first iteration itself, the range is from (2, 1) Why does it still work without error????????
# Google the most efficient way!

for i in range(2, 101):
    for j in range(2, i - 1):
        if i % j == 0:
            break
    else:
        print(i, end=', ')


