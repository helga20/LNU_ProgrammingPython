@some_decorator
def some_function():
    pass

# The above code is equivalent to the following:

def some_function():
    pass # function's body

def some_decorator(func):
    pass # decorator's body

some_function = some_decorator(some_function)