o = []
e = []
i = 0
user = int(input('Введите сколько вам лет: '))
while i < user:
    if i % 2 == 0:
        o.append(i)

    elif i % 2 != 0:
        e.append(i)

    i += 1
if user % 2 == 0:
    print('четные числа: ', o)
else:
    print('нечетные числа: ', e)

# age = int(input('Age: '))
# a = 0 if age%2==0 else 1
# while a<=age:
#     print(a)
#     a+=2