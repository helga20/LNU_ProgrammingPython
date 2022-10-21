from sys import getsizeof

s1 = sum([x**2 for x in range(10**6)])
s2 = sum((x**2 for x in range(10**6)))

print('1:', s1, s2)

x1 = [x**2 for x in range(10**6)]
x2 = (x**2 for x in range(10**6))

print('2:', getsizeof(x1), getsizeof(x2))