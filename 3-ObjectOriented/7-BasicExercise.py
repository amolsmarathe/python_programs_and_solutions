
# QUE1: Create class Line to take co-ordinates in the form of a pair of tuples and print slope and distance of the line

print('QUE1:')


class Line:
    def __init__(self, cord1, cord2):
        self.cord1 = cord1
        self.cord2 = cord2

    def distance(self):
        x1, y1 = self.cord1  # Nice use of tuple unpacking!
        x2, y2 = self.cord2
        return ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5

    def slope(self):
        x1, y1 = self.cord1  # Nice use of tuple unpacking!
        x2, y2 = self.cord2
        return (y2 - y1) / (x2 - x1)


l1 = Line((2, 4), (6, 8))
print(f'{l1.distance()} - is distance between 2 points')
print(f'{l1.slope()} - is slope of the line')

print('\nQUE2:')
# QUE2: Create a bank acc class that has 2 attributes owner and balance. Create 2 methods for deposit and withdraw.
# Ensure that the owner is not withdrawing more that what he has currently in acc.

class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        print(f'Deposit Successful! Currrent Balance is {self.balance + amount}')

    def withdraw(self, amount):
        if amount > self.balance:
            print('You do not have sufficient balance to withdraw this amount. Try lesser amount.')
        else:
            print(f'Withdrawal Successful! Currrent Balance is {self.balance - amount}')

acc1 = BankAccount('Amol', 500)

acc1.deposit(400)
acc1.withdraw(300)
acc1.withdraw(900)
