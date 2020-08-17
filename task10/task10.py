# user = input('Введите букву : ')
# password = ['privet']
# count = 2
# b = user == password
#
# while True:
#     print("буквы нету в слове\n", 'Ваша жизнь', count)
#     user == input('Введите букву : ')
#     count -= 1
#     if user == password:
#         b = True
#     elif count == 0:
#         print('вы потратили все попытки')
#         break
# if b:
#     print('Верно')


a = 'privet'
count = 3
while count > 0:
    b = input('Letter: ')
    if b in a:
        print('Index:', a.find(b))
    # elif a == b:
    #     break
    else:
        count -= 1
        print('Incorrect! Attempts left:', count)
print('Попытки закончились!')