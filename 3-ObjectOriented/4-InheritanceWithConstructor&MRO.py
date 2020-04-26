# Class can inherit single or multiple classes
# class C(A,B): means class C inherits classes A & B
# if class B(A) then class C(B) means C inherits both class A and B since B already inherits A

# initialization/constructor behavior:
#   - By default, if there is no constructor in sub class only then it will look for the super class and execute
#     super class's constructor. Otherwise it will execute only its own constructor
#   - We can explicitly call constructor/any method from super class using super.__init__ or super.method

# MRO: Method Resolution Order:
#   - Suppose, class C(A,B) and both class A and B have same method. If we use super.method inside class C, it will
#     always point to the method from left most class which is A in this case. So the order is from left to right


class A:

    def __init__(self):
        print('Constructor for class A')

    def feature1(self):
        print('Feature 1-A is working')

    def feature2(self):
        print('Feature 2 is working')


class B(A):

    def __init__(self):
        super().__init__()                  # This is to explicitly call the constructor of super class A
#                                           # absence of this statement will only execute constructor of current class B
        print('Constructor for class B')

    def feature1(self):
        print('Feature 1-B is working')

    def feature4(self):
        print('Feature 4 is working')


class C(B):

    def __init__(self):                     # absence of super() will only execute constructor of current class B
        print('Constructor for class C')

    def feature5(self):
        print('Feature 5 is working')


class D(B, A):                              # Absence of any constructor in D will check for availability of
                                            # constructors in super classes in the order from left to right.
                                            #  Hence in this case it will call constr of B which already calls con. of A

    def callsupermethod(self):
        super().feature1()                  # This will call the feature1 method from super class B NOT A, according to
#                                             the inheritance sequence which is (B,A) although feature1 method also
#                                             exist in class A


a1 = A()                                    # This will call constructor of A, of course
b1 = B()                                    # This will call constructor of A & B
c1 = C()                                    # This will call constructor of C only
d1 = D()                                    # No constructor defined, hence call constructor of B which already has
#                                             constructor of A

print('\nFor object a1 of class A: ')
a1.feature1()
a1.feature2()

print('\nFor object b1 of class B: ')
b1.feature1()
b1.feature2()
b1.feature1()
b1.feature4()

print('\nFor object c1 of class C: ')
c1.feature1()
c1.feature2()
c1.feature4()
c1.feature5()

print('\nFor object d1 of class D: ')
d1.callsupermethod()
d1.feature1()                               # This will call the feature1 method from super class B NOT A, according to
#                                             the inheritance sequence which is (B,A) although feature1 method also
#                                             exist in class A
