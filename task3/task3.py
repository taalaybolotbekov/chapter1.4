user = int(input('Enter the password:'))
count = 1
while user != 8:
    print("число не верно")
    user = int(input('Введите число:'))
    count += 1
else:
    print('верное')
