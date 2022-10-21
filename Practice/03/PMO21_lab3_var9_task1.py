file_names = 'names.txt'
file_ages = 'ages.txt'

with open(file_names, encoding='utf-8' ) as f:
    men_names = f.readline()
    women_names = f.readline()

with open(file_ages, encoding = 'utf-8') as datafile, \
     open('oldest.txt', 'w') as result_file:
    for names in datafile:
        names = names.rstrip()
        current_name = names.split(" ")[0]
        current_age = names.split(" ")[1]
        if current_name in men_names:
            name_dict  = dict({current_name : current_age})
            values = [float(x) for x in list(name_dict.values())]
            print(values)
            result_file.write(f"{current_name}\n")
            result_file.write(f"{values}\n")
            

            '''
            men_list  = list(current_age)
            max_men_age = men_list[0]
            for current_age in men_list:      
                if current_age > max_men_age:
                    max_men_age = current_age
                    result_file.write(f"{max_men_age}\n")
        elif current_name in women_names:
           result_file.write(f"{current_name}\n")
            'women_list  = list(current_age)
            max_women_age = women_list[0]
            for current_age in women_list:      
                if current_age > max_women_age:
                    max_women_age = current_age
                    result_file.write(f"{max_women_age}\n")
            '''


