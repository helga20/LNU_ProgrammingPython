'''entered = int(input('Введіть секунди: '))
hour = entered // 3600
minute = entered % 3600 // 60
second = entered % 3600 % 60
print(f"{hour}:{minute}.{second}")'''

def second_func(entered):
    hour = entered // 3600
    minute = entered % 3600 // 60
    second = entered % 3600 % 60
    print(f"{hour}:{minute}.{second}")

second_func(25)

