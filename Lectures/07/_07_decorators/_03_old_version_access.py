# decorator: adds 'грн.' after result of function
def uah(func):
    def wrapper(*args, **kwargs):
        return f"{func(*args, **kwargs)} грн."
    return wrapper 

def money(deposit, years, percent):
    return round(deposit * (1 + percent / 100) ** years)

initial_money = money # memorizing initial function
money = uah(money) # decorating is here

print('1:', money(1000, 2, 10))

print('2:', initial_money(1000, 2, 10))