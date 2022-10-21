from random import randint

def create_list():
    lis = []
    while len(lis) < 6:
        r = randint(-10, 10)
        if r not in lis:
            lis.append(r)
    return lis

def cocktail_sort(elem):
    n = len(elem)
    is_swapped = True
    begin = 0
    end = n-1

    while is_swapped:
        print(elem) 
        is_swapped = False
        for i in range (begin, end):
            if (elem[i] > elem[i+1]) :
                temp = elem[i]  
                elem[i] = elem[i+1]  
                elem[i+1] = temp 
                print(elem)
                is_swapped=True
        if not(is_swapped):
            break
        print(elem)
        is_swapped = False
        end = end-1
        for i in range(end-1, begin-1,-1):
           if elem[i] > elem[i + 1]:  
                temp = elem[i]  
                elem[i] = elem[i+1]  
                elem[i+1] = temp  
                print(elem)
                is_swapped = True
        begin = begin+1

def direction_sort(elem):
    count = int(input("\nВведіть: 1 - зростання | 2 - спадання: "))
    if count == 1:
        cocktail_sort(elem)
    elif count == 2:
        cocktail_sort(elem)
        elem.sort(reverse = True)
    else:
        print("\nНекоректно введені дані")


