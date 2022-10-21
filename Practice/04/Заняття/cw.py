m, n = 4, 5
squares = [(1, 1, 2, 2), (2, 2, 3, 4)]

s = set()
union_set = set()

for i in range(m):
    for j in range(n):
        s.add((i, j))
        
for square in squares:
    for i in range(square[0],  square[2]+1) :
        for j in range(square[1], square[3]+1) :
            union_set.add((i, j))
            
k = len(s-union_set)

text = ' '
for i in range(m):
    for j in range(n):
        if (i, j) in union_set:
            text += '+ '
        else:
             text += '-  '
    text += '\n'

print(text)          
print("Кількість незайнятих клітинок - ", k)

