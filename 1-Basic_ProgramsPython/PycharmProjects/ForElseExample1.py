
# We cas use For ... Else in Python which is not possible in every other language.
# For .. Else ONLY works when we have a IF...BREAK statement inside For loop. Remember, BREAK is mandatory.
# The idea is, if the if statement has never broken, it will execute the else condition for 'for loop'


# QUE: Print Only first prime number in any list and then print "Not found!", all using for...else statement


x = [22, 45, 34, 66, 34]

for i in x:
    if i % 2 != 0 and i % 3 != 0:
        print(i)
        break
else:
    print('Not found!')
