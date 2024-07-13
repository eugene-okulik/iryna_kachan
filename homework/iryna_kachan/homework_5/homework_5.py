# task_1 create variables from list
person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person
print(name)
print(last_name)
print(city)   
print(phone)
print(country)
# task_2 using method index
line_1 = 'результат операции: 42'
line_2 = 'результат операции: 514'
line_3 = 'результат работы программы: 9'
number_1 = int(line_1[line_1.index(':') + 2:]) + 10
number_2 = int(line_2[line_2.index(':') + 2:]) + 10
number_3 = int(line_3[line_3.index(':') + 2:]) + 10
print(number_1)
print(number_2)
print(number_3)
# task_3
students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
students = ', '.join(students)
subjects = ', '.join(subjects)
print('Students', students, 'study these subjects:', subjects)  # 1 version
text = 'Students %s study these subjects: %s'
print(text % (students, subjects))  # 2 version
text = 'Students {0} study these subjects: {1}'
print(text.format(students, subjects))  # 3 version
text = f'Students {students} study these subjects: {subjects}'  # 4 version
print(text)
