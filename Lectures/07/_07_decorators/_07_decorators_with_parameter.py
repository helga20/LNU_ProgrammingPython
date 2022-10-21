def validate_number(minimum=None, maximum=None):
    def wrapper(func):
        def inner(arg):
            if not isinstance(arg, (int, float)):
                raise TypeError(f'Argument must be int or float, not {type(arg)}')
            if minimum is not None and arg < minimum:
                raise ValueError(f'Argument must be over {minimum}')
            if maximum is not None and arg > maximum:
                raise ValueError(f"Argument must be under {maximum}")
            return func(arg)
        return inner
    return wrapper

# @validate_number(minimum=0)
def sqrt(x):
    return x ** 0.5

print('1:', sqrt(-2))