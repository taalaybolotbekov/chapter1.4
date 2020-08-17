students = ['Taalay', 'Kirill', 'Arsen']
a = 'exit'
while True:
    user = input('Введите имя студента: ')

    students.append(user)
    if user == a:
        students.remove('exit')
        print(students)
        break
