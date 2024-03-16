sybols = ["%", "*", "$", "?"]
passowrd = input("Введите пароль: ")
for i in passowrd:
    if i in sybols:
        print("Введен запрещенный символ:", i)
        break

