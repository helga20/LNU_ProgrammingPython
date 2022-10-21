session = {'Кравець Ольга': {'Програмування': 98, 'Архітектура': 93, 'Матан': 96},
           'Барський Андрій': {'Програмування': 92, 'Дискретна': 91, 'Матан': 96},
           'Ласько Маркіян' : {'Архітектура': 51, 'Матан': 40}
           }

top_students = []
stats_1 = {} # course: number_of_students

for i, student in enumerate(session):
    print(f'{i+1}. {student.upper()}')
    is_top = True
    for course, mark in session[student].items():
        print(f"{course} - {mark}")
        if mark < 90:
            is_top = False
        if course not in stats_1:
            stats_1[course] = 1
        else:
            stats_1[course] += 1
    if is_top:
        top_students.append(student)

print(top_students)
print(stats_1)
        
        
