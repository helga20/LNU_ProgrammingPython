from functions import *
from random import randint

list_1 = [randint(1, 100) for i in range(8)]
print("Список: ", list_1)
print("Кількість викинутих парних чисел:",  count_even(list_1))

print("---------------------------")

print("Кількість днів у 2021 році: ", days_in_year(2021))
print("Кількість днів у 2020 році: ",days_in_year(2020))



