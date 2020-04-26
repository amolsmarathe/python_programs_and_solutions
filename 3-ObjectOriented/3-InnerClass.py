# We can create a class inside the class
# There is no default/necessary link/relatoin between objects of outer and inner class. How to build that connection????


# Example -
# Student is a class which has
#   - name and age variables
#   - show method to print all the info about a student
#   - Laptop class which has-
#       - brand, cpu, ram variables
#       - show method to print all the info about the laptop

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.lap = self.Laptop()           # THIS STEP IS IMP. creating new OBJECT for self i.e. 'self.Laptop()'
#                                          # This newly created object will be assigned as variable to self i.e.self.lap
#                                     # No need to create lap objects outside Student class as we created it here itself
#                                     Sill we can otherwise choose not to create lap object here and create them
#                                     outside Student class instead

    def show(self):
        print('\nName of the student is- ', self.name, ' and age is- ', self.age)
        self.lap.show()                    # THIS STEP IS IMP. you should call the method for self.lap object
#                                           NOTE that this show method is from Laptop class

    class Laptop:

        def __init__(self):
            self.brand = ''
            self.cpu = ''
            self.ram = ''

        def setlapconfig(self, brand, cpu, ram):
            self.brand = brand
            self.cpu = cpu
            self.ram = ram

        def show(self):
            print('Laptop config for this student is- ', self.brand, self.cpu, self.ram)


std1 = Student('Amol', 28)
std2 = Student('Saurabh', 25)

std1.lap.setlapconfig('HP', 'i5', '32GB')
std2.lap.setlapconfig('DELL', 'i7', '16GB')

std1.show()
std2.show()

