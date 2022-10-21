from math import factorial

def timer(func):
    from time import time
    def wrapper(*args, **kwargs):
        start_execution_time = time()
        result = func(*args, **kwargs)
        print(f"Execution time: {time()-start_execution_time} seconds")
        return result
    return wrapper

@timer
def money(deposit, years, percent):
    return round(deposit * (1 + percent / 100) ** years)

@timer
def length_of_factorial(x):
    return len(str(factorial(x)))


print('1:', money(1000, 2, 10))

print('2:', length_of_factorial(100000))

