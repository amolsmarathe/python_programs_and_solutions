

# Print following pattern:
    #
   ##
  ###
 ####
#####

for i in range(5):
    for j in range(5-i):
        print(' ',end='')
    for k in range(4-i, 5):
        print('#', end='')
    print()
