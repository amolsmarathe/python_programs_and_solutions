# Method Overload (within same class): 2 methods exist with same name but different number of args
#   - NOT supported as it is in python,we CANNOT have 2methods with same name in python. But there is a similar concept
#   - In python,we define method with arg=None &while creating an object,it will get default value None if arg is absent
#   - This itself can be called as a similar concept to Method overload

# Method Override (within 2 diff. classes): 2 methods exist with same name and same no. of args but in different classes
#   - When we inherit the classes i.e. class B(A) and both A and B have same methods, preference is given to
#   - the method from class B over class A. This is called method override


# Method Overload Example:

class Addition:

    def add(self, a=None, b=None, c=None):
        sum = 0

        if a != None and b != None and c != None:
            sum = a + b + c
        elif a != None and b != None:
            sum = a + b
        else:
            sum = a

        return sum


a1 = Addition()
print(a1.add(5, 6, 7))  # In this way, we have overloaded same method 'add' by passing different no. of args
print(a1.add(5, 6))
print(a1.add(5))


# Method Override Example:

class A:

    def printfun(self):
        print('Fun in Class A')


class B(A):

    def printfun(self):                 # this method overrides the method in class A
        print('Fun in Class B')


b1 = B()
b1.printfun()


