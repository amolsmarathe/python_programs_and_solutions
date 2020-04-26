
# Some Theory:

# Basic 3 types of error-
# 1. compile time error - e.g. syntactical errors (syntax error)
# 2. logical error - code runs successfully and also gives output but that output is incorrect
# 3. run time error - error during run time e.g. due to wrong user input
#       Exception handling is for RUN TIME ISSUES!


# Types of errors in python:
# Name Error: when name of variable not defined
# Type Error: when trying to add int+str
# OS Error: when trying to write to a file which you don't have access to
# Syntax error: missing colan, etc.
# ZeroDivisionError: when trying to divide by zero

# Modules and packages:
# Module is just a .py script that you can call in another .py script
# Package is collection of Modules. A directory must contain __init__.py file(although empty),to recognize it as package
# Simply, package is the folder which contains (.py scripts which we call modules) and __init__.py file (although empty)
# Package can have numerous sub folders which will behave as subpackages provided that each sub folder has __init__.py

# IMPORT:
# When you import something,
# "from mymodule import myfunc" - you import a myfunc.py script from module
# "from mypackage import mymodule" - you import a module.py script from a package
# "from mypackage.subpackage import mysubscript/mysubmodule" - you import a module.py script from subpackage
# import mymodule Vs from mymodule import * -
#   -import mymodule: use mymodule.myfuc everytime you want to use the function from mymodule
#   -from mymodule import *: directly use myfuc() i.e.function name,everytime you want to use any function from mymodule
#   -from myapckage import *: ????? CHECK- CAN WE DIRECTLY USE FUNCTION NAMES or we have to use mymodule.myfunc()???



# __name__ and __main__ : refer Udemy video for any details or google

