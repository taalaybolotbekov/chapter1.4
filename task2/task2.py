o = []
e = []
i = 0
while i < 21:
    if i % 2 == 0:
        o.append(i)
    else:
        e.append(i)
    i += 1
print('Нечетные числа: ', e)
print('четные числа: ', o)