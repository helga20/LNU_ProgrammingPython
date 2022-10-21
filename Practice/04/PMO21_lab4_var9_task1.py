from random import randint as rnd
from math import sqrt

N = int(input("Введіть N: "))
begin_list = [rnd(1, 10000) for i in range(N)]

print("Початковий список: ", begin_list)
list_with_sqrt = []
finish_list = []

for number in begin_list:
    if sqrt(number) == round(sqrt(number)):
        list_with_sqrt.append(number)
    else:
        finish_list.append(number)
    
print("Кількість повних квадратів:",  len(list_with_sqrt))
print ("Список повних квадратів: ", list_with_sqrt)

finish_list.sort(reverse = True)
print ("Кінцевий список (сортований): ",finish_list)

