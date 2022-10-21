from functions import *

list_1 = create_list()
print("\nПочатковий список: ")
n = len(list_1)

for i in range(n):
   print (list_1[i],end = " ")

direction_sort(list_1)

print("\nВідсортований список:")
for i in range(n):
   print (list_1[i],end = " ")

print('')
