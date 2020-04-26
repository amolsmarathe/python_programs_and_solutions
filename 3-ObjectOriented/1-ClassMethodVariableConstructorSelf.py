# Classes, methods and variables can be created in python. Refer below short code.
# Class names usually start with capital letters which is not the case for vbles and methods
# __init__ is used to define INSTANCE variables. This is nothing but a Constructor, you can say, will be executed
# every time you create a new object
# Self always points to the self /current object under consideration. It is mandatory arg for each method in class
# Instance vs Class/Static variables: instance vble are particular to object while class vble are common to entire class
# class variables can be called by both classname.vble or object.vble
# when we change a class vble it will change the value for all objects created from this class
# instance method, class method, static method - explained in next file
# Note that vbles are of 2 types while methods are 3. for vbles, static vble and class vble is same but diff for method
# Whenever you're inside class, you must use 'self' for all variables and methods. Whereas outside class, it is taken
# care of by default


class Computer:
    def __init__(self, cpu, ram):  # initialize INSTANCE variables, this is nothing but a constructor
        self.cpu = cpu
        self.ram = ram
        print('\nConstructor executed for ', self)

    storage = 'HDD'                # This is a class vble common to all objects
    print('\nStorage type for all Computers is- ', storage)

    def printconfig(self):         # define method to print comp config
        print(''
              '\nConfig is- ', self.cpu, self.ram)

    def compare(self, other):      # define method to compare 2 objects
        if self.ram == other.ram:
            print('\nBoth are same')
        else:
            print('\nBoth are different')



comp1 = Computer('i5', '8GB')
comp2 = Computer('i7', '16GB')
comp3 = Computer('i9', '16GB')

comp1.printconfig()
comp2.printconfig()

comp2.compare(comp3)
comp1.compare(comp2)


print('\nAccess class vble using object.vble- ', comp1.storage)
print('\nAccess class variable using classname.vble- ', Computer.storage)
