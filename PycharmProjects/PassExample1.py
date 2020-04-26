
# QUE - PASS : Print all odd numbers in 1-10 using "PASS"

for i in range(11):
    if i % 2 == 0:
        pass
        # this will pass only the if statement and continue to else statement and all further statements in for loop
        # On contrary, continue statement will continue directly to the next i and skip all next statements in for loop
        # NOTE that pass also executes the immediate else statement
        # pass is mostly used while defining empty function or class unlike continue and break which are mostly
        # useful only inside loops
    else:
        print(i)