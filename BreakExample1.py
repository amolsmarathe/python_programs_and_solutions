
# QUE - BREAK: There are total 3 candies in stock. Ask user how many candies he wants and print candies that times.
# If He asks more candies than available, print the available number of candies and then print OUT OF STOCK

a = 3    # available candies
x = int(input('Hey, how many candies do you want? '))

i = 1
while i < x:
    if i > a:
        print('Sorry, we are OUT OF STOCK')
        break
        # this will simply break the loop and come out of the loop by skipping everything next in the loop
        # pass is mostly used while defining empty function or class unlike continue and break which are mostly
        # useful only inside loops
    else:
        print('Candi')
        i += 1
