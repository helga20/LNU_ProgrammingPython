from functools import wraps

# decorator: adds 'грн.' after result of function
def uah(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return f"{func(*args, **kwargs)} грн."
    return wrapper 

@uah
def money(deposit, years, percent):
    return round(deposit * (1 + percent / 100) ** years)

print('1:', money(1000, 2, 10))

print('2:', money.__name__) # but it is impossible to call initial version