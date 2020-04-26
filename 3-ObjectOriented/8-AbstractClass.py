# What is Abstract Class?
# abc module-  Python does not support Abstract classes by default but we have abc module to use Abstract classes
# abc = Abstract Base Classes - Every class which inherits the class ABC in abc, is an Abstract Class
# Abstract class is a class which has at least one abstract method. Use decorator @classmethod to set method as abstract
# Abstract method only has declaration (only pass inside method) does not have any definition.

# When 2 Use- Abstract classes are used to define the structure. Other classes will inherit Abstract classes.
# Every abstract method MUST BE defined by the class which inherits Abstract class. CHECK THIS. IT IS NOT MANDATORY?????

from abc import ABC


class Computer(ABC):  # Class Computer becomes Abstract class since it inherits ABC

    @classmethod      # This defines an Abstract method which should not contain any definition
    def process(self):
        pass


class Laptop(Computer):  # Now it is mandatory for Programmer class to implement all abstract methods of Computer???
    def process(self):       # If we do not define this method, we get an error - NO ERROR WHY???????????
        print('\nThis is the method implemented from an abstract class')


p1 = Laptop()
p1.process()
