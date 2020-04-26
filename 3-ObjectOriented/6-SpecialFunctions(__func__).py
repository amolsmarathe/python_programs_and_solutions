# Functions with double underscore are special functions
# Not only as operator overload (like add, sub, etc.) but we can also use such functions as __len__ and __str__
# __str__ can be used to print any object of a class! because print function also takes what str function returns

# Following example is for __str__() and __len__() special methods


class Dog:
    def __init__(self, name, count):
        self.name = name
        self.count = count

    # At this point, we cannot print the objects of Dog() class using print methond.
    # Se we define __str__() in Dog() class

    def __str__(self):
        return self.name

    # At this point, we cannot get the length/size of objects of Dog() class using len methond.
    # So we define __len__() in Dog() class

    def __len__(self):
        return self.count


dog = Dog('Rookie', 20)

print(dog)  # Now we can use print method on dog objects to print their names
n = len(dog)  # Now we can use len method on dog objects to get count of these dogs
print(n)
