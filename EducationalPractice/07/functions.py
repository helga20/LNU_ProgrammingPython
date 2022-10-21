import calendar

#16.Функція отримує аргументом список цілих чисел, викидає з нього парні і повертає кількість викинутих чисел. 
def count_even(myList):
    count = 0
    for item in myList:
        if int(item) % 2 == 0:
            count += 1           
    return count

#8.Функція отримує аргументом рік у вигляді цілого числа та повертає кількість днів у ньому. 
def days_in_year(year):
    days = 0
    if year > 0:
        if calendar.isleap(year):
            days = 366
        else:
            days = 365
    return days



'''#8.Функція отримує аргументом рік у вигляді цілого числа та повертає кількість днів у ньому. 
def days_in_year(year):
    days = 0
    if year > 0:
        if year % 4 == 0 and year % 100 != 0:
            days = 366
        elif year % 400 == 0:
            days = 366
        else:
            days = 365
    return days'''

