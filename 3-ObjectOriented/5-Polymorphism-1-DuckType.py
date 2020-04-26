# Poly- multiple, morph- forms. i.e. one thing in different forms
# Types of Polymorphism:
#   - Duck Typing
#   - Operator Overloading
#   - Method Overloading
#   - Method Overriding

# Duck Typing- same method name in 2 "independent" classes (somewhat related to the Interface topic in Java)
#   - pass an object as arg to a method and no matter which class the object belongs to, if that class has the method
#     to execute, it doesn't affect code


class Pycharm:
    def execute(self):
        print('Welcome to Pycharm!')


class MyEditor:
    def execute(self):
        print('Welcome to MyEditor!')


class Test:
    def code(self, ide):
        ide.execute()


ide = Pycharm()
t1 = Test()
t1.code(ide)              # At this execution, ide.execute will be called from Pycharm class

ide = MyEditor()
t1.code(ide)              # At this execution, ide.execute will be called from MyEditor class
#                         Hence the object is of different class but both the classes have execute method hence it works



