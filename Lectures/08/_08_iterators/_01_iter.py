x = (x**2 for x in range(4))

while True:
    print(next(x))

x = (x**2 for x in range(4))

print(next(x))