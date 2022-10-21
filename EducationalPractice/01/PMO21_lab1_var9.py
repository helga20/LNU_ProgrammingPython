from route_func import *

file_name = 'routes_data.txt'
with open(file_name, encoding = 'utf-8') as datafile:
    routes_list = []
    for r in datafile:
        d_list = []
        for i in range(2, len(r.split(', '))):
            d_list.append(int(r.split(', ')[i]))
        routes_list.append(Route(r.split(', ')[0], r.split(', ')[1], d_list))
        
print("\nМаршрути:")
print_on(routes_list)

print("\nМаршрути за протяжністю:")
routes_list.sort()
print_on(routes_list)

print("\nМаршрути з максимальною кількістю привалів:")
print_on(routes_max_stop(routes_list))

print("\nМаршрути з найдовшим переходом:")
print_on(longest_distance(routes_list))

print("\nМаршрути з початком у Чорногорі:")
print_on(start_in_certain_point('Чорногора', routes_list))

print("\nМаршрути з кінцем у Дземброні:")
print_on(end_in_certain_point('Дземброня', routes_list))

