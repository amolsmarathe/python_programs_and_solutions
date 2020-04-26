
# Exception handling by 4 ways - try-except, try-except-else, try-except-finally, try-except-else-finally
# try-except: try 1, if error, execute except
# try-except-else: try 1, execute either except OR else (if error, execute except, if no error, execute else)
# try-except-finally: try 1, execute BOTH except AND finally (if error, execute except, always execute finally)
# try-except-else-finally: try 1, execute either except OR else, always execute finally
# finally is mostly useful to disconnect any database connection/closing a resource file after the operation
# irrespective of operation is successful or not, in order to avoid keeping the resource open mistakenly

# Yo can also check for specific type of error such as 'ZeroDivision Error', 'ValueError', etc.
# except zeroDivisionError as e: Checks only for ZeroDivisionError and stores it in e, so that e can be printed
# except ValueError as e: Checks only for ValueError and stores it in e, so that e can be printed
# except Exception as e: Checks any type of error and stores it in e, so that e can be printed


print('Example-1:')
# Example-1: Simple use of exception handling while taking an user input as number.

while True:
    try:
        x = int(input('Enter a number between 1-9: '))
    except:
        print('Invalid input! Please enter only a number.')
    else:
        if x in range (1,10):
            break
        else:
            print('The number is not in the range 1-9. Try again.')
            continue

print(f'{x} was taken as input')
print('\n')
###############
print('\nExample-2:')

for i in ['a', 'b', 3]:
    try:
        print(f'{i**2} is the square of {i}')
    except:
        print(f'{i} is not a number')


###############
print('\nExample-3: ')

x, y = 2, 3

try:
    print(f'Division is- {x/y}')
except ZeroDivisionError as e:
    print(f'Denominator is zero hence reversing the position of numerator and denominator. \nNew division is- {y/x}', e)
except ValueError as e:
    print('There was a ValueError', e)
except Exception as e:
    print('Any other error apart from ZeroDivisionError and ValueError', e)
else:
    print('Denominator was not zero! Excellent! No Error!')
finally:
    print('End of Division exercise')



