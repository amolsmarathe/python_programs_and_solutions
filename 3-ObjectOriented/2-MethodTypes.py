# instance method, class method, static method - there are 3 types of methods
# instance method has further 2 types- Accessor (i.g. getter) & Mutator (i.e. setter)
# self arg is mandatory for inst method, can be called using both object.instmethod and classname.instmethod

# Note that vbles are of 2 types while methods are 3. for vbles, static vble and class vble is same but diff for method

# Creating class method needs a special decorator- @classmethod without which it is recognized as normal inst method
# class method needs cls as compulsory arg, it can be called only using classname.classmethod

# Creating static method needs a special decorator- @statismethod without which it is recognized as normal inst method
# static method needs on arg, can be called only using classname.staticmethod(), no args to be passed


class Student:

    def __init__(self):
        self.m1 = 0  # set initial value as zero
        self.m2 = 0
        self.m3 = 0

    # Instance methods (getter, setter and other methods) - to operate on object level

    def setmarks(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def getmarks(self):
        return self.m1, self.m2, self.m3    # NOTE - This will return a tuple!

    def calcavg(self):
        return (self.m1 + self.m2 + self.m3) / 3

    # Class methods - to operate on class level

    @classmethod
    def schoolinfo(cls):
        print('School for all students is \'Dnyan Probodhini\'')

    # Static methods - to operate independent of class or object

    @staticmethod
    def info():
        print('Education system in India is developing now-a-days')


# Execution:

std1 = Student()
std2 = Student()
print(std1.m1)                      # will print initial value which is zero
print(std2.m1)

std1.setmarks(53, 78, 56)           # wil set new values
std2.setmarks(87, 68, 90)

print(std1.getmarks())              # will get new values and print
print(std2.getmarks())


print(std1.calcavg())               # will calculate avg marks and print
print(std2.calcavg())

Student.schoolinfo()                # will get school name and print using class method

Student.info()                      # will run static method which which in independent of class and objects
#                                   # will print something about education system just static & independent statement

