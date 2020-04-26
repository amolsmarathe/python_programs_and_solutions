
# operator overload is used when you want to use operators like +-<>, on objects
# you can define the __operator__ method in the class of that object, so everytime we use that operator on that object,
# it would call that method from its class
# Operator overload also used to pass any object in print() to print its content which would otherwise print its ADDRESS
# Methods to use for such overload:
#   - __str__ : must return a string because by default, print function works the same print(a) = print(a.__str__())
#   - __add__ : +
#   - __sub__ : -
#   - __mul__ : *
#   - __div__ : /
#   - __lt__  : <
#   - __gt__  : >
#   - __ge__  : >=
#   - ... and so on


class Student:

    def __init__(self, m1, m2):             # This is initializing variables m1 and m2
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):               # This is for overloading + operator between objects of Student class
        result1 = self.m1 + other.m1
        result2 = self.m2 + other.m2
        return result1, result2             # This will return a tuple NOT values only but a tuple of values

    def __sub__(self, other):               # This is for overloading - operator between objects of Student class
        result1 = self.m1 - other.m1
        result2 = self.m2 - other.m2
        return '{} {}'.format(result1, result2)     # Here we have formatted to return only values not a tuple!!

    def __gt__(self, other):               # This is for overloading > operator between objects of Student class
        if self.m1 + self.m2 > other.m1 + other.m2:
            return True
        else:
            return False

    def __str__(self):                     # This is for overloading (which?) operator between objects of Student class
                                           # It is used to print using an OBJECT as the argument to print()
        return '{} {}'.format(self.m1, self.m2)     # Here we have formatted to return only values not a tuple!!


s1 = Student(55, 66)
s2 = Student(77, 88)
print(s1)                                   # This uses __str__ method
print(s2)                                   # This uses __str__ method


s3 = s1 + s2                                # This uses __add__ method
print(s3)

s4 = s1 - s2                                # This uses __sub__ method
print(s4)

if s1 > s2:                                 # This uses __gt__ method
    print('s1 Wins!')
else:
    print('s2 Wins!')

