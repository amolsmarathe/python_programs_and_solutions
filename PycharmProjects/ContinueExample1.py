# QUE - CONTINUE: Print only odd numbers from 1-10 using "CONTINUE"

for i in range(11):
    if i % 2 == 0:
        continue
        # this will directly continue to the next i in the for loop skipping all further statements inside "for loop"
        # On contrary, pass only passes the if statement and continues to further statements inside "for loop"
        # pass also executes the immediate else statement!
        # pass is mostly used while defining empty function or class unlike continue and break which are mostly
        # useful only inside loops
    print(i)
