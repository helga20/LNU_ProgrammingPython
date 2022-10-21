from random import uniform
n = int(input("n = "))

counter = 0 
for _ in range(n):
    x, y = uniform(-1, 1), uniform(-1, 1)
    if x**2 + y**2 <= 1:
        counter += 1
s = 4*counter / n
print(s)
    
