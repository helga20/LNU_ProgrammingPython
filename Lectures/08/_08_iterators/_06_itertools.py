from itertools import permutations, combinations
 
names = ['Alice', 'Bob', 'Kate', 'Peter']

for item in permutations(names):
    print('1:', item)

for item in combinations(names, 2):
    print('2:', item)