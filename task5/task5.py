a = int(input('Введите число а: '))
b = int(input('Введите число b: '))
c = int(input('Введите число c: '))

i = a
k = 0
while i < b:
    i += 1
    if i % c == 0:
        k += 1
print('Делимых на c чисел : ', k)