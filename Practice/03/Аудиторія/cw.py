import os.path
import sys

filename = 'marks.txt'

if  not os.path.exists(filename) :
    sys.exit(f"File {filename} does not exist!")

course = input("Введіть дисципліну:  ")

with open(filename, encoding = 'utf-8') as datafile, \
     open('course.txt', 'w') as result_file:
    counter = marks = 0
    result_file.write(f"ДИСЦИПЛІНА: {course.upper()}\n")
    for line in datafile:
        line = line.rstrip()
        current_course = line.split(' - ')[1].split(' : ')[0]
        mark = int(line.split(' : ')[1])
        if current_course.lower() == course.lower() :
            result_file.write(line + '\n')
            counter += 1
            marks += mark
    result_file.write('-'*30 + '\n')
    if counter > 0:
        result_file.write(f"Середній бал: {marks/counter}")
    else:
        result_file.write(f"Дані відсутні")



'''
import os.path
import sys

filename = 'marks.txt'

if  not os.path.exists(filename) :
    sys.exit(f"File {filename} does not exist!")

course = input("Введіть дисципліну:  ")

with open(filename, encoding = 'utf-8') as datafile, \
     open('course.txt', 'w') as result_file:
    counter = marks = 0
    for line in datafile:
        line_copy = line.rstrip()
        minus_index = line_copy.find('-')
        semicolon_index = line_copy.find(':')
        current_course = line_copy[minus_index+2:semicolon_index-1]
        print(current_course)
   '''     




