user = input('Введите код : ')
password = 'init'
count = 1
b = user == password

while user != password:
    print("неправильные пароль", count)
    user = input('Введите код : ')
    count += 1
    if user == password:
        b = True
    elif count > 2:
        print('вы потратили все попытки')
        break
if b:
    print('Верно')
