def timer(func):
    from time import time
    def wrapper(*args, **kwargs):
        start_execution_time = time()
        result = func(*args, **kwargs)
        print(f"Execution time: {time()-start_execution_time} seconds")
        return result
    return wrapper

def uah(func):
    def wrapper(*args, **kwargs):
        return f"{func(*args, **kwargs)} грн."
    return wrapper

@timer
@uah
def money(deposit, years, percent):
    return round(deposit * (1 + percent / 100) ** years)

print(money(1000, 2, 10))