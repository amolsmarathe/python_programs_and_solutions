# QUE: Print following patterns:
# Pattern-1: (include all hash in print)
#
# #
# # #
# # # #

# Pattern-2: (include all hash in print)
# # # #
# # #
# #
#

# Pattern-3: (exclude all hash in print)
# 1 2 3 4
# 1 2 3
# 1 2
# 1

# Pattern-4: (exclude all hash in print) - THIS IS TRICKY!
# A P Q R
# A B Q R
# A B C R
# A B C D

# Pattern-5:
    #
   ##
  ###
 ####
#####


# ANS: Pattern-1:

j = 1
for i in range(4):
    while j <= 4:
        for temp in range(j):
            print('#', end=' ')
        j += 1
        print()


# OR BETTER answer can be:

i = 1
while i <= 4:
    for j in range(i):
        print('#', end=' ')
    i += 1
    print()


# OR the BEST answer is:

for i in range(4):
    for j in range(i + 1):
        print('#', end=' ')
    print()

print('\n')


# ANS: Pattern-2:

i = 4
while i > 0:
    for j in range(i):
        print('#', end=' ')
    i -= 1
    print()


# OR the BEST answer is:

for i in range(4):
    for j in range(4 - i):
        print('# ', end='')
    print()


# ANS: Pattern-3:

for i in range(4):
    for j in range(4-i):
        print(i+1, end='')
        i += 1
    print()


# ANS: Pattern-4:

x = 'ABCD'
y = 'PQR'

for i in range(4):

    for j in range(i+1):
        print(x[j], end=' ')
    for k in range(i, 3):
        print(y[k], end=' ')
    print()


# ANS: Pattern-5:

for i in range(5):
    for j in range(5-i):
        print(' ',end='')
    for k in range(4-i, 5):
        print('#', end='')
    print()
