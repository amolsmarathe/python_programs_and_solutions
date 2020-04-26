
# Decorator concept is used when you want to extend an existing function with new code without changing existing func

# The function to be decorated is passed as an argument to the decorator function. decorator function has a wrapper
# function inside it which wraps some additional code around the function to be decorated and the decorator returns
# the wrapper function. After this, we can user the decorator as-
# @decorator
# def function_to_be_decorated():
#     pass

# Decorators are built on 2 concepts: Function inside function and Function as arg
# 1. Function inside function- inner function can only be executed inside the outer function. If you want to execute it
#    outside the outer function, 1/ outer function should return inner function and then 2/ outside the outer function,
#    create newfunction = outerfunction()
# 2. Function as arg- pass a function2 inside a function1, do some stuff, and then execute function 2 inside function1


# Basic Framework for this usage as decorator is given below (source-Udemy):
print('Example-1:')


def new_decorator(original_func):           # decorator function which is going to decorate orig func with new code
    def wrapper_func():                     # wrapper function is the actual wrap over the orig function and will be
        #                                     the function which the decorator returns
        print('Some extra code, before the original function')
        original_func()                     # This is the original function
        print('Some extra code, after the original function')
    return wrapper_func                     # decorator function will return the wrapper function NOTE that there are no
    #                                         parenthesis () which means that we are not executing wrapper func only
    #                                         returning it as a variable


# new_func = new_decorator(original_func)   # this is one way to implement the decorator but it is not common
# new_func()                                  it is only for understanding purpose

@new_decorator                              # This is the actual way to implement a decorator. if you simply comment
def original_func():                        # this one line, you can switch on and off the decorator. once switch off,
    pass                                    # the original function will behave as it is designed natively

# Example-1 (Telusku) there is a function to divide 2 numbers. create a new function using this function, new function
# will check which is the larger number and always keep it as denominator


def smart_div(func):             # new smart_div function of function - is a decorator
    def inner(a,b):              # inner function to check the condition and then swap the values - is a wrapper func
        if a < b:                # some code to check additional to original function
            a, b = b, a
        return func(a,b)         # wrapper function returns the execution of dummy (original) func(a,b) not the function
    return inner                 # new smart_div function returns inner function i.e. decorator returns wrapper function


@smart_div
def div(a,b):                    # Main function/original function for division of 2 numbers which needs to be decorated
    print('Division is- ', a/b)


div2 = smart_div(div)            # New function div2 OR use same name div so that old function will behave as modified.
#                                  new function is created using the decorator. this new function has additional stuff.
#                                  Although, this was only for understanding and actual implementation is using
#                                  @smart_div as given above

div2(2,4)                        # Calling the new function now

div(2,4)                         # Calling the decorated function

# Example-2 (Udemy) there is a function to divide 2 numbers. create a new function using this function. new function
# should check if the denominator is zero and if present, always keep it as numerator
print('\nExample-2:')


def divide(a,b):                    # original function
    return a/b


def decorator(origin_func):         # decorator
    def wrapper(a, b):              # wrapper function to wrap the original func with additional code
        if b == 0:
            a, b = b, a
        return origin_func(a, b)    # wrapper returns something using original function execution + additional code
    return wrapper                  # decorator returns wrapper


new_fun = decorator(divide)         # new function is created using the decorator


print(new_fun(2,0))                 # execute the new function
