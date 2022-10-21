print(1)
number = int(input('Введіть число: '))
number_without_5 = number//10
product = number_without_5*(number_without_5+1)
result = product*100+25
print(number**2)
sep = " "
print(sep)
print(f"{number}^2=({number_without_5}*{number_without_5+1})25={result}")
