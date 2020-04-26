
# Iterators in python can be created using __next__() and iter() methods (next() method is alternative to __next__())
# Iterators can be used with range, list, etc. and may sometimes replace the for loop
# NOTE: Both next() and __next() methods remember the last accessed index of the iteration
# Basically, for loop also uses __next__() method internally.
# CUSTOM iterators- iterator for object of the class. MUST define __iter__() & __next__() methods in that class
#                   this will create an iteration for the object (NOT for ATTRIBUTE of the object)


# Simple example to create an iterator to iterate through values in range

nums = range(10)            # this is a range through which we want to iterate without using for loop
list1 = list(range(5,10))

myiter1 = iter(nums)         # iter() method to create a new iterator for the range nums
print(myiter1.__next__())    # __next__() can be used to iterate to the next item in the iteration
print(next(myiter1))         # next() method is alternative to __next__()
#                              NOTE: Both next() and __next() methods remember the last accessed index of the iteration

myiter2 = iter(list1)        # creating iterator of a list
print(myiter2.__next__())
print(next(myiter2))


# Class level example of creating CUSTOM iterators for objects of the class:
# Following example iterates from first value 1 to next 10 values by getting a double each time

print('\nClass example: ')


class Doubles:
    def __init__(self):
        self.listdoubles = 1            # IMPORTANT: Initialize first value of the OBJECT (not the attribute) iterator
        #                                 Object (NOT THE ATTRIBUTE) is going to iterate from this starting value

    def __iter__(self):                 # MUST define __iter__() method
        return self                     # IMPORTANT: We must return the self! but WHY?????????? not clear.

    def __next__(self):                 # MUST define this method to get the next iteration of the object
        if self.listdoubles < 100:      # Object iteration will be doubled while current value is < 100
            self.listdoubles *= 2       # Modify current iteration of the object to get next value in the iteration
            return self.listdoubles     # return the modified value as next value of object's iteration
        else:
            raise StopIteration


values = Doubles()          # Create an object of the class. this object will be iterable

print(next(values))         # NOTE: Although this gives the first value in the iteration, upcoming for loop will start
#                                   from the second iteration and will NOT REPEAT the first iteration. Because previous
#                                   iteration index is always stored by __next__() or next() method

for i in values:            # for each iteration in the object 'values', we will print it, REMEMBER, it will
    print(i)                # automatically start from SECOND ITERATION because the first was already executed
    #                         above an it stores previous iteration index








